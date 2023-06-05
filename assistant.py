import os
import smtplib
import pyttsx3
import webbrowser
import random
import datetime
import wolframalpha
import sys
import speech_recognition as sr
import requests
import wikipedia
import pyaudio

api_weather = 'api.openweathermap.org/data/2.5/weather?q='
email = "jarmatlal@gmail.com"
password = "Jrmt12345"
engine = pyttsx3.init()

client = wolframalpha.Client(email)

voices = engine.getProperty('voices')
engine.setProperty('voice', voices[len(voices) - 1].id)


def speak(command):
    print('computer: ' + command)
    engine.say(command)
    engine.runAndWait()


def good_time():
    current_hour = datetime.datetime.now().hour
    if 0 <= current_hour <= 12:
        speak('Good Morning')
    elif 13 <= current_hour <= 15:
        speak('Good Noon')
    elif 16 <= current_hour <= 18:
        speak('Good Afternoon')
    elif 19 <= current_hour <= 21:
        speak('Good Evening')
    else:
        speak('Good Night')


good_time()
speak('Hello Sir, I am your assistant JARMAT!')
speak('How may I help you?')


def my_commend():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        query = r.recognize_google(audio, language='en-US')
        print('User: ' + query + '\n')
    except sr.UnknownValueError:
        speak('Sorry sir! I didn\'t get it! Try typing your command!')
        query = str(input("Command: "))

    return query


def main():
    while True:
        query = my_commend()
        query = query.lower()

        if 'open youtube' in query:
            speak('okay')
            webbrowser.open('www.youtube.com')
        elif 'open google' in query:
            speak('okay')
            webbrowser.open('www.google.com')
        elif 'open gmail' in query:
            speak('okay')
            webbrowser.open('www.gmail.com')
        elif 'what\'s up' in query or 'how are you' in query:
            stMsg = ['Just doing my job!', 'okay', 'I\'m ready for your next command', 'pretty good']
            speak(random.choice(stMsg))
        elif 'email' in query:
            speak('Who is the recipient?')
            recipient = my_commend()

            if 'me' in recipient:
                is_sent = False
                while not is_sent:
                    speak('What is the subject?')
                    subject = my_commend()
                    speak('What should i say?')
                    content = my_commend()
                    try:
                        server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
                        server.ehlo()
                        server.login(email, password)
                        msg = f'Subject: {subject}\n\n{content}'
                        server.sendmail(email, email, msg)
                        is_sent = True
                    except:
                        speak("Something went wrong.")
                        speak("Want to try again?")
                        answer = my_commend()
                        if 'yes' in answer:
                            is_sent = False
                        else:
                            is_sent = True
            else:
                is_sent = False
                while not is_sent:
                    speak('What is the subject?')
                    subject = my_commend()
                    speak('What should i say?')
                    content = my_commend()
                    try:
                        server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
                        server.ehlo()
                        server.login(email, password)
                        msg = f'Subject: {subject}\n\n{content}'
                        server.sendmail(email, recipient, msg)
                        is_sent = True
                    except:
                        speak("Something went wrong.")
                        speak("Want to try again?")
                        answer = my_commend()
                        if 'yes' in answer:
                            is_sent = False
                        else:
                            is_sent = True

        elif 'weather' in query:
            if 'in' in query:
                try:
                    all_words = query.split()
                    city = all_words[all_words.index('in') + 1]
                    url_weather = api_weather + city
                    json_weather = requests.get(url_weather).json()
                    formatted_weather = json_weather['weather'][0]['main']
                    speak('The weather is ' + formatted_weather)
                except:
                    is_weather = False
                    while not is_weather:
                        try:
                            speak("Didn't understand...")
                            speak('Please say the city and the country!')
                            place = my_commend()
                            place_det = place.split()
                            city = place_det[0]
                            country = place_det[1]
                            url_weather = api_weather + city + ',' + country
                            json_weather = requests.get(url_weather).json()
                            formatted_weather = json_weather['weather'][0]['main']
                            speak('Got it!')
                            speak('The weather is ' + formatted_weather)
                            is_weather = True
                        except:
                            is_weather = False
            else:
                res = requests.get('https://ipinfo.io')
                data = res.json()
                city = data['city']
                country = data['country']
                country = country.lower()
                url_weather = api_weather + city + ',' + country
                json_weather = requests.get(url_weather).json()
                formatted_weather = json_weather['weather'][0]['main']
                speak('The weather is ' + formatted_weather)
        elif 'search' in query:
            speak('Searching...')
            search = query.split()
            search_str = ''
            for x in range(len(search)):
                if x > search.index('search'):
                    search_str = search[x] + ' '
            try:
                try:
                    res = client.query(search_str)
                    results = next(res.results).text
                    speak('WOLFRAM ALPHA says - ')
                    speak('Got it.')
                    speak(results)
                except:
                    results = wikipedia.summary(search_str)
                    speak('Got it!')
                    speak('WIKIPEDIA says - ')
                    speak(results)
            except:
                speak('Can\'t find it...')
                speak('Try searching on google!')
                webbrowser.open('www.google.com')
        else:
            speak('Searching...')
            try:
                try:
                    res = client.query(query)
                    results = next(res.results).text
                    speak('WOLFRAM ALPHA says - ')
                    speak('Got it.')
                    speak(results)
                except:
                    results = wikipedia.summary(query)
                    speak('Got it!')
                    speak('WIKIPEDIA says - ')
                    speak(results)
            except:
                speak('Can\'t find it...')
                speak('Try searching on google!')
                webbrowser.open('www.google.com')

        next_command = ['Ready for the next command', 'Next command, Sir!', 'Ready for your next command',
                        'Ready for another Task!']
        speak(random.choice(next_command))


if __name__ == "__main__":
    main()
