# NLP Experiments

A repo tracking experiments in Natural Language Processing.

## About the software

This project uses Python 3 and NLTK .

## Programs in Repo

### Passive Voice Checker
 _Checks for the passive voice in English sentences._
 Takes an English sentence as a string and returns True if the sentence uses the passive voice and False if not.

 ***Current Problems being fixed***
 * If an irregular adverb is used between the conjugated form of _to be_ and the past participle of the main verb, then the program does not recognize the passive voice.
 * Does not recognize irregular past participles

#### About the Formation of English Passive Voice (EPV)
EPV = form of verb _to be_  + past participle of the main verb denoting the action.

Sometimes the verb _to be_ can be replaced by the verb _get_ like

_get_ + past tense form of word  

conjugation of the verb _be_ found [here](https://en.wiktionary.org/wiki/be#Conjugation)

Past Participles is identical to the past tense form of the verb.

Past tense form of verb is typically formed by (ending in _-ed_), however there are
irregular verbs. [list found here](https://www.wikiwand.com/en/List_of_English_irregular_verbs)
