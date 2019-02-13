#!/usr/bin/env python3

#Steve module imports
from modules import Speek
from modules import web
from modules import comp
from modules import Wikipedia
from modules import Timer
from modules import greating
from modules import DateTime
from modules import wordtonum

# Must have librarries
import time
import os

# other inports
from pocketsphinx import LiveSpeech
import pyttsx3
import _thread
import time

Speek.Speek("Hi I'm Steve")

for words in LiveSpeech():
  words = wordtonum.wordtonum(str(words))
  words = str(words)
  words = words.replace(' ', '_')
  if 'steve' in words:
    print('active')
    print(words)
    found = False
    # if found == False:
    #   for i in range(len(your_module.quorry())):
    #     if your_module.quorry()[i] in words:
    #       found = True
    #       your_module.Steve(words)

    if found == False:
      for i in range(len(DateTime.quorry())):
        if DateTime.quorry()[i] in words:
          found = True
          DateTime.Steve(words)

    if found == False:
      for i in range(len(web.quorry())):
        if web.quorry()[i] in words:
          found = True
          web.Steve(words)

    if found == False:
      for i in range(len(comp.quorry())):
        if comp.quorry()[i] in words:
          found = True
          comp.Steve(words)

    if found == False:
      for i in range(len(Wikipedia.quorry())):
        if Wikipedia.quorry()[i] in words:
          found = True
          Wikipedia.Steve(words)

    if found == False:
      for i in range(len(Timer.quorry())):
        if Timer.quorry()[i] in words:
          found = True
          Timer.Steve(words)

    if found == False:
      for i in range(len(greating.quorry())):
        if greating.quorry()[i] in words:
          found = True
          greating.Steve(words)

    if found == False:
      for i in range(len(Speek.quorry())):
        if Speek.quorry()[i] in words:
          found = True
          Speek.Steve(words)
