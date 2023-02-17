import config
import requests

def lastfm_get(payload):
    # define headers and URL
    headers = {'user-agent': config.USER_AGENT}
    url = '/2.0/?method=track.getTags&api_key=YOUR_API_KEY&artist=AC/DC&track=Hells+Bells&use...'

    # Add API key and format to the payload
    payload['api_key'] = config.API_KEY
    payload['format'] = 'json'

    response = requests.get(url, headers=headers, params=payload)
    return response

r = lastfm_get({
    'method': 'track.getTags'
})


import json

def jprint(obj):
    # create a formatted string of the Python JSON object
    text = json.dumps(obj, sort_keys=True, indent=4)
    print(text)

jprint(r.json())