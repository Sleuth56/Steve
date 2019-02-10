#!/usr/bin/env python3

#put imports here
import time
from modules import Speek


#use under scores '_' insted of spaces
def quorry():
  return ['what_is_the_time', 'what_time_is_it', 'what_day_is_it', 'what_year_is_it', "what's_the_date", 'whats_the_date', 'what_is_the_date', "what's_the_month", 'what_month_is_it', "what's_the_day", 'what_day_is_a', 'what_time_is_a']


def DateTime(quorry=''):
  if 'day' in quorry:
    Speek.Speek('the ' +str(time.localtime()[2]) + 'th')

  elif 'month' in quorry:
    Speek.Speek(str(time.localtime()[1]))

  elif 'year' in quorry:
    Speek.Speek(str(time.localtime()[0]))

  elif 'date' in quorry:
    Speek.Speek(str(time.localtime()[1]) + ', ' +  str(time.localtime()[2]) + ', ' + str(time.localtime()[0]))

  elif 'time' in quorry:
    hour = time.localtime()[3]
    if hour > 12:
      hour = hour - 12
    Speek.Speek(str(hour) + ':' + str(time.localtime()[4]))


#put the code specific to making your code work with Steve
#exp. removing all the text from the string that isn't needed
def Steve(quorry=''):
  DateTime(quorry)
