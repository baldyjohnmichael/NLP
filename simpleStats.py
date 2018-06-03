from nltk.book import *

# Returns the Lexical Diversity of a given text.
def lexical_diversity(text):
    return len(set(text)) / len(text)

# Retrurns the precentage of a word count in a text
# params:
#   wordFrequency - how often a word appears in a text3
#   totalWords - total number of words in text
def precentage(wordFrequency, totalWords):
    return 100 * wordCount / totalWords

# GOALS,
# Find the lexical diversity of the The Book of Genesis (text3)
# Compare the number of times the words "mother" and "father" are used.
def main():
    text_name = "The Book of Genesis"
    lex_div = lexical_diversity(text3)
    text_len = len(text3)
    mother_count = text3.count("mother")
    mother_prec = precentage(mother_count, text_len)
    father_count = text3.count("father")
    father_prec = precentage(father_count, text_len)

    # print("The Lexical Diversity of The Book of Genesis is: {0}. \n The word mother appears {1} times, which is {2}%. \n ".format(lex_div, mother_count, mother_prec))
    print("The {0} has {1} words with a lexiical diversity of {2}.".format(text_name, text_len, lex_div))

    print("The word {0} appears {1} times, or {2}%, in {3}. ".format('mother',mother_count, mother_prec, text_name))
    print("The word {0} appears {1} times, or {2}%, in {3}. ".format('father',father_count, father_prec, text_name))

main()
