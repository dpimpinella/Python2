import json
import urllib.parse
import urllib.request

from bs4 import BeautifulSoup

# Web scraper using BeautifulSoup that grabs the top 10 results from a given SoundCloud search.

def scrape_top_results():
    """Scrapes the top results from a given SoundCloud search.
    Returns:
        top_results: dictionary of song titles and links for the results that
            were scraped
    """       
    
    # Get user input, create a url to open with urllib. 
    # urllib.parse.quote replaces special characters to avoid errors in the query URL.
    # Example:
    # urllib.parse.quote('/El Niño/') yields '/El%20Ni%C3%B1o/'
    query = input('Which SoundCloud artist\'s top hits would you like to export? >> ').lower()
    encoded_query = urllib.parse.quote(query)
    url = 'https://soundcloud.com/search?q=' + encoded_query
    
    
    # Open the URL that was just created to grab the HTML, and then make soup!
    req = urllib.request.Request(url)
    with urllib.request.urlopen(req) as response:
        html = response.read()
    soup = BeautifulSoup(html, 'html.parser')
    
    # Use 'ul' HTML tags to get to the HTML of search results.
    res = soup.ul.find_next_sibling("ul")
    
    # Use for loop to get song titles and links to the songs. 'item' is just 
    # an item in a list (which we called 'res', as above). 
    results = []
    for item in res:
        result = {}

        # Ignore line breaks ('/n')
        if (item == '\n'):
            continue
        # Get song title from 'item' using BeautifulSoup.
        song_title = item.a.contents[0]
        
        # This if block throws away results if the contents are the same as input
        #  from the user.
        # If the contents are the same as the search, then the content is NOT a
        #  song title, it is the artists name, so we skip it with continue.
        if (song_title.lower() == query):
            continue
        
        # Create a dictionary with 'song title' and 'link' keys
        result["song_title"] = song_title
        result["link"] = 'https://soundcloud.com' + item.a["href"]
        results.append(result)

    # Create and return dictionary of results (which are song titles and links)
    top_results = {query: results}
    return top_results

def write_results(top_results_dict):
    """
    Writes top results of search to JSON file.
    Args:
        top_results_dict: dictionary of top results, created by 
        scrape_top_results()
    """

    # Open/create a file to write to write the top 10 results for the user's 
    # search. 
    with open("search_results.json", 'w+') as outfile:
        json.dump(top_results_dict,outfile, indent=4)
        outfile.flush()
        outfile.close()

# Run the program!
def main():
    write_results(scrape_top_results())

main()