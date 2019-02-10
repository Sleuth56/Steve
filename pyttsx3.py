import pyttsx3

def onWord(name, location, length):
    print('word', name, location, length)
    if location > 10:
        engine.stop()

engine = pyttsx3.init()
rate = engine.getProperty('rate')
engine.setProperty('rate', rate - 160)
engine.connect('started-word', onWord)
engine.say('The quick brown fox jumped over the lazy dog.')
engine.runAndWait()
