
import speech_recognition as sr
import pyttsx3
import datetime
import wikipedia
import webbrowser
import os
import smtplib

# Set up text-to-speech engine
engine = pyttsx3.init()

# Function to speak the given text
def speak(text):
    engine.say(text)
    engine.runAndWait()

# Function to recognize speech
def listen():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = recognizer.listen(source)
        command = ""

        try:
            print("Recognizing...")
            command = recognizer.recognize_google(audio)
            print(f"You said: {command}")
        except sr.UnknownValueError:
            print("Sorry, I didn't get that. Can you please repeat?")
        except sr.RequestError as e:
            print(f"Could not request results from Google Speech Recognition service; {e}")

        return command.lower()

# Function to execute commands
def execute_command(command):
    if 'wikipedia' in command:
        speak("Searching Wikipedia...")
        query = command.replace("wikipedia", "")
        result = wikipedia.summary(query, sentences=2)
        speak("According to Wikipedia, " + result)
    elif 'open youtube' in command:
        webbrowser.open("https://www.youtube.com/")
    elif 'open google' in command:
        webbrowser.open("https://www.google.com/")
    elif 'play music' in command:
        music_dir = "D:\music"
        songs = os.listdir(music_dir)
        os.startfile(os.path.join(music_dir, songs[0]))
    elif 'time' in command:
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        speak(f"The current time is {current_time}")
    elif 'send email' in command:
        # Configure your email settings
        speak("Whom should I send the email to?")
        recipient = listen()
        speak("What should the email say?")
        email_content = listen()
        # Use your own email sending logic here
        # Example: Use smtplib to send an email
        speak("Email sent successfully!")
    elif 'exit' in command:
        speak("Goodbye!")
        exit()

# Main loop
speak("Hello! How can I assist you today?")
while True:
    command = listen()
    execute_command(command)
