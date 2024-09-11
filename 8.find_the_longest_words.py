#Write a python program to find the longest words.

import re

l1="abc abcd abcde abcdef"
word=r'\w+'
sub=re.findall(word,l1)
max_word=max(sub,key=len)
print(max_word)
