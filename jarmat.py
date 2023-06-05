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
import ssl
import pyowm
import bs4
import psutil
import keyword
path = 'C:\\Users\\TAL_M\\Desktop\\'
is_browser_chose = False
is_push_to_talk = False
browser = ''
key_weather = pyowm.OWM('9f7c2fa467bc6f9cc9bea91abf2e4e2c')
email = "jarmatlal@gmail.com"
password = "fbleozbxdcylgsnq"
chrome_path = "C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s"
firefox_path = 'C:/Program Files/Mozilla Firefox/irefox.exe %s'
edge_path = ''
engine = pyttsx3.init()

client = wolframalpha.Client('U47V33-EQLJEHEH2H')

voices = engine.getProperty('voices')
engine.setProperty('voice', voices[len(voices) - 1].id)


def speak(command):
    print('computer: ' + command)
    engine.say(command)
    engine.runAndWait()


def speak_without_print(command):
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
        print('Listening...')
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source, duration=1)
        audio = r.listen(source)
    try:
        query = r.recognize_google(audio)
        print('User: ' + query + '\n')
    except sr.UnknownValueError:
        speak('Sorry sir! I didn\'t get it! Try typing your command!')
        query = str(input("Command: "))
        if 'retry' in query:
            speak('Please try say it again!')
            query = my_commend()

    return query


def wake_up():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source, duration=1)
        audio = r.listen(source)
        try:
            query = r.recognize_google(audio)
            if 'wake up' in query:
                print('User: ' + query + '\n')
                return False
            else:
                return True
        except sr.UnknownValueError:
            wake_up()


def choose_browser():
    speak('Which browser you want to use?')
    speak('Chrome, firefox or edge?')
    answer = my_commend()
    answer = answer.lower()
    if 'chrome' in answer:
        speak('Okay, chrome is successfully going to be the browser!')
        return chrome_path
    elif 'fire' in answer or 'fox' in answer:
        speak('Okay, firefox is successfully going to be the browser!')
        return firefox_path
    elif 'edge' in answer:
        speak('Okay, edge is successfully going to be the browser!')
        return '$'
    else:
        speak('Didn\'t understand, opening in your default browser.')
        return '$'


def change_speed_rate():
    speak('Faster or slower')
    answer = my_commend()
    if 'fast' in answer:
        speed_rate_fast()
    elif 'slow' in answer:
        speed_rate_slow()
    else:
        speak('Can\'t do this...')


def speed_rate_fast():
    rate = engine.getProperty('rate')
    engine.setProperty('rate', rate + 50)


def speed_rate_slow():
    rate = engine.getProperty('rate')
    engine.setProperty('rate', rate - 50)


def change_volume():
    speak('Lower or higher?')
    answer = my_commend()
    if 'low' in answer:
        volume_low()
    elif 'high' in answer:
        volume_high()
    else:
        speak('Can\'t do that...')


def volume_high():
    volume = engine.getProperty('volume')
    if volume < 1:
        engine.setProperty('volume', volume + 0.25)
        msg = ['Okay?', 'This is fine?', 'This is good?']
        speak(random.choice(msg))
        answer_yn = my_commend()
        if 'no' in answer_yn:
            volume_high()
        elif 'yes' in answer_yn:
            speak('Great!')
        else:
            answer = str(input(speak('Didn\'t understand, please write(yes/no): ')))
            if 'yes' in answer:
                speak('Okay, this is good!')
            elif 'no' in answer:
                volume_high()
            else:
                speak('Can\'t do that...')
    else:
        speak('This is the highest volume!')


