import requests, json
from collections import Counter
from dateutil.parser import parse

github_api_url = "https://api.github.com/users/junglelk"

endpoint = github_api_url + "/repos"
repos = requests.get(endpoint).json()
# print(repos)
dates = [parse(repo['created_at']) for repo in repos]
for date in dates:
    print(date.__format__('%b %d, %Y %H:%M:%S'))

last_5_repositories = sorted(repos, key=lambda r: r['pushed_at'], reverse=True)[:5]
last_5_languages = [repo['language'] for repo in last_5_repositories]
print(last_5_languages)
