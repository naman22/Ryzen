import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import smtplib
import webbrowser as wb
import psutil
import pyjokes
import os
import pyautogui
import time


engine = pyttsx3.init()


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def time_():  # Tells Time
    time = datetime.datetime.now().strftime("%I:%M:%S")
    speak("The current time is")
    speak(time)


def date_():  # Tells Date
    year = datetime.datetime.now().year
    month = datetime.datetime.now().month
    date = datetime.datetime.now().day
    speak("The current date is")
    speak(date)
    speak(month)
    speak(year)


def wishme():  # Wishes according to the time of the day
    speak("Welcome back Naman")
    date_()
    time_()

    # Greetings

    hour = datetime.datetime.now().hour
    if 6 <= hour < 12:
        speak("Good Morning Sir")
    elif 12 <= hour < 18:
        speak("Good Afternoon Sir")
    elif 18 <= hour < 24:
        speak("Good Evening Sir")
    else:
        speak("Good Night Sir")
    speak("Ryzen at your service . How can I help you Sir?")


def takeCommand():  # Convert audio command to text
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Ryzen is Listening.....")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Ryzen is Recognizing Your Voice.....")
        query = r.recognize_google(audio, language='en-US')
        print("Ryzen recognized that you said :")
        print(query)
    except Exception as e:
        print(e)
        print("Say that again please.....")
        return "None"
    return query


def SendEmail(to, content):  # For sending mails
    server = smtplib.SMTP('64.233.184.108')
    server.ehlo()
    server.starttls()
    server.login('naman.shukla_cs18@gla.ac.in', 'YOYON@M@N2026')
    server.sendmail('naman.shukla_cs18@gla.ac.in', to, content)
    server.close()


def cpu():  # Tells the cpu usage and battery
    usage = str(psutil.cpu_percent())
    speak("CPU is at " + usage)
    battery = psutil.sensors_battery()
    speak("Battery is at ")
    speak(battery.percent)


def joke():  # Tells Jokes
    speak(pyjokes.get_jokes())


def screenshot():
    img = pyautogui.screenshot()
    img.save('C:/users/naman/Desktop/screenshot.png')
    speak("Screenshot taken Sir!")


if __name__ == '__main__':
    wishme()
    while True:
        query = takeCommand().lower()

        # All commands will be stored in lower case

        if 'time' in query:  # Tells Time
            time_()
        elif 'date' in query:  # Tells Date
            date_()
        elif 'wikipedia' in query:
            speak("Searching.....")
            query = query.replace("wikipedia", "")
            result = wikipedia.summary(query, sentences=3)
            speak("According to Wikipedia")
            print(result)
            speak(result)
        elif 'send email' in query:
            try:
                speak("What should I say?")
                content = takeCommand()

                # provide receiver email address
                speak("Who is the receiver?")
                receiver = input("Enter the receiver's email \n")
                to = receiver
                SendEmail(to, content)
                speak(content)
                speak('Ryzen has sent the email successfully Sir')
            except Exception as e:
                print(e)
                speak("Ryzen was unable to send the email")
        elif 'search in chrome' in query:
            speak("What should I search?")
            # Location of chrome browser
            chromepath = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'

            search = takeCommand().lower()
            wb.get(chromepath).open_new_tab(search + '.com')  # only websites with .com

        elif 'search youtube' in query:
            speak("What should I search?")
            search_Term = takeCommand().lower()
            speak("Here we go to YOUTUBE!")
            wb.open('https://www.youtube.com/results?search_query= ' + search_Term)
        elif 'search google' in query:
            speak("What should I search?")
            search_Term = takeCommand().lower()
            speak("Searching.....")
            wb.open('https://www.google.com/search?search_Term= ' + search_Term)
        elif 'battery' in query:
            cpu()
        elif 'joke' in query:
            joke()
        elif 'bye' in query:
            speak("GoodBye Sir,have a good day")
            quit()
        elif 'word' in query:
            speak("Opening MS Word.....")
            os.startfile('C:/Program Files/Microsoft Office/root/Office16/WINWORD.exe')
        elif 'diary' in query:
            speak("Diary Opened,What should I write sir?")
            notes = takeCommand()
            file = open('notes.txt', 'w')
            speak("Sir should I include Date and Time?")
            ans = takeCommand()
            if 'yes' in ans or 'sure' in ans:
                strtime = datetime.datetime.now().strftime("%H:%M:%S")
                file.write(strtime)
                file.write(':~')
                file.write(notes)
                speak("Done Taking Notes Sir!")
            else:
                file.write(notes)
        elif 'show note' in query:
            speak("Showing Notes!")
            file = open('notes.txt', 'r')
            print(file.read())
            speak(file.read())
        elif 'screenshot' in query:
            screenshot()
        elif 'remember that' in query:
            speak("What should I remember?")
            memory = takeCommand()
            speak("You asked to remember " + memory)
            remember = open('memory.txt', 'w')
            remember.write(memory)
            remember.close()
        elif 'do you remember' in query:
            remember = open('memory.txt', 'r')
            speak("You asked me to remember " + remember.read())
        elif 'where is' in query:
            query = query.replace("where is", "")
            location = query
            speak("you asked to locate " + location)
            wb.open_new_tab("https://www.google.co.in/maps/place/" + location)
        elif 'stop listening' in query or 'go to sleep' in query:
            speak("For how long should I sleep?")
            ans = int(takeCommand())
            time.sleep(ans)
            speak("Hey! Ryzen is back from sleep!")
        elif 'log out' in query:
            os.system('shutdown-1')
        elif 'restart' in query:
            os.system("shutdown /r /t 1")
        elif 'shutdown' in query:
            os.system("Shutdown /s /t 1")
