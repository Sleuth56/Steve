#!/usr/bin/env python3

#put imports here
from pixel_ring import pixel_ring
from gpiozero import LED
import random
import time


#use under scores '_' insted of spaces
def quorry():
  return ['start_a_light_show']


def startup():
  power = LED(5)
  green = 28
  red = 51
  while True:
    pixel_ring.set_color(r=red, g=green, b=0)
    red = red - 1
    green = green + 1
    time.sleep(0.2)
    if green >= 50:
      break


def light_show():
  pass


def setcolor(red=50, green=50, blue=0):
  power = LED(5)
  power.on()
  pixel_ring.set_color(r=red, g=green, b=blue)
  while True:
    pass


#put the code specific to making your code work with Steve
#exp. removing all the text from the string that isn't needed
def Steve(quorry=''):
  light_show()


if __name__ == '__main__':
  startup()
  setcolor(30, 30, 0)
