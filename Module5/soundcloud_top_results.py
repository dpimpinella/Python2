import urllib.request
import urllib.parse
import json
from bs4 import BeautifulSoup

def scrape_top_results(html):
    """Scrapes the top results from a given SoundCloud search.
    Args:
        html: HTML from urllib request/response
    Returns:
        top_results: dictionary of song titles and links for the results that were scraped
    """
    results = []
    soup = BeautifulSoup(html, 'html.parser')
    res = soup.ul.find_next_sibling("ul")
    for item in res:
        result = {}
        if (item == '\n'):
            continue
        result["song_title"] = item.a.contents
        result["link"] = 'https://soundcloud.com' + item.a["href"]
        results.append(result)
    top_results = {"top_results": results}
    return top_results

def write_results(top_results_dict):
    """
    Writes top results of search to JSON file.
    Args:
        top_results_dict: dictionary of top results, created by 
        scrape_top_results()
    """
    with open("search_results.json", 'w+') as outfile:
        json.dump(top_results_dict,outfile, indent=4)
        outfile.flush()
        outfile.close()

def get_query():
    """
    Gets search term from user.
    """
    query = input('What would you like to search for?')
    query = urllib.parse.quote(query)
    return query

url = 'https://soundcloud.com/search?q=' + get_query()
req = urllib.request.Request(url)
with urllib.request.urlopen(req) as response:
    html = response.read()
write_results(scrape_top_results(html))
