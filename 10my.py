import requests
import pyttsx3 as tts
import pyaudio
from vosk import Model, KaldiRecognizer
from time import sleep
import json
# Speech Recognition
model = Model("Lab-10-main\model") # path to your model directory or use models/en-us/model
rec = KaldiRecognizer(model, 160000)

# Text To Speech
engine = tts.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id) 

# PyAudio for audio input
p = pyaudio.PyAudio()
stream = p.open(format=pyaudio.paInt16, channels=1, rate=160000,
                input=True, frames_per_buffer=8000)
stream.start_stream()

# Command List
commands = {
    "создать": "new joke",
    "тип": "speech or dialogue",
    "прочесть": "read joke",
    "категория": "category",
    "записать": "add to file"
}
engine.say('Запущен')
engine.runAndWait()
while True:
    data = stream.read(8000)
  
    if len(data) == 0:
        break
    if rec.AcceptWaveform(data):
        text = rec.Result()
        for key, value in commands.items():
            if key in text: # Check command
                if "создать" in text: # Create new joke
                    r = requests.get("https://v2.jokeapi.dev/joke/Any?safe-mode")
                    joke = r.json()
                    print(joke)
                    try:
                        engine.say(joke["setup"])
                        engine.runAndWait()
                        sleep(1)# Text to speech setup
                        engine.say(joke["delivery"])
                        engine.runAndWait()
                    except:
                        engine.say(joke["joke"])
                        engine.runAndWait()
                        sleep(1)
                        # Text to speech delivery
                elif "тип" in text:
                    engine.say(joke["type"])
                    engine.runAndWait()
                elif "прочесть" in text:
                    try:
                        engine.say(joke["setup"])
                        engine.runAndWait()
                        sleep(1)# Text to speech setup
                        engine.say(joke["delivery"])
                        engine.runAndWait()
                    except:
                        engine.say(joke["joke"])
                        engine.runAndWait()
    
                elif "категория" in text:
                    engine.say(joke["category"])
                    engine.runAndWait()
                elif "записать" in text:
                    with open('joke.txt', 'w') as fp:
                        fp.write(json.dumps(joke))
                    pass