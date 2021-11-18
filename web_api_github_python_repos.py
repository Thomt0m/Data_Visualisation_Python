# Request data from GitHubs API and visualise it
# ! Data is imcomplete, and varies with each call !


import requests

from plotly.graph_objects import Bar
from plotly import offline






# Make an API call and store the response
url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
headers = {'Accept': 'application/vnd.github.v3+json'}
r = requests.get(url=url, headers=headers)

# Print some info on about the call being made
print(f'Calling {url}')
print(f'Status code: {r.status_code}')

# Store the response in a variable
response_dict = r.json()

# Print some info on the information recieved
print(f'total_count = {response_dict["total_count"]}')
print(f'incomplete_results = {response_dict["incomplete_results"]}')

# Access the items (repos)
repo_dicts = response_dict['items']
print(f'Repositories returned: {len(repo_dicts)}')


# Data to retrieve
repo_links_and_names = []
repo_stars = []
repo_labels = []
repo_links = []

for repo_dict in repo_dicts:
    repo_url = repo_dict['html_url']
    repo_links_and_names.append(f'<a href="{repo_url}">{repo_dict["name"]}</a>')
    repo_stars.append(repo_dict['stargazers_count'])
    repo_labels.append(f'{repo_dict["owner"]["login"]}<br />{repo_dict["description"]}')





# Visualise the data
data = [{
    'type': 'bar',
    'x': repo_links_and_names,
    'y': repo_stars,
    'hovertext': repo_labels,
    'marker': {
        'color': 'rgb(60, 100, 150)',
        'line': {'width': 1.5, 'color': 'rgb(25, 25, 25)'},
    },
    'opacity': 0.6,
}]
layout = {
    'title': 'Most-Starred Python Projects on GitHub',
    'titlefont': {'size': 24},
    'xaxis': {
        'title': 'Repository',
        'titlefont': {'size': 18},
        'tickfont': {'size': 12},
    },
    'yaxis': {
        'title': 'Stars',
        'titlefont': {'size': 18},
        'tickfont': {'size': 12},
    },
}

fig = {'data': data, 'layout': layout}
offline.plot(fig, filename='python_repos.html')

