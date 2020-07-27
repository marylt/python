import requests
import json

'''
headers1 = {'X-API-KEY': 'VhLxdiMEePfmVuyeEP5akYvbDBBG5qdJpDlXsYkC'}
headers2 = {'X-API-KEY': 'VhLxdiMEePfmVuyeEP5akYvbDBBG5qdJpDlXsYkC'}

url1 = 'https://api.propublica.org/congress/v1/116/house/members.json'
url2 = 'https://api.propublica.org/congress/v1/116/senate/members.json'

housemembers = requests.get(url1, headers = headers1).json()
senatemembers = requests.get(url2, headers = headers2).json()

housememberss = json.dumps(housemembers, indent = 2)
senatememberss = json.dumps(senatemembers, indent = 2)

print(housememberss)
print(senatememberss)
'''

housedob = []
senatedob = []

def get(url):
    headers = {'X-API-KEY': 'VhLxdiMEePfmVuyeEP5akYvbDBBG5qdJpDlXsYkC'}
    url = 'https://api.propublica.org/congress/v1' + url
    data = requests.get(url, headers = headers).json()
    return data['results']

for member in get('/116/house/members/json'):
    housedob.append(member['date_of_birth'])
for member in get ('/116/senate')
