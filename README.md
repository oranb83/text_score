# text_score
Find the smallest substring with highest text score

## What to install?
Install python3.9:
If you have Mac: `brew install python@3.9`
Note: it should work for python >= 3.7, but not tested.

## How to run tests
### Run for the first time
`mkdir Envs`
`python3 -m venv ~/Envs/text_score`
`source ~/Envs/text_score/bin/activate`
`pip install -U pip`
`pip install -r test_requirements.txt`

### Run every time
`source ~/Envs/text_score/bin/activate`  # once per terminal
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
