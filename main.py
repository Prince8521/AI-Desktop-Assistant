import speech_recognition as sr
import os
import pyttsx3
import webbrowser
import openai
from gtts import gTTS
import win32com.client
from config import apikey
import random

# Initialize the text-to-speech engine

engine = pyttsx3.init()
# Initialize the speech recognition engine
recognizer = sr.Recognizer()

chatStr = ""
def chat(query):
    global chatStr
    print(chatStr)
    openai.api_key = apikey
    chatStr += f"Prince: {query}\n Jarvis: "
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt= chatStr,
        temperature=0.7,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    #todo: Wrap this inside of a  try catch block
    say(response["choices"][0]["text"])
    chatStr += f"{response['choices'][0]['text']}\n"
    return response["choices"][0]["text"]
def ai(prompt):
    openai.api_key = apikey
    text = f"OpenAI response for Prompt:  {prompt} \n *******************\n\n"

    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=prompt,
        temperature=1,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
# todo: Wrap this inside of a try catch block
    print(response["choices"][0]["text"])
    text += response["choices"][0]["text"]
    if not os.path.exists("Openai"):
        os.mkdir("Openai")
    with open(f"Openai/{' '.join(prompt.split('intelligence')[1:]).strip()}.txt", "w") as f:
        f.write(text)

def say(text):

    engine.say(text)
    engine.runAndWait()

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        audio = r.listen(source)
    try:
        print("Recongnizing...")
        query = r.recognize_google(audio, language="en-in")
        print("User said:",query)
        return query
    except Exception as e:
        return "Some Error Occurred. Sorry from Jarvis"
def play_song(song_name):
    # Construct the YouTube search URL for the song
    search_url = f"https://www.youtube.com/results?search_query={song_name}"
    webbrowser.open(search_url)

if __name__ == "__main__":
    print('Pycharm')
    say("Hello I am your assistant, How can I help You")
    while True:
        print("Listening...")
        query = takeCommand()
        sites = [["youtube", "https://www.youtube.com"], ["wikipedia", "https://www.wikipedia.com"],
                 ["google", "https://www.google.com"],]
        for site in sites:
            if f"Open {site[0]}".lower() in query.lower():
                say(f"Opening {site[0]} sir...")
                webbrowser.open(site[1])

        if "play song" in query.lower():
            song_name = query.replace("play song", "").strip()
            say(f"Playing {song_name} on YouTube...")
            play_song(song_name)

        elif "Open My Profile".lower() in query.lower():
            say("Opening LinkedIn Sir...")
            webbrowser.open("https://www.linkedin.com/in/prince-kumar-256950208/")

        elif "Using artificial intelligence".lower() in query.lower():
            ai(prompt=query)

        elif "Jarvis Quit".lower() in query.lower():
            exit()

        elif "reset chat".lower() in query.lower():
            chatStr = ""

        else:
            print("Chatting...")
            chat(query)

