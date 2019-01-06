#!/usr/bin/env python3

#start and configure paulseaudio
import os
#os.system('pacmd set-default-sink "1"')
os.system('pulseaudio --start')

#Steve module imports
from modules import web
from modules import comp
from modules import Wikipedia
from modules import Timer
from modules import greating
from modules import DateTime
from modules import wordtonum

from modules import Speek
Speek.Speek("Hi I'm Steve")

from pocketsphinx import LiveSpeech
import pyttsx3


#text = input(": ")
speech = LiveSpeech(lm=False, keyphrase='steve', kws_threshold=1e-20)
for phrase in speech:
  words = phrase.segments(detailed=False)
  if 'steve' in words:
    print('active')

    for text in LiveSpeech():
      found = False
      text = wordtonum.wordtonum(str(text))
      text = str(text)
      text = text.replace(' ', '_')
      print(text)

      # if found == False:
      #   for i in range(len(your_module.quorry())):
      #     if your_module.quorry()[i] in text:
      #       your_module.Steve(text)
      #       found = True

      if found == False:
        for i in range(len(DateTime.quorry())):
          if DateTime.quorry()[i] in text:
            DateTime.Steve(text)
            found = True

      if found == False:
        for i in range(len(web.quorry())):
          if web.quorry()[i] in text:
            web.Steve(text)
            found = True

      if found == False:
        for i in range(len(comp.quorry())):
          if comp.quorry()[i] in text:
            comp.Steve(text)
            found = True

      if found == False:
        for i in range(len(Wikipedia.quorry())):
          if Wikipedia.quorry()[i] in text:
            Wikipedia.Steve(text)
            found = True

      if found == False:
        for i in range(len(Timer.quorry())):
          if Timer.quorry()[i] in text:
            Timer.Steve(text)
            found = True

      if found == False:
        for i in range(len(greating.quorry())):
          if greating.quorry()[i] in text:
            greating.Steve(text)
            found = True

      if found == False:
        for i in range(len(Speek.quorry())):
          if Speek.quorry()[i] in text:
            Speek.Steve(text)
            found = True
