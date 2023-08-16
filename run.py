import openai
from AppOpener import open
from AppOpener import close
import pyttsx3
from playsound import playsound
import os
import pandas as pd
import time
import speech_recognition as sr
engine=pyttsx3.init()
newVoiceRate=130
engine.setProperty('rate',newVoiceRate)
openai.api_key = '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'
def get_completion(prompt, model="gpt-3.5-turbo"):
    messages = [{"role": "user", "content": prompt}]
    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=0,
    )
    return response.choices[0].message["content"]
r=sr.Recognizer()
text="hello"
while True:
    with sr.Microphone(device_index=1) as source:
        print("Hello i m jarvis your virtual assistant")
        r.adjust_for_ambient_noise(source)
        audio= r.listen(source)
        text = r.recognize_google(audio)
        text_split=text.split()
        print(text_split)
        for x in text_split:
            if(x=="search"):
                respone=get_completion(text)
                engine.say(respone)
                engine.runAndWait()
            if(x=="shutdown"):
                engine.say("system is going offline ")
                engine.runAndWait()
                time.sleep(5)
                os.system('shutdown -s')
            if(x=="open" and "whatsapp"):
                open("whatsapp")
            if(x=="close" and "whatsapp"):
                close("whatsapp")
            else:
                respone=get_completion(text)
    if text_split[0]=="stop":
        break