def volume_low():
    volume = engine.getProperty('volume')
    if volume > 0:
        engine.setProperty('volume', volume - 0.25)
        msg = ['Okay?', 'This is fine?', 'This is good?']
        speak(random.choice(msg))
        answer_yn = my_commend()
        if 'no' in answer_yn:
            volume_low()
        elif 'yes' in answer_yn:
            speak('Great!')
        else:
            answer = str(input(speak('Didn\'t understand, please write(yes/no): ')))
            if 'yes' in answer:
                speak('Okay, this is good!')
            elif 'no' in answer:
                volume_low()
            else:
                speak('Can\'t do that...')
    else:
        print('The lowest volume!')


def meant_yt(query):
    if 'in youtube' in query and 'search' not in query:
        speak('Did you meant to search in youtube?')
        speak('Yes or no?')
        answer = my_commend()
        if 'ye' in answer:
            query = 'search ' + query
            return True, query
        elif 'no' in answer:
            return False, query
        else:
            speak('Sorry, can\'t do it...')


def meant_gl(query):
    if 'in google' in query and 'search' not in query:
        speak('Did you meant to search in google?')
        speak('Yes or no?')
        answer = my_commend()
        if 'ye' in answer:
            query = 'search ' + query
            return True, query
        elif 'no' in answer:
            return False, query
        else:
            speak('Sorry, didn\'t understand...')


