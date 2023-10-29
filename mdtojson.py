import os 
import glob
import json
import markdown
from bs4 import BeautifulSoup

quote_files = glob.glob("quotes/**")
quote_list = []

for quote_file in quote_files:
    f = open(quote_file, 'r')
    html = markdown.markdown(f.read())
    soup = BeautifulSoup(html, 'html.parser')
    quote = soup.find('blockquote')

    if quote: 
        quote_list.append(
            {
                'quote': quote.get_text(strip=True)
            }
        )
    
def write_json_data(quote_list):
    with open("db.json", "w") as json_file:
        # json_content = json.dumps(quote_list, indent=4)
        # print(json_content)
        json.dump(
            quote_list,
            json_file,
            indent=4
        )

write_json_data(quote_list)