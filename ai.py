import pyttsx3
import speech_recognition as sr

class AI():    
    def __init__(self, name=None):
        self.engine = pyttsx3.init()
        self.recognizer = sr.Recognizer()
        self.mic = sr.Microphone()

        with self.mic as source:
            self.recognizer.adjust_for_ambient_noise(source)

    def say(self, sentence):
        self.engine.say(sentence)
        self.engine.runAndWait()
    
    def listen(self):
        print("Listening...")
        with self.mic as source:
            audio = self.recognizer.listen(source)
            print("Processing...")
            
            try:
                phrase = self.recognizer.recognize_google(audio, show_all=False, language="en")
            except:
                print("Didn't understand what you said")
            
            print("You said", phrase)
            return phrase
