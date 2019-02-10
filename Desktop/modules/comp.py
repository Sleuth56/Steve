#!/usr/bin/env python3

from modules import Speek

def quorry():
  return ['plus', 'added', 'add', 'minus', 'subtracted', 'divide', 'divided', 'multiplied', 'multiply', 'times']


def math(words=''):
  words = words.split("_")
  op = ''
  res = ''
  num1 = ''
  num2 = ''
  for i in range(len(words)):
      word = words[i]
      if word.isdigit() == True:
          if num1 == '':
              num1 = int(word)
          else:
              num2 = int(words[i])
      else:
          op = word
      if str(num1).isdigit() == True:
          if str(num2).isdigit() == True:
              if op == "plus":
                  res = int(num1) + int(num2)
                  num1 = res
                  num2 = ''
              if op == "added":
                  res = int(num1) + int(num2)
                  num1 = res
                  num2 = ''
              if op == "add":
                  res = int(num1) + int(num2)
                  num1 = res
                  num2 = ''
              elif op == "subtracted":
                  res = int(num1) - int(num2)
                  num1 = res
                  num2 = ''
              elif op == "subtract":
                  res = int(num1) - int(num2)
                  num1 = res
                  num2 = ''
              elif op == "minus":
                  res = int(num1) - int(num2)
                  num1 = res
                  num2 = ''
              elif op == "times":
                  res = int(num1) * int(num2)
                  num1 = res
                  num2 = ''
              elif op == "multiply":
                  res = int(num1) * int(num2)
                  num1 = res
                  num2 = ''
              elif op == "multiplied":
                  res = int(num1) * int(num2)
                  num1 = res
                  num2 = ''
              elif op == "multiplied":
                res = int(num1) * int(num2)
                num1 = res
                num2 = ''
              elif op == "divide":
                  res = int(num1) / int(num2)
                  num1 = res
                  num2 = ''
              elif op == "divided":
                  res = int(num1) / int(num2)
                  num1 = res
                  num2 = ''
              else:
                  pass
  if res != '':
      Speek.Speek(res)
      res = ''


def Steve(quorry=''):
  quorry = quorry.replace("too", "2")
  quorry = quorry.replace("to", "2")
  math(quorry)
