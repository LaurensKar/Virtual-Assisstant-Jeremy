import sys
import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes
import requests, json
listener = sr.Recognizer()
engine = pyttsx3.init()

def talk(text):
    engine.say(text)
    engine.runAndWait()

def take_command():
    try:
        with sr.Microphone() as source:
            print('listening...')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'jeremy' in command:
                command = command.replace('jeremy', '')

    except:
        pass
    return command


def weather(city):

    api_key = "47ad9a8962661da5b3c88e2d9ab163a5"
    base_url = "http://api.openweathermap.org/data/2.5/weather?"
    city_name = city
    complete_url = base_url + "appid=" + api_key + "&q=" + city_name
    response = requests.get(complete_url)
    x = response.json()
    if x["cod"] != "404":
        y = x["main"]

        # store the value corresponding
        # to the "temp" key of y
        current_temperature = y["temp"]
        return str(current_temperature)

        # print following values
        '''print(" Temperature (in kelvin unit) = " +
                        str(current_temperature) + 
            "\n atmospheric pressure (in hPa unit) = " +
                        str(current_pressure) +
            "\n humidity (in percentage) = " +
                        str(current_humidiy) +
            "\n description = " +
                        str(weather_description)) 
    else: 
        print(" City Not Found ")
        '''

def run_jeremy():
    command = take_command()
    print(command)
    if 'play' in command:
        song = command.replace('play', '')
        talk('playing' + song)
        pywhatkit.playonyt(song)
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%H:%M %p')
        talk('Current time is ' + time)
        print('Current time is ' + time)
    elif 'who is' in command:
        person = command.replace('who is', '')
        info = wikipedia.summary(person, 1)
        print(info)
        talk(info)
    elif 'joke' in command:
        talk(pyjokes.get_joke())
    elif 'how are you' in command:
        talk('I am doing good and you?')
    elif 'weather' in command:
        talk('What is the name of the city?')
        city = take_command()
        weather_api = weather(city)
        talk(weather_api + 'degree fahrenheit')
        print(weather_api  + ' degree fahrenheit')
    elif 'stop' in command:
        sys.exit()
    elif 'alarm' in command:
        text = command.replace('i want to set an alarm', '')
        talk('At what hour would you like the alarm to go off')
        hour = take_command()
        talk('And how many minutes')
        minutes = take_command()
        talk('The alarm is set to go off at ' + hour + ' hours and ' + minutes + ' minutes')
        print(hour)
        print(minutes)
        while True:
            if hour == datetime.datetime.now().hour and minutes == datetime.datetime.now().minute:
                talk('ring ring')

    else:
        talk('Please say the command again.')

while True:
    run_jeremy()