import requests
import json

base_url = 'https://api.github.com/users/dlm6693/repos'
url_params = {'visibility':'public'}
response = requests.get(url=base_url, params=url_params)

repo_names = []
for item in response.json():
    repo_names.append(item.get('name'))
print(repo_names)