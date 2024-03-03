import speech_recognition as sr
import pyttsx3
import winsound
import pygame
class Speaker:
    def __init__(self):
        self.recognizer = sr.Recognizer()
        self.engine = pyttsx3.init()

    def recognize_speech(self, *args):
        durations = list(args)

        with sr.Microphone() as source:
            self.recognizer.adjust_for_ambient_noise(source, duration = durations[0]) 
            audio = self.recognizer.listen(source, timeout=durations[1], phrase_time_limit=durations[2])

            try:
                text = self.recognizer.recognize_google(audio).lower()

                return text

            except sr.WaitTimeoutError:
                return ''

            except sr.UnknownValueError:
                print("Could not understand audio")
                return ' '

    def speak_text(self, text):
        self.engine.say(text)
        self.engine.runAndWait()
    
    def cancel_speech(self, event):
        self.engine.stop()
        print("Speech cancelled")

    def beep(self):
        for i in range(100):
            winsound.Beep(2440+i, 20)

        winsound.Beep(4440, 250) # Frequency (Hz) and duration (milliseconds) of the beep
    
    

    def activation_sound(self):
        file_path = "assets/activation.wav"
        
        self.make_sound(file_path)
    
    def deactivation_sound(self):
        file_path = "assets/deactivation.MP3"

        self.make_sound(file_path)

    def make_sound(self, file_path):
        pygame.mixer.init()
        try:
            # Load the audio file
            pygame.mixer.music.load(file_path)

            # Play the audio file
            pygame.mixer.music.play()

            # Wait until the audio finishes playing
            while pygame.mixer.music.get_busy():
                continue

        except pygame.error as e:
            print("Error playing audio:", e)


