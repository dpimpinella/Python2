import urllib.parse

API_SEARCH_ENDPOINT = 'https://api.twitter.com/1.1/search/tweets.json?q='

query = "MOARRRR COWBELL"
encoded_query = urllib.parse.quote(query.encode('utf-8'))


url = API_SEARCH_ENDPOINT + encoded_query
print(url)
