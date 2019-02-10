#!/usr/bin/env python3

#put imports here
import pyttsx3
import _thread	

SpeekOnOff = True
engine = pyttsx3.init()

#use under scores '_' insted of spaces
def quorry():
  return ['stop', 'shutup', 'shut_up']


def f(text):
  if SpeekOnOff == True:
    rate = engine.getProperty('rate')
    engine.setProperty('rate', rate-50)
    engine.say(text)
    engine.runAndWait()
  else:
    print(text)

def Speek(text):
  _thread.start_new_thread( f, (text,) )


def stop():
  pyttsx3.engine.Engine.stop(engine)
  #pyttsx3.driver.DriverProxy.setBusy(engine, busy=False)



#put the code specific to making your code work with Steve
#exp. removing all the text from the string that isn't needed
def Steve(quorry=''):
  stop()

if __name__ == '__main__':
  while True:
    Speek(input(': '))
