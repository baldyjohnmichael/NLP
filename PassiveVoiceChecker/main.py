import nltk, re, pprint
from nltk import word_tokenize


# Can recognize the passive voice for
# normal PPoVs and as long as there is no adv
# seperating conjugationsOfToBe and PPoV

def main():
    sentence = "the car was turned on"
    ps = "I turned the car on"
    advPassive = "the car was quickly turned on"
    advActive = "I quickly turned the car on"

    print(sentence)
    print(hasPassive(prepText(sentence)))
    print(ps)
    print(hasPassive(prepText(ps)))
    print(advPassive)
    print(hasPassive(prepText(advPassive)))
    print(advActive)
    print(hasPassive(prepText(advActive)))


def prepText(sentence):
    tokenized = word_tokenize(sentence)
    text = nltk.Text(tokenized)
    return text

# PPoV = Past Participle of verb
# returns only whether or not a sentence has
# the passive voice, it does not show where it is.
def hasPassive(text):
    i = 0
    while i < len(text):
        if isConjOfToBE(text[i]):
            print("to be found: " + text[i])
            if isPPoV(text[i+1]):
                print("PPoV found: " + text[i+1])
                return True
            elif isADV(text[i+1]) and isPPoV(text[i+2]):
                print("ADV found: " + text[i+1])
                return True
        i = i + 1
    return False

conjugationsOfToBe = re.compile(r"\b(am|are|is|was|were|be|being)\b")
def isConjOfToBE(word):
    if re.fullmatch(conjugationsOfToBe, word):
        return True
    return False

regularPast = re.compile(r"[a-z]+(ed)\b")
def isPPoV(word):
    if re.fullmatch(regularPast, word):
        return True
    return False

regularADV = re.compile(r"[a-z]+(ly)\b")
def isADV(word):
    if re.fullmatch(regularADV, word):
        return True
    return False
main()
