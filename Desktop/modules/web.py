#!/usr/bin/env python3

import webbrowser

def quorry():
  return ['search_the_web', 'search_for', 'search_on_the_web']

def search(quorry = '', category = 'web'):
  quorry = quorry.replace('!', '')
  webbrowser.open('https://duckduckgo.com/?q=' + quorry.replace(' ', '+') + '&atb=v135-1__&ia=' + category, new=2)
  print('https://duckduckgo.com/?q=' + quorry.replace(' ', '+') + '&atb=v135-1__&ia=' + category)

def site(url = ''):
  webbrowser.open(url, new=2)

def Steve(Quorry=''):
  Quorry = Quorry.replace('steve', '')
  for i in range(len(quorry())):
    Quorry = Quorry.replace(quorry()[i], '')
  Quorry = Quorry.replace('_', ' ')
  Quorry = Quorry.replace('for', '')
  Quorry = Quorry.replace('web', '')
  search(Quorry)
