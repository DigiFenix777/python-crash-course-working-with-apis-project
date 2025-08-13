from operator import itemgetter
import requests
import plotly.express as px



# Make an API call and check the response.
url = "https://hacker-news.firebaseio.com/v0/topstories.json"
r = requests.get(url)
print(f"Status code: {r.status_code}")

# Process information about each submission.
submission_ids = r.json()

submission_dicts = []
for submission_id in submission_ids[:30]:
    # Make a new API call for each submission.
    url = f"https://hacker-news.firebaseio.com/v0/item/{submission_id}.json"
    r = requests.get(url)
    print(f"id: {submission_id}\tstatus: {r.status_code}")
    response_dict = r.json()

    # Build a dictionary for each article.
    try:
        submission_dict = {
            'title': response_dict['title'],
            'hn_link': f"https://news.ycombinator.com/item?id={submission_id}",
            'comments': response_dict['descendants']
        }

        submission_dicts.append(submission_dict)
    except KeyError:
        # Handle cases where 'descendants' key might be missing (e.g., promotional posts).
        print(f"Skipping submission {submission_id}: 'descendants' key not found.")

submission_dicts = sorted(submission_dicts, key=itemgetter('comments'),
                          reverse=True)

story_links, sub_comments = [], []
for submission_dict in submission_dicts:
    # Turn story names into active links.
    story_title = submission_dict['title']
    story_url = submission_dict['hn_link']
    story_link = f"<a href='{story_url}'>{story_title}</a>"
    story_links.append(story_link)
    sub_comments.append(submission_dict['comments'])
    print(f"\nTitle: {submission_dict['title']}")
    print(f"Discussion link: {submission_dict['hn_link']}")
    print(f"Comments: {submission_dict['comments']}")

# Make a visualization.
title = "Most Commented Stories on Hacker News!"
labels = {'x': 'Story', 'y': 'Number of Comments'}
fig = px.bar(x=story_links, y=sub_comments, title=title, labels=labels)

fig.update_layout(title_font_size=28, xaxis_title_font_size=20, yaxis_title_font_size=20)
fig.show()
