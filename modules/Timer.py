#!/usr/bin/env python3

import threading
import time
from modules import wordtonum
import os
from modules import Speek


def quorry():
  return ['start_a_timer', 'set_a_timer', 'set_the_timer', 'start_the_timer']


def f(sleep):
    global done
    done = False
    sleeping = sleep
    while sleeping != 0:
      time.sleep(1)
      sleeping = sleeping - 1
    os.system('play Librem-5-power-on-3-by-Dinesh-Manajipet.ogg')


def Timer(quorry=''):
  timer = 0
  words = quorry.split('_')
  for i in range(len(words)):
      if words[i] == 'second':
          timer = timer + int(words[i-1])

      if words[i] == 'seconds':
          timer = timer + int(words[i-1])

      if words[i] == 'minute':
          timer = 60 * int(words[i-1]) + timer

      if words[i] == 'minutes':
          timer = 60 * int(words[i-1]) + timer

      if words[i] == 'hour':
          timer = 36000 * int(words[i-1]) + timer

      if words[i] == 'hours':
          timer = 36000 * int(words[i-1]) + timer

  t = threading.Thread(target=f, args=(timer,))
  t.start()


def Steve(quorry=''):
  quorry = wordtonum.wordtonum(quorry)
  Timer(quorry)
