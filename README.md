# text_score
Find the smallest substring with highest text score

# Description
Given three strings, text, prefixString, and suffixString, find:

● prefixScore: the longest substring of text matching the end of prefixString
● suffixScore: the longest substring of text matching the beginning of suffixString.
Sum the lengths of the two strings to get the textScore. The substring of text that begins with
the matching prefix and ends with a matching suffix, and has the highest textScore, is the
correct value to return. If there are other substrings with equal textScore, return the
lexicographically lowest substring.

## What to install?
Install python3.9:
If you have Mac: `brew install python@3.9`

Note: it should work for python >= 3.7, but not tested.

## How to run tests
### Run for the first time
```
mkdir Envs
python3 -m venv ~/Envs/text_score
source ~/Envs/text_score/bin/activate
pip install -U pip
pip install -r test_requirements.txt
```

### Run every time
`source ~/Envs/text_score/bin/activate`  // once per terminal tab

`python -m pytest`

## How to run the program
`python3 main.py`


### Run Example
```
❯ python3 main.py
Please enter strings:
text: fdagag
PrefixString: ga
SuffixString: ag
The substring of text with the highest textScore is: gag
```
