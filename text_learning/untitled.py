#!/usr/bin/python

from nltk.stem.snowball import SnowballStemmer
import string
f = open("../text_learning/test_email.txt", "r")
f.seek(0)
### go back to beginning of file (annoying)
all_text = f.read()
### split off metadata
content = all_text.split("X-FileName:")
print(content)
