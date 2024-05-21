# cccat

A copy of the command line tool cat allows reading file content into the terminal.

## Run
Install the neccessary dependencies in a virtual environment:
```bash
python3 -m venv .venv
. .venv/bin/activate
pip install -r requirements.txt
python3 cccat.py [-n|-b] [filenames]
```

## Usage

```bash
cccat test.txt
cccat test.txt test2.txt
head -n1 test.txt | cccat -
# number lines with `-n`
head -n3 test.txt | cccat -n
sed G test.txt | cccat -n | head -n4
# number non-blank lines only with `-b`
sed G test.txt | cccat -b | head -n5
```

## Inspired by

[Build Your Own cat Tool](https://codingchallenges.fyi/challenges/challenge-cat/)


## Fun Fact
The default command parsing behaviour provided by the click package allows options to work independent of positions of arguments. E.g, the below code does mark line numbers.
```bash
python3 cccat.py test.txt -n
```
However, the original cat tool does not follow the same principle.
```bash
cat test.txt -n # cat: -n: No such file or directory
```