#!/usr/bin/env python3

# Must have librarries
import time
import os
# steve specific external imports
from pocketsphinx import LiveSpeech
import pyttsx3
import _thread
# steve modules
from modules import Speek
from modules import web
from modules import comp
from modules import Wikipedia
from modules import Timer
from modules import greating
from modules import DateTime
from modules import wordtonum

# Veriables
IsFound = False

Speek.Speek("Hi I'm Steve")

# defining the keyphrase to trigger steve
speech = LiveSpeech(lm=False, keyphrase='steve', kws_threshold=1e-20)

# an infinate loop that checks every word to see if it matches the keyphrase
for phrase in speech:
  words = phrase.segments(detailed=False)
  if 'steve' in words:
    print('active')
    
    # starts a realtime speech to text seshion
    for text in LiveSpeech():
      if IsFound == False:
        print(str(text))
        IsFound = True
        
      else:
        IsFound = False
        break
