#!/usr/bin/env python3

#put imports here
import random
from modules import Speek


#use under sh=cores '_' insted of spaces
def quorry():
  return ['hi', 'hello', 'whats_up', "what's_up", 'how_are_you']


def greating(quorry=''):
  if 'how_are_you' in quorry:
    how_are_you_doing_responce = ['Good, you', 'Good', 'Just fine, thanks', 'Fine']
    Speek.Speek(int(how_are_you_doing_responce[random.randint(0, 3)]))
  else:
    responce = ['Hi', 'Hello']
    Speek.Speek(responce[random.randint(0, 1)])


#put the code specific to making your code work with Steve
#exp. removing all the text from the string that isn't needed
def Steve(quorry=''):
  greating(quorry)
