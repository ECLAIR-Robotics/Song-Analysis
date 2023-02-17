import config
import requests

headers = {
    'user-agent': config.USER_AGENT 
}

params = {
    'artist': 'Imagine',
    'track': 'John Lennon',
    'api_key': config.API_KEY,
    'method': 'track.getTags',
    'format': 'json',
    'user': 'sarahwz'
}

url = 'http://ws.audioscrobbler.com/2.0/'
#response = requests.get(url, headers=headers, params=params)
response = requests.get('https://2.0/?method=track.getTags&api_key=611bb642df86b5ac99ab8ec251e59641&artist=AC/DC&track=Hells+Bells&use...', headers=headers, params=params)
#data = response.json()
print(response)

"""if response.status_code == 200:
    if 'tags' in data:
        tags = [item['name'] for item in data['tags']['tag']]
        print("Tags for 'Imagine' by 'John Lennon'")
        for i, tag in enumerate(tags, 1):
            print(f"{i}. {tag}")
    else:
        print("No tags found.")
else:
    print(f"Request failed with status code: {response.status_code}")"""
