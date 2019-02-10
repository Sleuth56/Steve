#!/usr/bin/env python3

#put imports here
import pyttsx3
import _thread
import time

SpeekOnOff = True
IfStopping = False

#use under scores '_' insted of spaces
def quorry():
  return ['stop', 'shutup', 'shut_up']


def onWord(name, location, length):
  engine.stop()
  # if IfStopping == True:
  #   engine.stop()
  #   IfStopping = False


def f(text):
  if SpeekOnOff == True:
    engine = pyttsx3.init()
    rate = engine.getProperty('rate')
    engine.setProperty('rate', rate - 160)
    engine.connect('started-word', onWord)
    engine.say(text)
    engine.runAndWait()
  else:
    print(text)


def Speek(text):
  _thread.start_new_thread( f, (text,) )


def stop():
  IfStopping = True



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
