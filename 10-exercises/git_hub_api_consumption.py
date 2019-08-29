import requests, json
from dateutil.parser import parse as parse_date
from collections import Counter

rileys_repos_endpoint = 'https://api.github.com/users/rileyL6122428/repos'
rileys_repos = json.loads(requests.get(rileys_repos_endpoint).text)

creation_dates = [
    parse_date(repo['created_at'])
    for repo
    in rileys_repos
]

weekday_counts = Counter(date.weekday() for date in creation_dates)
month_counts = Counter(date.month for date in creation_dates)
year_counts = Counter(date.year for date in creation_dates)

print('weekdate_counts = %s' % weekday_counts)
print('month_counts = %s' % month_counts)
print('year_counts = %s' % year_counts)
# print(creation_dates)
