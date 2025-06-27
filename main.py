import speech_recognition as sr
import webbrowser
import pyttsx3
import musicLibrary
from gtts import gTTS
import pygame
import time
import os
from client import aiProcess

recognaizer = sr.Recognizer()
engine = pyttsx3.init()

# I added just for study purpose
def old_speak(text: str): #Not using due to bad unser interface
    engine.say(text)
    engine.runAndWait()

# New speak fucntion
def speak(text: str):
    tts = gTTS(text)
    tts.save('tempaudio.mp3')

    pygame.mixer.init()
    pygame.mixer.music.load("tempaudio.mp3")
    pygame.mixer.music.play()

    while pygame.mixer.music.get_busy():
        time.sleep(1)

    pygame.mixer.music.unload()  # Optional but good practice  
    os.remove("tempaudio.mp3")


def processCommand(command):
    if "open google" in command.lower():
        webbrowser.open("https://google.com")

    elif "open facebook" in command.lower():
        webbrowser.open("https://facebook.com")

    elif"open youtube" in command.lower(): 
        webbrowser.open("https://youtube.com")

    elif"open linkedin" in command.lower(): 
        webbrowser.open("https://in.linkedin.com")
    
    elif command.lower().startswith("play"):
        song = command.lower().split(" ")[1]
        link = musicLibrary.music[song]
        webbrowser.open(link)
    else:
        output = aiProcess(command)
        speak(output)

    
if __name__ == "__main__" :
    speak("Initializing your personal assistant AD....")
    
    while True:
        # Listen for the wake word AD
        # Obtain audio from the Microphone

        r = sr.Recognizer()
        r.energy_threshold = 300
        
        print("Recognizing....")
        # Recognize speech using google
        try:
            with sr.Microphone() as source:
                r.adjust_for_ambient_noise(source)
                print("Listening....")
                audio = r.listen(source)
                word = r.recognize_google(audio)
                if(word.lower() == "hello ad"):
                    speak("Yeah")
                    #Listen for command
                    with sr.Microphone() as source:
                        print("Ad is now Active....")
                        audio = r.listen(source)
                        command = r.recognize_google(audio)


                        processCommand(command)
                else:
                    speak("I did not understand")
        except Exception as e:
            print("Error; {0}".format(e))