def main():
    global is_browser_chose, browser, is_push_to_talk
    while True:
        query = my_commend()
        query = query.lower()
        is_meant_gl = False
        is_meant_yt = False
        if 'in youtube' in query and 'search' not in query:
            is_meant_yt, query = meant_yt(query)
        elif 'push to talk' in query:
            speak('Which key from your keyboard?')
            key = str(input('Key: '))
            is_push_to_talk = True
        elif 'in google' in query and 'search' not in query:
            is_meant_gl, query = meant_gl(query)
        elif 'shut' in query and 'down' in query or 'turnof' in query:
            speak('Do you want to turn off this computer?')
            answer = my_commend()
            if 'ye' in answer:
                speak('Turning off.')
                os.system('shutdown -s')
            elif 'no' in answer:
                speak('Okay, don\'t turn it off!')
            else:
                speak('Didn\'t understand, so i guess I don\'t turn off your pc.')
            continue
        elif 'change' in query and 'browser' in query:
            browser = choose_browser()
            speak_without_print('Changed browser successfully done')
            continue

        if 'open youtube' in query:
            speak('okay')
            if not is_browser_chose:
                browser = choose_browser()
                is_browser_chose = True
            if '$' in browser:
                webbrowser.open('www.youtube.com')
            else:
                webbrowser.get(browser).open('www.youtube.com')
        elif 'open program' in query:
            speak('Which program?')
            answer = my_commend()
            speak('This program - ' + answer + '?')
            answer_yn2 = my_commend()
            if 'no' in answer_yn2:
                answer = str(input(speak('Write it down: ')))
            answer = answer.lower()
            try:
                for filenames in os.listdir(path):
                    if answer in filenames.lower():
                        speak('Open ' + str(filenames) + '?')
                        answer_yn = my_commend()
                        if 'ye' in answer_yn:
                            answer = str(filenames)
                            os.startfile(path + answer)
                            speak('Found it!')
                            break
                        elif 'no' in answer_yn:
                            speak('Okay!')

            except FileNotFoundError:
                speak('Sorry, can\'t find it.')
        elif 'close program' in query:
            speak('Which program?')
            answer = my_commend()
            speak('This program - ' + answer + '?')
            answer_yn2 = my_commend()
            if 'no' in answer_yn2:
                answer = str(input(speak('Write it down: ')))
            answer = answer.lower()
            try:
                for filenames in psutil.process_iter():
                    if answer in filenames.name().lower():
                        speak('Close ' + filenames.name() + '?')
                        answer_yn = my_commend()
                        if 'ye' in answer_yn:
                            answer = filenames.name()
                            os.system(str('taskkill /f /im ').upper() + answer)
                            speak('Found it!')
                            continue
                        elif 'no' in answer_yn:
                            speak('Okay!')
                            break
                continue
            except FileNotFoundError:
                speak('Sorry, can\'t find it.')
        elif 'search' in query and 'in google' in query or is_meant_gl:
            google_url = 'https://www.google.com/search?q='
            search = ''
            words = query.split()
            for x in range(len(words)):
                if words.index('search') < x < words.index('in'):
                    if x == words.index('in') - 1:
                        search += words[x]
                    else:
                        search += words[x] + ' '
            google_url += search + '&source=lnms'
            speak('All, pictures, news or videos? ')
            answer = my_commend()
            if not is_browser_chose:
                browser = choose_browser()
                is_browser_chose = True
            if 'all' in answer:
                if '$' in browser:
                    webbrowser.open(google_url)
                else:
                    webbrowser.get(browser).open(google_url)
            elif 'picture' in answer:
                if '$' in browser:
                    webbrowser.open(google_url + '&tbm=isch')
                else:
                    webbrowser.get(browser).open(google_url + '&tbm=isch')
            elif 'news' in answer:
                if '$' in browser:
                    webbrowser.open(google_url + '&tbm=nws')
                else:
                    webbrowser.get(browser).open(google_url + '&tbm=nws')
            elif 'video' in answer:
                if '$' in browser:
                    webbrowser.open(google_url + '&tbm=vid')
                else:
                    webbrowser.get(browser).open(google_url + '&tbm=vid')
            else:
                speak('Didn\'t understand, do you want to search it in google?')
                answer_yn = my_commend()
                if 'ye' in answer_yn:
                    webbrowser.open('https://www.google.com')
                elif 'no' in answer_yn:
                    speak('Okay, let\'s continue!')
                else:
                    speak('Sorry, did\'t understand you again...')
            is_meant_gl = False
        elif 'thank' in query:
            speak('No problem, Sir!')
        elif 'search' in query and 'in youtube' in query or is_meant_yt:
            search = ''
            words = query.split()
            for x in range(len(words)):
                if words.index('search') < x < words.index('in'):
                    if x == words.index('in') - 1:
                        search += words[x]
                    else:
                        search += words[x] + ' '
            if not is_browser_chose:
                browser = choose_browser()
                is_browser_chose = True
            if '$' in browser:
                webbrowser.open('www.youtube.com/results?search_query=' + search)
            else:
                webbrowser.get(browser).open('www.youtube.com/results?search_query=' + search)
            is_meant_yt = False
        elif 'open google' in query:
            if not is_browser_chose:
                browser = choose_browser()
                is_browser_chose = True
            speak('okay')
            if '$' in browser:
                webbrowser.open('https://www.google.com')
            else:
                webbrowser.get(browser).open('https://www.google.com')
        elif 'open gmail' in query:
            if not is_browser_chose:
                browser = choose_browser()
                is_browser_chose = True
            speak('okay')
            if '$' in browser:
                webbrowser.open('https://www.gmail.com')
            else:
                webbrowser.get(browser).open('https://www.gmail.com')
        elif 'what' in query and 'hour' in query or 'time' in query:
            print(str(datetime.datetime.now().hour) + ' h' + ' : ' + str(datetime.datetime.now().minute) + ' m')
            speak_without_print(str(datetime.datetime.now().hour) + ' and ' + str(datetime.datetime.now().minute) +
                                ' minutes.')
        elif 'what' in query and 'date' in query:
            speak('Which format?')
            speak('first or second?')
            print('1) day/month/year')
            print('2) month/day/year')
            answer = my_commend()
            if 'first' in answer:
                print(str(datetime.datetime.now().day) + '/' + str(datetime.datetime.now().month) + '/' + str(
                    datetime.datetime.now().year))
                speak_without_print(
                    str(datetime.datetime.now().day) + ' to ' + str(datetime.datetime.now().month) + str(
                        datetime.datetime.now().year))
            elif 'second' in answer:
                print(str(datetime.datetime.now().month) + '/' + str(datetime.datetime.now().day) + '/' + str(
                    datetime.datetime.now().year))
                speak_without_print(
                    str(datetime.datetime.now().month) + ' to ' + str(datetime.datetime.now().day) + str(
                        datetime.datetime.now().year))
            else:
                speak('Did\'t understand...')
        elif 'what\'s up' in query or 'how are you' in query or 'hello' in query and len(query.split()) == 1:
            stMsg = ['Just doing my job!', 'okay', 'I\'m ready for your next command', 'pretty good']
            speak(random.choice(stMsg))
        elif 'email' in query:
            context = ssl.create_default_context()
            is_rec = False
            speak('Who is the recipient?')
            recipient = my_commend()
            if '@gmail.com' not in recipient and not 'me' in recipient:
                recipient = recipient + '@gmail.com'
            while not is_rec:
                speak(recipient + ", this is right?")
                answer = my_commend()
                if 'no' in answer:
                    speak('Please write your recipient...')
                    recipient = input('recipient: ')
                    if '@gmail.com' not in recipient and not 'me' in recipient:
                        recipient = recipient + '@gmail.com'
                else:
                    is_rec = True
            if 'me' in recipient:
                is_sent = False
                while not is_sent:
                    speak('What is the subject?')
                    subject = my_commend()
                    speak('What should i say?')
                    content = my_commend()
                    try:
                        with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
                            smtp.login(email, password)
                            msg = 'Subject: {}\n\n{}'.format(subject, content)
                            smtp.sendmail(email, email, msg)
                            smtp.quit()
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
                        server = smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context)
                        server.login(email, password)
                        msg = 'Subject: {}\n\n{}'.format(subject, content)
                        server.sendmail(email, recipient, msg)
                        server.quit()
                        is_sent = True
                    except:
                        speak("Something went wrong.")
                        speak("Want to try again?")
                        answer = my_commend()
                        if 'yes' in answer:
                            is_sent = False
                        else:
                            is_sent = True
        elif 'weather' in query or 'temperature' in query:
            if 'in' in query:
                try:
                    all_words = query.split()
                    city = all_words[all_words.index('in') + 1]
                    ob = key_weather.weather_at_place(city)
                    weather = ob.get_weather()
                    temp = weather.get_temperature('celsius')['temp']
                    status = weather.get_status()
                    speak('The weather is ' + status + ', and the temperature is ' + str(temp) + ' celsius!')
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
                            ob = key_weather.weather_at_place(city + ', ' + country)
                            weather = ob.get_weather()
                            temp = weather.get_temperature('celsius')['temp']
                            status = weather.get_status()
                            speak('Got it!')
                            speak('The weather is ' + status + ', and the temperature is ' + str(temp) + ' celsius!')
                            is_weather = True
                        except:
                            is_weather = False
            else:
                res = requests.get('https://ipinfo.io')
                data = res.json()
                city = data['city']
                ob = key_weather.weather_at_place(city)
                weather = ob.get_weather()
                temp = weather.get_temperature('celsius')['temp']
                status = weather.get_status()
                speak('The weather is ' + status + ', and the temperature is ' + str(temp) + ' celsius!')
        elif 'bye' in query or 'rest' in query:
            speak('bye')
            good_time()
            break
        elif 'sleep' in query:
            is_sleep = True
            speak('Okay, good night...')
            while is_sleep:
                is_sleep = wake_up()

        elif 'change volume' in query:
            change_volume()
        elif 'change speed' in query:
            change_speed_rate()
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
                if not is_browser_chose:
                    browser = choose_browser()
                    is_browser_chose = True
                if '$' in browser:
                    webbrowser.open('https://www.google.com')
                else:
                    webbrowser.get(browser).open('https://www.google.com')

        next_command = ['Ready for the next command', 'Next command, Sir!', 'Ready for your next command',
                        'Ready for another Task!']
        speak(random.choice(next_command))


if __name__ == "__main__":
    main()
