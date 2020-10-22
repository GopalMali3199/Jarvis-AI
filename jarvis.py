import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import random
import smtplib
import sys

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)



def speak(audio):
    print('Jarvis: ' + audio)
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour =int(datetime.datetime.now().hour)

    if hour >=0 and hour <12:
        speak("Good Morning !")

    elif hour >=12 and hour < 18:
        speak("Good Afternoon!")

    else:
        speak("Good Evening!")

wishMe()

speak('Hello Sir, I am your digital assistant Jarvis!')
speak('How may I help you?')

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening.....")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing.....")
        query = r.recognize_google(audio,language='en-in')
        print(f"user said: {query}\n")

    except sr.UnknownValueError:
        speak('Sorry sir! I didn\'t get that! Try typing the command!')
        query = str(input('Command: '))
    return query

if __name__ == "__main__":
    while True:
        query = takeCommand().lower()

        if 'wikipedia' in query:
            speak('okay')
            speak("Serching wikipedia....")
            query = query.replace("wikipedia","")
            results = wikipedia.summary(query,sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            speak('okay')
            webbrowser.open("www.youtube.com")

        elif 'open google' in query:
            speak('okay')
            webbrowser.open("www.google.com")
        
        elif 'play music' in query:
            music_dir = "C:\\Users\\Gopal Mali\\Music\\New folder"
            songs = os.listdir(music_dir)
            os.startfile(os.path.join(music_dir,random.choice(songs)))
            speak('Okay, here is your music! Enjoy!')


        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"sir,the time is {strTime}")

        elif 'open code' in query:
            speak('okay')
            codePath = "C:\\Users\\Gopal Mali\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)

        elif 'hi' in query:
            speak("Hello sir..")

        elif "what\'s up" in query or 'how are you' in query:
            stMsgs = ['Just doing my thing!', 'I am fine!', 'Nice!', 'I am nice and full of energy']
            speak(random.choice(stMsgs))

        elif 'marathi movie' in query:
            speak('okay')
            dDrivePath="D:\\Gopal\\Movie"
            os.startfile(dDrivePath)

        elif ' hollywood movie' in query:
            speak('okay')
            eDrivePath="E:\\"
            os.startfile(eDrivePath)

        elif ' bollywood movie' in query:
            speak('okay')
            gDrivePath="G:\\"
            os.startfile(gDrivePath)

        elif 'bye' in query:
            speak('Bye Sir')
            sys.exit()

        speak('Next Command! Sir!')
       