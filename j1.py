import speech_recognition as sr
from time import ctime
import time
import os
from gtts import gTTS
import pyttsx3
import sys
import subprocess
def speak(audioString):
    print(audioString)
    engine = pyttsx3.init()
    engine.setProperty('rate',150)
   
    engine.say(audioString)
    engine.runAndWait()
 
def recordAudio():
# Record Audio
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Say something!")
        audio = r.listen(source)
 
# Speech recognition using Google Speech Recognition
    data = ""
    try:
# Uses the default API key
# To use another API key: `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
        data = r.recognize_google(audio)
        print("You said: " + data)
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))
 
    return data

def jarvis(data):
   
    if "hello" in data:
        speak("or bhaay , kee haal hain")
    if "how are you" in data:
        speak("I am fine")
 
    if "what time is it" in data:
        speak(ctime())
 
    if "where is" in data:
        data = data.split(" ")
        location = data[2]
        speak("Hold on Frank, I will show you where " + location + " is.")
        os.system("chromium-browser https://www.google.nl/maps/place/" + location + "/&amp;")
    if "open file" in data:
        speak("yess sir")
        os.system('nautilus')
    if "open terminal" in data:
        speak("yess sir")
        os.system('terminal')
    if "open notepad" in data:
        speak("yess sir")
        os.system('gedit')
    if "open setting" in data:
        speak("yess sir")
        os.system('setting')

    if "shutdown" in data:
        speak("come soon ")
       
        subprocess.call(["shutdown","-h","now"])
       
    if "open Chrome" in data:
        speak("okk sir ")
       
        subprocess.call(["google-chrome"])
        


    if "who am I" in data:
        speak("you are kaleem molani, my creator, A handsom and very smart man,GHANTA, hahahahahahahahahaha ,but my friend,kashika is sooo smart")
       
        



    if "open YouTube" in data:
        speak("okk sir ")
       
        subprocess.call(["google-chrome", "https://www.youtube.com/"])
       

    if "open my mail" in data:
        speak("okk sir ")
       
        subprocess.call(["google-chrome" ,"--app=https://mail.google.com/mail/u/0/#inbox"]) 
     

    if "open slide" in data:
        speak("okk sir ")
       
        subprocess.call(["google-chrome", "https://docs.google.com/presentation/u/0/"]) 
       

    if "Google doc" in data:
        speak("okk sir ")
       
        subprocess.call(["google-chrome", "https://docs.google.com/document/u/0/"])
    

    if "my Instagram" in data:
        speak("okk sir ")
       
        subprocess.call(["google-chrome", "--app=https://www.instagram.com/?hl=en"]) 
     
    if "my Facebook" in data:
        speak("okk sir ")
       
        subprocess.call(["google-chrome", "--app=https://www.facebook.com/"])
 
 
    if "ok bye" in data:
        speak("goodbye kaleem")
        sys.exit("goodbye!")
 
# initialization
time.sleep(2)
speak("Hi kaleem , what can I do for you?")
while 1:
    data = recordAudio()
    jarvis(data)
