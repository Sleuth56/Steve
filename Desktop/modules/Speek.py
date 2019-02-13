#!/usr/bin/env python3

#put imports here
import pyttsx3
import _thread
import time

SpeekOnOff = True

engine = pyttsx3.init()

#use under scores '_' insted of spaces
def quorry():
  return ['stop', 'shutup', 'shut_up']


def onWord(name, location, length):
  pass

def f(text):
  print('started')
  if SpeekOnOff == True:
    rate = engine.getProperty('rate')
    engine.setProperty('rate', rate - 90)
    engine.connect('word', onWord)
    engine.say(text)
    engine.runAndWait()
  else:
    print(text)


def Speek(text):
  _thread.start_new_thread( f, (text,) )


def stop():
  engine.stop()



#put the code specific to making your code work with Steve
#exp. removing all the text from the string that isn't needed
def Steve(quorry=''):
  stop()


if __name__ == '__main__':
  while True:
    text = input(': ')
    if text == 'stop':
      stop()
    else:
      Speek(text)
