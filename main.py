import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes


listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', 'english+f4')
engine.setProperty('rate', 178)

def talk(text):
    engine.say(text)
    engine.runAndWait()

def take_command():
    try:
        with sr.Microphone() as source:
            print('Listening...')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'milo' in command:
                command = command.replace('milo', '')
                print(command)
    except:
        pass
    return command


def run_milo():
    command = take_command()
    print(command)
    if 'play' in command:
        song = command.replace('play', '')
        talk('playing' + song)
        pywhatkit.playonyt(song)
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        talk('The time is' + time)
    elif 'what is' in command:
        information = command.replace('what is', '')
        info = wikipedia.summary(information, 1)
        print(info)
        talk(info)
    elif 'date' in command:
        talk('Sorry, I have a headache')
    elif 'How are you' in command:
        talk('Im good')
    elif 'joke' in command:
        talk(pyjokes.get_joke())
    else:
        talk('Please say that again, I did not understand.')
        print('I did  not understand')


while True:
    run_milo()
