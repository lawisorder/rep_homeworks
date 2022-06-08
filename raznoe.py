import pyttsx3


engine = pyttsx3.init()

engine.setProperty('rate', 150)
engine.setProperty('volume', 3)
engine.setProperty('voice', 'ru')
voices = engine.getProperty('voices')


for voice in voices:
    if voice.name == 'Mikhail':
        engine.setProperty('voice', voice.id)

engine.say('''
матвей не сиди на полу
''')
engine.runAndWait()