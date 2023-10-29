# obsidian

parser search for quotes inside the **quotes** folder.

A quote should be inside a \<blockquote\> tag 
> This is an example blockquote

text outside the blockquote will be ignored by the parser

### convert md to json
everytime you push a commit into main branch, a workflow runner will be triggered. See the implementation in `.github/workflows/mdtojson.yml`
