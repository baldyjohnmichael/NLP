import nltk, re, pprint
from nltk import word_tokenize
from urllib import request

# good graphic explaining the NLP Pipeline
# http://www.nltk.org/images/pipeline1.png
url = "http://www.gutenberg.org/files/2554/2554-0.txt"
response = request.urlopen(url)
raw = response.read().decode('utf8')
# raw is just a really long string as shown by the print statement bellow
print(type(raw))

print(len(raw))

# print the string from index 0 to 74 inclusive
print(raw[:75])

# make a list tokens from the words of the raw string
tokens = word_tokenize(raw)
print(type(tokens))

# convert tokens list into a nltk.Text object
text = nltk.Text(tokens)
print(type(text))

print(text[1024:1062])
print(text.collocations())

# notice how the last print statement has "project gutenberg" as
# a Collocation, this is due to the header and preface of the bookself.
# to fix this we have to slice the 'raw' string so that only the content itself remainsself.

# use raw.find() to find where to start the text
starttext = raw.find("PART I")
print(starttext)
# rfind will find the first instace of it's parameter of a string if the string was reversed
# use raw.rfind() to find where the end of useable text ends
endtext = raw.rfind("End of Project Gutenberg")
print(endtext)

raw = raw[raw.find("PART I"):raw.rfind("End of Project Gutenberg")]
print(raw.find("PART I"))
