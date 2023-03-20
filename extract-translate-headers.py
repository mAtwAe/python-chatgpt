

import requests
from bs4 import BeautifulSoup
import googletrans

url = 'https://www.techworld-with-nana.com/post/a-guide-of-how-to-get-started-in-it-in-2023-top-it-career-paths'

# get the html from the website
page = requests.get(url)

# parse the html
soup = BeautifulSoup(page.content, 'html.parser')

# extract all the html headers
headers = soup.find_all(['h1', 'h2', 'h3', 'h4', 'h5', 'h6'])

# translate the headers to spanish
translator = googletrans.Translator()
spanish_headers = []
for header in headers:
    translated_header = {
        "text": translator.translate(header.text, dest='es').text,
        "name": header.name
    }
    spanish_headers.append(translated_header)

# create an html file with the translated headers
with open('spanish_headers.html', 'w', encoding="utf-8") as f:
    f.write('<html><head><title>Translated Headers</title></head><body>\n')
    for header in spanish_headers:
        f.write(f'<{header["name"]}>{header["text"]}</{header["name"]}>\n')
    f.write('</body></html>\n')