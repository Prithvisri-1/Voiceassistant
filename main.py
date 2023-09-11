import pyttsx3
import speech_recognition as sr
from pyttsx3 import *
import datetime
import wikipedia
import webbrowser

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', 'voices[2].id')
engine.setProperty('rate', 190)


api_key = "8ef61edcf1c576d65d836254e11ea420"

speak("Hi I Am Your Jarvis!! Initiating Your Jarvis")
speak("Jarvis Mode ON ")

while True:
    def speak(text):
        engine.say(text)
        engine.runAndWait()


    def tc():
        a = sr.Recognizer()
        with sr.Microphone() as src:
            print("Listening>>")
            ad = a.listen(src)

        try:
            s = a.recognize_google(ad, language='en-in')
            print(f'YOU said : {s}\n')
        except Exception as e:
            speak("Did not hear your voice ,Please Say That Again")
            return "None"
        return s


    def voices(s):
        if "goodbye" in s or 'ok bye' in s or 'bye jarvis' in s:
            speak('Good bye')
            quit()
        elif "hi" in s or 'hey' in s or 'hello' in s:
            speak('Hi Sir')
        elif "what is time now" in s or 'time' in s or 'current time now' in s:
            t = datetime.datetime.now().strftime("%H:%M:%S")
            print(f"Your Current Time is {t}")
        elif 'youtube' in s:
            if 'open youtube' in s:
                webbrowser.open_new_tab("https://www.youtube.com")
                speak('Got the Youtube and Open Now')
                print('Got the Youtube and Open Now')
            else:
                n = s.replace("youtube", "")
                y = "https://www.youtube.com/results?search_query="
                nu = y + n.replace("", "+").rstrip("+")
                webbrowser.open(nu)
                speak(f"Opening youtube with search as {nu}")
                print(f"Opening youtube with search as {nu}")
        elif 'wikipedia' in s:
            s = s.replace("wikipedia", "")
            r = wikipedia.summary(f"{s}, sentences=2")
            speak(r)
            print(f'In The Wikipedia {r}')
        elif "good morning" in s or "good afternoon" in s or "good evening" in s:
            def wish(name):
                h = datetime.datetime.now().hour
                if h >= 0 and h < 12:
                    speak(f"Good Morning{name}")

                elif h >= 12 and h < 18:
                    speak(f"Good Afternoon{name}")

                else:
                    speak(f"Good Evening{name}")

            a = wish("sir")
            print(a)
        elif 'open google' in s:
            webbrowser.open_new_tab('https://www.google.com')
            speak( 'Got The Google Search Engine and Open Now')
        elif 'open gmail' in s:
            webbrowser.open_new_tab('gmail.com')
            speak("Got The Gmail Page and Show Them")
        elif "news" in s or "today news" in s or "today headlines" in s:
            webbrowser.open_new_tab("https://timesofindia.indiatimes.com/home/headlines")
            speak("Got The Today Headlines and Show Them")
        elif "thank you" in s:
            speak("your welcome sir")
        else:
            speak("Sorry I didn't get that \n I'm Still Learning New Stuff")


    speak("Listening")
    us = tc().lower()
    ai = voices(us)
