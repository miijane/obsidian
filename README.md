# obsidian

parser search for quotes inside the **quotes** folder.

A quote should be inside a \<blockquote\> tag 
> This is an example blockquote

text outside the blockquote will be ignored by the parser

### convert md to json
the converting is done by the python script `mdtojson.py`

everytime you push a commit into main branch, a workflow runner that runs the script will be triggered. See the implementation in `.github/workflows/mdtojson.yml` file

The server will take up to 30s before the changes to [db.json](https://raw.githubusercontent.com/miijane/obsidian/main/db.json) is reflected in your repo.
