import os 
import glob
import json
import markdown

quote_files = glob.glob("quotes/**")

for quote_file in quote_files:
    print(quote_file)
    f = open(quote_file, 'r')
    print(markdown.markdown(f.read()))

def write_json_data():
    print("writing json data...")
    with open("db.json", "w") as json_file:
        json.dump(
            {
                "quotes": [
                    {
                        "text": "first trial"
                    }
                ]
            },
            json_file,
            indent=4
        )

write_json_data()