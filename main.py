#import tkinter as tk
import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes
import os

#root = tk.Tk()
#apps = []

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')

#frame = tk.Frame(root,bg='white')
#frame.place(relwidth=8, relheight=8,relx=0.1, rely=0.1)

#canvas = tk.Canvas(root, height = 700, width = 700, bg ='#263D42' )
#canvas.pack()

def talk(text):
    engine.say(text)
    engine.runAndWait()


def take_command():
        try:
            with sr.Microphone() as source:
                #print('Listening...')
                # talk ('hello Samuel')
                voice = listener.listen(source)
                command = listener.recognize_google(voice)
                command = command.lower()
                if 'ben' in command:
                    command = command.replace('ben', '')
                    print(command)
        except:
            pass


def playsong(song):
    dir_path = os.path.dirname(os.path.realpath(__file__))

    for root, dirs, files in os.walk(dir_path):
        for file in files:
            if file.endswith('.mp3'):
                files.append(file)
                if file  is song:
                        os.startfile(file)
def run_alexa():
    command = take_command()
    print(command)
    if 'play' in command:
        song = command.replace('play', '')
        talk('playing' + song)
        playsong(song)
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        talk('oh oh oh  Samuel, the time is ' + time)
    elif 'who is' in command:
        person = command.replace('who is', '')
        info = wikipedia.summary(person, 3)
        talk(info)
    elif 'what is' in command:
        thing = command.replace('what is', '')
        tinfo = wikipedia.summary(thing,3)
        talk(tinfo)
    elif ' i love' in command:
        talk("i am sorry, but i don't feel the same way because i am gay")

    elif 'joke' in command:
        talk(pyjokes.get_joke())
    else:
        talk('I did not quite get that, my love, could you perharps  speak more equivocally')

talk('DO YOU WANT A LOCAL ASSISTANT OR AN ONLINE ASSISTANT MAN')

if True:
    run_alexa()
else:
    exit()

def run_barry():
    command = take_command()
    print(command)
    if 'play' in command:
        song = command.replace('play', '')
        talk('playing' + song)
        pywhatkit.playonyt(song)
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        talk('oh oh oh  Samuel, the time is ' + time)
    elif 'who is' in command:
        person = command.replace('who is', '')
        info = wikipedia.summary(person, 3)
        talk(info)
    elif 'what is' in command:
        thing = command.replace('what is', '')
        tinfo = wikipedia.summary(thing,3)
        talk(tinfo)
    elif ' i love' in command:
        talk("i am sorry, but i don't feel the same way because i am gay")

    elif 'joke' in command:
        talk(pyjokes.get_joke())
    else:
        talk('I did not quite get that, my love, could you perharps  speak more equivocally')

if True:
    run_alexa()
else:
    exit()
talk('DO YOU WANT A LOCAL ASSISTANT OR AN ONLINE ASSISTANT')

openQ = input('DO YOU WANT A LOCAL ASSISTANT OR AN ONLINE ASSISTANT: ')

openQ = openQ.lower()

if 'local' in openQ:
    run_alexa()

else:
    run_barry()


#root.mainloop()
