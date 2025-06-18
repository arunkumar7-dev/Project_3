import speech_recognition as sr
import webbrowser
import pyttsx3
import musicLibrary
import requests

recognaizer = sr.Recognizer()
engine = pyttsx3.init()
# news_api = "be29a230439a4eb0a226846059a57784"

def speak(text: str):
    engine.say(text)
    engine.runAndWait()

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

    # elif "news" in command.lower():
    #     r = requests.get(f"https://newsapi.org/v2/top-headlines?country=us&apiKey={news_api}")
    #     if r.status_code == 200:
    #         # Parse the JSON response
    #         data = r.json()
            
    #         # Extract the articles
    #         articles = data.get('articles', [])
            
    #         # Print the headlines
    #         for article in articles:
    #             speak(article['title'])

    #     else:
    #         # Let open ai handle the request
    #         pass
    
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
