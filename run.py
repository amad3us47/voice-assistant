import openai
import pyttsx3
import os
import time
import speech_recognition as sr
from AppOpener import open
from AppOpener import close

# Initialize text-to-speech engine
engine = pyttsx3.init()
newVoiceRate = 130
engine.setProperty('rate', newVoiceRate)

# Set your OpenAI API key
openai.api_key = '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'

def get_completion(prompt, model="gpt-3.5-turbo"):
    messages = [{"role": "user", "content": prompt}]
    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=0,
    )
    return response.choices[0].message["content"]

r = sr.Recognizer()

while True:
    with sr.Microphone() as source:
        print("Hello, I'm Jarvis, your virtual assistant")
        r.adjust_for_ambient_noise(source, duration=1)
        audio = r.listen(source)
        
        try:
            text = r.recognize_google(audio)
            text = text.lower()  # Convert to lowercase for easier comparison
            print("Recognized:", text)
            
            if "search" in text:
                response = get_completion(text)
                print("Response:", response)
                engine.say(response)
                engine.runAndWait()

            elif "shutdown" in text:
                engine.say("System is going offline")
                engine.runAndWait()
                time.sleep(5)
                os.system('shutdown -s')

            elif "open whatsapp" in text:
                print("Opening WhatsApp")
                # Implement your logic to open WhatsApp here
                open("whatsapp")

            elif "close whatsapp" in text:
                print("Closing WhatsApp")
                # Implement your logic to close WhatsApp here
                close("whatsapp")
            else:
                print("Unknown command")

        except Exception:
            print("Could not understand audio")
        except sr.RequestError as e:
            print(f"Could not request results; {e}")
