import requests
import pandas as pd
import plotly.express as px
import textwrap

# Make an API call to NIST NVD API, and store the response.
url = "https://services.nvd.nist.gov/rest/json/cves/2.0"
url += "?pubStartDate=2025-01-01T00:00:00.000Z&pubEndDate=2025-01-30T00:00:00.000Z&noRejected&resultsPerPage=200"
r = requests.get(url)
print(f"Status code: {r.status_code}")

# Explore the structure of the data.
response_dict = r.json()
first_item = response_dict['vulnerabilities'][0]
cve = first_item['cve']


# Get the 30 latest CVEs from the API (200 non-rejected results per call).
cve_ids = r.json()
target_dicts = 30
cve_dicts = []

cve_dict = cve_ids['vulnerabilities']

for cve_item in cve_dict:
    cve = cve_item['cve']
    if cve['vulnStatus'] == 'Analyzed':
        cve_dicts.append(cve)
        if len(cve_dicts) == target_dicts:
            break

cve_names, cve_scores, hover_texts = [], [], []
line_break = "<br>"

for cve_dict in cve_dicts:
    # Build a dictionary for each CVE.
    cve_names.append(cve_dict['id'])
    cve_scores.append(cve_dict['metrics']['cvssMetricV31'][0]['cvssData']['baseScore'])
    description = cve_dict['descriptions'][0]['value']

    # Wrap the description to ~60 characters per line.
    wrapped_description = line_break.join(line.strip() for line in textwrap.wrap(description, width=60))

    # Hover text data.
    title = cve_dict['id']
    date = cve_dict['published']
    cvss_vector = cve_dict['metrics']['cvssMetricV31'][0]['cvssData']['vectorString']
    score = cve_dict['metrics']['cvssMetricV31'][0]['cvssData']['baseScore']
    vector = cve_dict['metrics']['cvssMetricV31'][0]['cvssData']['attackVector']
    confidentiality = cve_dict['metrics']['cvssMetricV31'][0]['cvssData']['confidentialityImpact']
    integrity = cve_dict['metrics']['cvssMetricV31'][0]['cvssData']['integrityImpact']
    availability = cve_dict['metrics']['cvssMetricV31'][0]['cvssData']['availabilityImpact']
    value = cve_dict['weaknesses'][0]['description'][0]['value']

    # Build the hover parts -- CVS vector remains on one line.
    hover_parts = [
        title,
        date,
        line_break,
        wrapped_description,
        line_break,
        f"{cvss_vector}",     # stays whole
        f"Score: {score}",          # stays whole
        line_break,
        f"Attack vector: {vector}",
        f"Confidentiality: {confidentiality}",
        f"Integrity: {integrity}",
        f"Availability: {availability}",
        value
    ]

    hover_parts = [str(p) for p in hover_parts if p is not None]
    hover_text = line_break.join(hover_parts)
    hover_texts.append(hover_text)

# NVD CVSS v3.1 severity bands with Pandas
df = pd.DataFrame({
    "CVE_ID": cve_names,        # same length as cve_scores
    "Score": cve_scores,
    "Hover": hover_texts        # if you want custom hover
})

df["Score"] = pd.to_numeric(df["Score"], errors="coerce")

bins = [-0.001, 0.0, 3.9, 6.9, 8.9, 10.0]
labels = ["None", "Low", "Medium", "High", "Critical"]

df["Severity"] = pd.cut(
    df["Score"],
    bins=bins,
    labels=labels,
    include_lowest=True,    # puts 0.0 into "None"
    right=True              # default; (a, b]
)

df["Severity"] = df["Severity"].cat.add_categories(["Unknown"]).fillna("Unknown")
cat = pd.CategoricalDtype(
    categories=["None", "Low", "Medium", "High", "Critical", "Unknown"],
    ordered=True
)
df["Severity"] = df["Severity"].astype(cat)

# CVE color mapping.
color_discrete_map = {
    'None': "#808080",      # gray
    'Low': "#00CC00",       # green
    'Medium': '#FFCC00',    # yellow
    'High': '#FF9900',      # orange
    'Critical': '#FF0000'   # red
}
# Make visualization.
title = "Last 30 Scored Vulnerability IDs and Summaries"
plot_labels = {'x': 'Vulnerability IDs and Summaries', 'y': 'CVSS Severity'}
fig = px.bar(
    df,
    x="CVE_ID",
    y="Score",
    color="Severity",
    custom_data=["Hover"],
    title="Last 30 Scored Vulnerability IDs and Summaries",
    labels=plot_labels,
    color_discrete_map=color_discrete_map
)

fig.update_traces(hovertemplate="%{customdata[0]}<extra></extra>", hoverlabel=dict(align="left"))
fig.update_layout(title_font_size=28, xaxis_title_font_size=20, yaxis_title_font_size=20, yaxis=dict(range=[0, 10]))

fig.show()
