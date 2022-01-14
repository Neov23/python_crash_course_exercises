# Exercise 17-2

from os import link
from plotly.graph_objs import Bar
from plotly import offline

from operator import itemgetter

import requests

# Make an API call and store the response.
url = 'https://hacker-news.firebaseio.com/v0/topstories.json'
r = requests.get(url)
print(f"Status code: {r.status_code}")

# Process information about each submission.
submission_ids = r.json()
submission_dicts = []
for submission_id in submission_ids[:10]:
    # Make a separate API call for each submission.
    url = f"https://hacker-news.firebaseio.com/v0/item/{submission_id}.json"
    r = requests.get(url)
    print(f"id: {submission_id}\tstatus: {r.status_code}")
    response_dict = r.json()

    # Build a dictionary for each article
    try:
        submission_dict = {
            'title': response_dict['title'],
            'hn_link': f"http://news.ycombinator.com/item?id={submission_id}",
            'comments': response_dict['descendants'],
        }
        submission_dicts.append(submission_dict)
    except KeyError:
        submission_dict = {
            'title': response_dict['title'],
            'hn_link': f"http://news.ycombinator.com/item?id={submission_id}",
            'comments': 0,
        }
        submission_dicts.append(submission_dict)

print("\nInformation process about each submission completed.\n")

submission_dicts = sorted(submission_dicts, key=itemgetter('comments'),
    reverse=True)

comments, links = [], []
for submission_dict in submission_dicts:
    comments.append(submission_dict['comments'])
    
    title = submission_dict['title']
    url = submission_dict['hn_link']
    html_link = f"<a href={url}>{title}</a>"
    links.append(html_link)

# Visualize top 10 articles (sorted by comment quantity)
data = [{
    'type': 'bar',
    'x': links,
    'y': comments,
    'marker': {
        'color': 'rgb(0, 160, 0)',
        'line': {'width': 2, 'color': 'rgb(0, 0, 0)'}
    },
}]

my_layout = {
    'title': 'Top 10 commented articles of Hacker News',
    'titlefont': {'size': 38},
    'xaxis': {
        'title': 'Articles',
        'titlefont': {'size': 28},
        'tickfont': {'size': 15},
    },
    'yaxis': {
        'title': 'Comments',
        'titlefont': {'size': 28},
        'tickfont': {'size': 15},
    },
}

fig = {'data': data, 'layout': my_layout}
offline.plot(fig, filename='exercise_17_02.html')