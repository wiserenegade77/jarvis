import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import smtplib
import requests,bs4,sys

engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
#print(voices[2].id)
engine.setProperty('voices',voices[1].id)

def take():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("listening")
        r.pause_threshold = 1
        audio=r.listen(source)

    try:
        print("recognizing...")
        query=r.recognize_google(audio, language='en-in')
        print(f"user said: {query}\n")
    except Exception as e:
        print("say that again ")
        return "None"
    return query

def speak(audio):
    engine.say(audio)
    engine.runAndWait()
def wishme():
    hour=int(datetime.datetime.now().hour)
    minutes=int(datetime.datetime.now().minute)
    if hour>=0.00 and hour<12.00:
        speak("Good Morning sir")
    elif hour>=12.00 and hour<18.00:
        speak("Good evening sir")
    else:
        speak("Good Afternoon sir")
    #speak("its {} o {} sir".format(hour,minutes))

def sendemail(to,content):
    server=smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login('wiserenegade77@gmail.com','arsh0224')
    server.sendmail('wiserenegade77@gmail.com',to,content)
    server.close()

def search(audio):
    try:
        from googlesearch import search
    except ImportError:
        print("no module found")
    for j in search(audio,tld="co.in",num=10,stop=10,pause=2):
        print(j)
        

#speak("hello Mr Mago i am jarvis")
wishme()
query=""
while query!="shutdown":
    query=take().lower()
    if 'wikipedia' in query:
        query=query.replace("wikipedia","")
        result = wikipedia.search(query, results = 5)
        print(result)
        speak(result)
        query=take().lower()
        results=wikipedia.summary(query,sentences=5)
        speak("accoring to wikipedia")
        speak(results)
        #page_object=wikipedia.page(results)
        #print(page_object.original_title)

    elif 'open youtube' in query:
        webbrowser.open("youtube.com")
    elif 'open google' in query:
        webbrowser.open("google.com")
    elif 'music' in query:
        music_dir='D:\\songs'
        songs=os.listdir(music_dir)
        print(songs)
        os.startfile(os.path.join(music_dir, songs[5]))
    elif 'open code' in query:
        codepath="F:\\vs code\\Microsoft VS Code\\Code.exe"
        os.startfile(codepath)
    elif 'time' in query:
        strtime=datetime.datetime.now().strftime("%H:%M:%S")
        speak(f"sir the time is {strtime}")
    elif 'email' in query:
        try:
            speak("sir enter your content")
            content=take()
            to="raghavmago2@gmail.com"
            sendemail(to,content)
            speak("sir, email sent")
        except Exception as e:
            speak("sir email not sent")
    elif 'search' in query:
        query=take().lower()        
        search(query)
