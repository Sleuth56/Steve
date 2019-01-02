#!/usr/bin/env python3

#put imports here
import pyowm
import Speek

#use under sh=cores '_' insted of spaces
def quorry():
  return ["what's_the_weather", "what's_the_temperature", 'what_is_the_temperature', 'what_is_the_weather']


def get_temp(quorry=''):
  owm = pyowm.OWM('db7e156195898ac6c0b362a73e95ab93')
  observation = owm.weather_at_place('26330,US')
  w = observation.get_weather()
  words = quorry.split('_')
  for i in range(len(words)):
    if words[i] == 'fahrenheit':
      Speek.Speek("It's " + str(w.get_temperature('fahrenheit')['temp']).split('.')[0] + " degrees fahrenheit")
      break
    if words[i] == 'celsius':
      Speek.Speek("It's " + str(w.get_temperature('celsius')['temp']).split('.')[0] + " degrees celsius")
      break


def Steve(quorry=''):
  words = quorry.split('_')
  for i in range(len(words)):
    if words[i] == 'temperature':
      get_temp(quorry)



if __name__ == '__main__':
  while True:
    Steve(input(": "))

# print(w.get_wind())                  # {'speed': 4.6, 'deg': 330}
# print(w.get_humidity())              # 87
# print(w.get_temperature('fahrenheit'))  # {'temp_max': 10.5, 'temp': 9.7, 'temp_min': 9.0}
