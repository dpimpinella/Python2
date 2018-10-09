import json
import urllib.parse
import urllib.request

from bs4 import BeautifulSoup

def scrape_top_results():
    """Scrapes the top results from a given SoundCloud search.
    Returns:
        top_results: dictionary of song titles and links for the results that were scraped
    """       
    query = input('Which SoundCloud artist\'s top hits would you like to export? >> ').lower()
    encoded_query = urllib.parse.quote(query)
    url = 'https://soundcloud.com/search?q=' + encoded_query
    req = urllib.request.Request(url)
    with urllib.request.urlopen(req) as response:
        html = response.read()
    soup = BeautifulSoup(html, 'html.parser')
    res = soup.ul.find_next_sibling("ul")
    
    results = []
    for item in res:
        result = {}
        if (item == '\n'):
            continue
        content = item.a.contents[0]
        if (content.lower() == query):
            continue
        result["song_title"] = content
        result["link"] = 'https://soundcloud.com' + item.a["href"]
        results.append(result)

    top_results = {query: results}
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

def main():
    write_results(scrape_top_results())

main()