#!/usr/bin/env python3

#put imports here
import wikipedia
from modules import Speek


def quorry():
  return ['wikipedia', 'Wikipedia']


def Wikipedia(quorry):
  try:
    wikipedia.set_lang("en")
    return wikipedia.summary(quorry, sentences=2)
  except:
    print('Wikipedia search failed')

#put the code specific to making your code work with Steve
#exp. removing all the text from the string that isn't needed
def Steve(quorry=''):
  quorry = quorry.replace('steve', '')
  try:
    quorry = quorry.split('wikipedia_search')[1]
  except:
    quorry = quorry.split('wikipedia')[1]
  quorry = quorry.replace('_', ' ')
  Speek.Speek(Wikipedia(quorry))
