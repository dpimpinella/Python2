import requests
import json
import base64
import urllib

class OAuthToken:
    """Contains API key information used for authentication when sending 
    Twitter API requests.
    """
    API_OAUTH_ENDPOINT = 'https://api.twitter.com/oauth2/token'
    API_CONSUMER_KEY = 'key goes here'
    API_SECRET_KEY = 'key goes here'

    def __init__(self):
        self.bearer_token = self.request_bearer_token()

    def request_bearer_token(self):
        key_secret = '{}:{}'.format(
            OAuthToken.API_CONSUMER_KEY,
            OAuthToken.API_SECRET_KEY).encode('ascii')
        b64_encoded_key = base64.b64encode(key_secret)
        b64_encoded_key = b64_encoded_key.decode('ascii')

        headers = {
            'User-Agent':'TemperatureOfTheRoom',
            'Authorization':'Basic ' + b64_encoded_key,
            'Content-Type':'application/x-www-form-urlencoded;charset=UTF-8',
            'Accept-Encoding':'gzip'} 
        body = {'grant_type':'client_credentials'}
        request = requests.post(
            OAuthToken.API_OAUTH_ENDPOINT,
            data = body,
            headers = headers)

        bearer_token = request.json()['access_token']
        return bearer_token

class TwitterSearch:
    """Encodes query to Twitter Search API and stores results.
    """
    API_SEARCH_ENDPOINT = 'https://api.twitter.com/1.1/search/tweets.json?q='

    def __init__(self, query):
        self.query = query
        self.results = self.sendSearch()
        self.tweet_text = self.findText()

    def sendSearch(self):
        encoded_query = urllib.parse.quote(self.query.encode('utf-8'))
        url = self.API_SEARCH_ENDPOINT + encoded_query
        headers = {
            'User-Agent':'TemperatureOfTheRoom',
            'Authorization':'Bearer ' + OAuthToken().bearer_token,
            'Content-Type':'application/x-www-form-urlencoded;charset=UTF-8'}
        response = requests.get(url, headers = headers)
        results = json.loads(response.content)
        return results
    
    def findText(self):
        tweet_text = []
        for item in self.results["statuses"]:
            tweet_text.append(item["text"])
        return tweet_text

search = TwitterSearch("roses-filter:retweets-filter:replies")

for item in search.tweet_text:
    print(item)


