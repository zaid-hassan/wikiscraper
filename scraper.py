import requests
from flask import Flask
from bs4 import BeautifulSoup

def get_response(search):
    try:
        site_url = f'https://en.wikipedia.org/wiki/{search}'
        response = requests.get(site_url)
        return response.content
    except requests.RequestException as e:
        print(f'error {e}')
        return None

def parse_html(html_content):
    soup = BeautifulSoup(html_content, 'html.parser')
    required_html = soup.find(id='mw-content-text')
    if required_html:
        return required_html
    else:
        print('Error: Required html not found')
        return None

def populate_html(html):
    my_html = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Document</title>
</head>
<body>
  {html}
</body>
</html>"""
    return my_html

app = Flask(__name__)

@app.route('/')

def scrape_wiki():
    # wiki_search = input('Enter a keyword to search wiki: ')
    wiki_response = get_response('linux')
    search_html = parse_html(wiki_response)
    final_html = populate_html(search_html)
    return final_html

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)