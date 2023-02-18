"""
Project Name : AI Desktop Assistant.
Author : Shaily Kesharwani
Date : 18/02/2023
Language : Python 3.10.6
Details : This is an Artificial Assistant for Voice Commands.
"""

import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import smtplib
import random
import time
import openai
import platform
import socket

engine = pyttsx3.init('sapi5')
# pyttsx3- its a text-to-speech library
# sapi5 -it helps in recognition of voice

voices = engine.getProperty('voices')
engine.setProperty('voices', voices[2].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()
# runAndWait- without this command, speech will not be audible to us

def wishme():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        print("Hello! Good morning!")
        speak("Hello! Good morning!")

    elif hour >= 12 and hour < 18:
        print("Hello! Good afternoon!")
        speak("Hello! Good afternoon!")

    else:
        print("Hello! Good Evening!")
        speak("Hello! Good Evening!")
        time.sleep(0.3)

    print("I am Robo kronos") 
    speak("I am Robo kronos")
    time.sleep(0.1)

    print("I am an advanced machine to assist you with your tasks")
    speak("I am an advanced machine to assist you with your tasks")
    time.sleep(0.1)

    print("please tell me how may i help you")
    speak("please tell me how may i help you")

def takeCommand():
    # it take microphone input from the user and returns string output
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Hearkening....")
        r.pause_threshold = 1
        # pause threshold - is the number of seconds the system will take to recognize the voice after the user has completed their sentence
        audio = r.listen(source,phrase_time_limit=5)

    try:
        print("Recognizing....")
        query = r.recognize_google(audio)
        # Recognizer class helps us to recognize input audios from user.
        print(f"User said: {query}\n")

    except Exception as e:
        # print(e)
        print("Say that again please...")
        return "none"
    return query

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    # smtplib- it is a protocol that allows us to send email
    server.ehlo()
    server.starttls()
    server.login('youremail@gmail.com', 'Your-password-here')
    server.sendmail('youremail@gmail.com', to, content)
    server.close()

def openai_response():
    print("Ask from AI: \n")
    speak("Ask from AI: ")
    prompt = takeCommand().lower() 

    openai.api_key = "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"
    model_engine = "text-davinci-003"
    print("Searching with AI chatGPT...")
    speak("Searching with AI chatGPT...")
    completion= openai.Completion.create(engine=model_engine,prompt=prompt,max_tokens= 1024,n=1,stop=None,temperature=0.9)

    response=completion.choices[0].text
    return response

if __name__ == "__main__":
    wishme()
    
    if 1:
        query = takeCommand().lower()
    # logic for executing tasks based on query

        if'open chat' in query:
            print("Enter your prompt")
            speak('Enter your prompt: ')
            openai_response()
            response = openai_response()
            print(response)
            speak(response)
        # else:
        #     print("Try again")
            
        if 'wikipedia' in query:
            speak('Searching wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        if "google" in query:

            if 'open google' in query:
                print("What you are seeking ?")
                speak("What you are seeking ?")
                search = takeCommand().lower()
                print("Looking for...")
                speak("Looking for...")
                url = "https://google.com/search?q=" + search
                webbrowser.open(url)
            
        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")

        elif 'play music' in query:
            music_dir = 'C:\\Users\\Shail\\Music'
            songs = os.listdir(music_dir)
            r = random.choice(songs)
            #print(r)
            os.startfile(os.path.join(music_dir, r))

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Friend, the time is{strTime}")

        elif 'open code' in query:
            codePath = "C:\\Users\\Shail\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)

        elif 'open whatsapp' in query:
            path = 'https://web.whatsapp.com'
            os.startfile(path)

        elif 'open files' in query:
            filePath = 'C:\\Users\\Shail'
            os.startfile(filePath)

        elif 'open facebook' in query:
            facePath = 'https://www.facebook.com'
            os.startfile(facePath)

        elif "system detail" in query:
            print(f"\n{platform.system()}", end="")  # Software type Windows , Linux, IOS
            speak(platform.system())
            print(f" - {platform.machine()}")  # Type of Processor
            speak(platform.machine())
            print(platform.architecture())  # Type of Software
            print(platform.node())   # Name of Computer.
            speak(platform.node())
            print(platform.processor())  # Processor Details.
            print(platform.uname()) # all above Details
            print("Python Version -",end=" ")
            print(platform.python_version())  # Python Version
            speak("Python Version")
            speak(platform.python_version())

        elif "ip address" in query:
            hostname = socket.gethostname()  # Coputername
            ipaddr = socket.gethostbyname(hostname)  # ip addresss
            print("Computer Name: ", hostname)
            speak("Computer Name")
            speak(hostname)
            print("IP Address:", ipaddr)
            speak("IP Address")
            speak(ipaddr)
        

        elif 'email to sender' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = "whomtosend@gmail.com"
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                # print(e)
                speak("Sorry friend. I am not able to send this email at moment")

        elif "shut down" in query or "shutdown" in query:
            shut = input("\nReally Want to Shutdown:(Y/N):\n>>> ").lower()
            if shut == "y":
                print("\nClosing VS Code,")
                speak("Closing VS Code")
                print("Shutting Down Computer,")
                speak("Shutting Down Computer")
                os.system("TASKKILL /F /IM code.exe")
                os.system("shutdown /s /t 10")

        elif "restart" in query:
            res = input("\nDo You Really Want to Restart:(Y/N):\n>>> ").lower()
            if res == "y":
                print("\nClosing VS Code,")
                speak("Closing VS Code")
                print("Re-starting Computer,")
                speak("ReStarting Computer")
                os.system("TASKKILL /F /IM code.exe")
                os.system("shutdown /r /t 10")

        elif "quit" in query or "bye" in query:
            print("Let me know if you need anything else\n Thankyou")
            speak("Let me know if you need anything else\n Thankyou")
            quit()


