# cccat

A copy of the command line tool cat allows reading file content into the terminal.

# Usage

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

# Inspired by

[Build Your Own cat Tool](https://codingchallenges.fyi/challenges/challenge-cat/)
