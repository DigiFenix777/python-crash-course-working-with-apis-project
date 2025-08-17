# 🔗 Working with APIs in Python

<!-- 📛 Project Badges -->
![Last Commit](https://img.shields.io/github/last-commit/DigiFenix777/python-crash-course-working-with-apis-project)
![Top Language](https://img.shields.io/github/languages/top/DigiFenix777/python-crash-course-working-with-apis-project)
![Repo Size](https://img.shields.io/github/repo-size/DigiFenix777/python-crash-course-working-with-apis-project)
![Issues](https://img.shields.io/github/issues/DigiFenix777/python-crash-course-working-with-apis-project)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)


## 🔑 Executive Summary
This project demonstrates how to use **Python for interacting with web APIs**, processing responses, and creating meaningful visualizations. The examples use GitHub’s API, Hacker News, and the National Vulnerability Database (NVD), but the same workflow is directly applicable to cybersecurity operations:

- Automating **vulnerability intelligence** collection from APIs.
- Parsing and analyzing **JSON data** from threat intelligence feeds.
- Visualizing **trending CVEs, attack surfaces, or incident metrics**.
- Building **repeatable, testable Python scripts** for security workflows.

👉 For recruiters and hiring managers: this project highlights my ability to **query APIs, handle real-world data, and visualize security trends** in ways that are critical to threat monitoring and compliance reporting.

---

## 📌 Overview

Key lessons explored in this project:

- Making **HTTP requests** with Python’s `requests` library.
- Handling JSON response objects and error codes.
- Summarizing API data (e.g., top GitHub repositories).
- Monitoring and respecting **API rate limits**.
- Creating visualizations with **Plotly** (interactive bar charts with tooltips, links, and custom styling).
- Querying multiple APIs, including the **Hacker News API** and **NIST NVD API**.

---

## 🧠 Skills & Concepts

- Working with REST APIs (`requests`, JSON parsing).
- Data processing with Python dictionaries & lists.
- API rate limiting and error handling.
- Visualization with **Plotly** (interactive charts).
- Testing with **pytest** for API response validation.
- Applying results to **cybersecurity use cases** (CVE monitoring, threat dashboards).

---

## 🗂️ Repository Structure

```plaintext
project-working-with-apis/
│
├── data/                     # Empty
├── docs/                     # Empty
│
├── images/portfolio/         # Exported plots
│   ├── Most Commented Stories on Hacker News.png
│   ├── Most Starred Python Projects on GitHub.png
│   └── NIST NVD Last 30 CVEs.png
│
├── src/                      # Python scripts for lessons & exercises
│   ├── __init__.py
│   ├── active_discussions.py
│   ├── further_exploration.py
│   ├── hn_article.py
│   ├── hn_submissions.py
│   ├── main.py
│   ├── other_languages.py
│   ├── python_repos.py
│   ├── python_repos_visual.py
│   └── testing_python_repos.py
│
├── tests/                    # Unit tests with pytest
│   └── test_python_repos.py
│
├── .editorconfig
├── .gitattributes
├── .gitignore
├── .pre-commit-config.yaml
├── LICENSE
├── README.md
├── requirements.lock.txt
└── requirements.txt
```

---


## 🚀 How to Run

1. Clone this repo and move into the folder:
```bash
git clone git@github.com:your-username/project-working-with-apis.git
cd project-working-with-apis
```

2. (Optional) Create a virtual environment:
```bash
python3 -m venv .venv
source .venv/bin/activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Run an example script, such as:
```bash
python src/python_repos.py
```

---

## 🔎 Skills Spotlight

- **API** calls & **JSON parsing** with Python requests.
- **Plotly** for interactive visualization (custom tooltips, links, colors).
- **Testing** API integrations with pytest.

Applying API workflows to cybersecurity:
- **Consuming** NVD API for CVE data.
- **Building** charts of vulnerabilities by severity.
- **Automating** intelligence reporting.


---


## 📝 Lessons Learned
- How to authenticate and query APIs reliably.
- How to process large JSON responses with error handling.
- Why monitoring rate limits is critical for scalability.
- How interactive charts can make technical data accessible to executives.

**Direct tie-ins**:
vulnerability scanning feeds, SOC dashboards, and compliance reporting tools all rely on these skills.


---


## 📊 Exercises Implemented

**17-1: Other Languages** → Visualized most popular projects in non-Python languages (JS, Ruby, Go, etc.).

**17-2: Active Discussions** → Bar chart of top Hacker News threads by comment count, with clickable links.

**17-3: Testing GitHub API Calls** → Used pytest to confirm status codes and API response properties.

**17-4: Further Exploration (Cybersecurity)** → Queried NIST NVD API for latest CVEs, filtered for “Analyzed,” and plotted CVSS 3.1 scores by severity band (Low/Medium/High/Critical) with custom tooltips.


---


## 🌍 Data Sources

**GitHub API** → repository metadata: [GitHub API](https://api.github.com/search/repositories)

**Hacker News API** → active discussions: [Hacker News API](https://hacker-news.firebaseio.com/v0/topstories.json)

**NIST NVD API** → latest CVEs and vulnerability metrics: [NIST NVD API 2.0](https://services.nvd.nist.gov/rest/json/cves/2.0)

Exercises adapted from Python Crash Course, 3rd Edition by Eric Matthes (No Starch Press).


---


## 📚 Attribution

Based on exercises from:
Matthes, E. (2023). Python Crash Course (3rd ed.). No Starch Press.
Book website


---

## 🧩 License

Distributed under the MIT License.
See LICENSE for details.


---
