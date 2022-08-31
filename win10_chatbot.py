# Python program to translate
# speech to text and text to speech
 
 
import speech_recognition as sr
import pyttsx3
import os
import openai

def GPT_Completion(texts):
## Call the API key under your account (in a secure way)
    openai.api_key = "<PUT YOU API FROM OPENAI HERE>"
    response = openai.Completion.create(
    engine="text-davinci-002",
    prompt =  texts,
    temperature = 0.6,
    top_p = 1,
    max_tokens = 64,
    frequency_penalty = 0,
    presence_penalty = 0 )
#    return print(response.choices[0].text)
    return response.choices[0].text
 
# Initialize the recognizer
r = sr.Recognizer()
 
# Function to convert text to
# speech
def SpeakText(command):
     
    # Initialize the engine
    engine = pyttsx3.init()
    engine.say(command)
    engine.runAndWait()
     
     
# Loop infinitely for user to
# speak
 
while(1):   
     
    # Exception handling to handle
    # exceptions at the runtime
    try:
         
        # use the microphone as source for input.
        with sr.Microphone() as source2:
             
            # wait for a second to let the recognizer
            # adjust the energy threshold based on
            # the surrounding noise level
            r.adjust_for_ambient_noise(source2, duration=0.2)
             
            #listens for the user's input
            audio2 = r.listen(source2)
             
            # Using google to recognize audio
            MyText = r.recognize_google(audio2)
            MyText = MyText.lower()
 
#            print("Did you say "+MyText)
            print("Q: "+MyText)            
            GptText = GPT_Completion(MyText)
            print(GptText)   
            SpeakText(GptText)
             
    except sr.RequestError as e:
        print("Could not request results; {0}".format(e))
         
    except sr.UnknownValueError:
        print("Sounds ignored")
