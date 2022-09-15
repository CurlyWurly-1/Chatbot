# Python program to translate
# speech to text and text to speech
import speech_recognition as sr
import pyttsx3
import os
import openai
botName      = "Buddy"
myName       = "Dracula"
myAge        = "202"
myBirthDate  = "1st April 1801" 
myBirthPlace = "The dark side of the Moon"
myLocation   = "London"

def InfoTextSet (botName, myName, myAge, myBirthDate, myBirthPlace):
    infoText = ""
    infoText = botName + " is a chatbot that cheerfully answers questions\n"
    infoText + infoText + "You:What is your name?\n" +botName +":My name is " + botName + "\n" 
    infoText = infoText + "You:What is my name?\n" + botName +":Your name is " + myName + "\n" 
    infoText = infoText + "You:How old am I?\n" + botName +":You are " + myAge + " years old\n" 
    infoText = infoText + "You:When was I born?\n" + botName + ":You were born on " + myBirthDate +"\n" 
    infoText = infoText + "You:Where was I born?\n" + botName +":You were born in "+ myBirthPlace + "\n" 
    infoText = infoText + "You:Where am I now?\n" + botName +":You are in "+ myLocation + "\n" 
    infoText = infoText + "You:What is my location now?\n" + botName +"Your location is "+ myLocation + "\n" 
    infoText = infoText + "You:Where do I live now?\n" + botName +"You live in "+ myLocation + "\n" 
    return infoText 


def GPT_Completion(texts):
## Call the API key under your account (in a secure way)
    openai.api_key = "<PUT YOU API FROM OPENAI HERE>"
    response = openai.Completion.create(
    engine="text-davinci-002",
    prompt =  texts,
    temperature = 0.9,
    top_p = 1,
    max_tokens = 64,
    frequency_penalty = 0,
    presence_penalty = 0)
#    return print(response.choices[0].text)
    return response.choices[0].text


# Function to convert text to speech
def SpeakText(command):
    engine.say(command)
    engine.runAndWait()


# Print mic list (use this find the device number)
# mic_list = sr.Microphone.list_microphone_names()
# print(mic_list)


# Initialize the speech speaking engine
engine = pyttsx3.init()

# Initialize the speech recognition engine
r = sr.Recognizer()

with sr.Microphone() as source:
    print("Please be quiet - Adjusting for background noise")
# listens for the user's input
    r.adjust_for_ambient_noise(source)
    print("Speaking my introduction")   
    SpeakText("Hi " + myName + ", I am " + botName + ", Please talk to me or ask a question whenever you see the listening prompt" )      

# Loop infinitely for user to
# speak
while(1):   
     
    # Exception handling to handle
    # exceptions at the runtime
    try:
         
        # use the microphone as source for input.
        with sr.Microphone() as source:
             
            # wait for a second to let the recognizer
            # adjust the energy threshold based on
            # the surrounding noise level
            # r.adjust_for_ambient_noise(source, duration=0.2)
            r.adjust_for_ambient_noise(source)             
            # listens for the user's input
            print("Listening")
            audio = r.listen(source, None, 15)
            print("Processing")             

        try:    
            myText = r.recognize_google(audio, language = 'en-UK')    
            print("Q: "+myText)            
            myText = InfoTextSet(botName, myName, myAge, myBirthDate, myBirthPlace) + myText
            gptText = GPT_Completion(myText)
            print(gptText)   
            try:
                if (gptText[0] == '?') :
                    gptText = gptText[1:]
                if ('?' in gptText) :
                    temp = gptText
                    zexit = False
                    while zexit == False :
                        if (temp[0] == '?') :
                            zexit = True
                        temp = temp[1:]
                    if temp != "":
                        gptText = temp
                if ('You:' in gptText) :
                    zexit = False
                    while zexit == False :
                        if (gptText[0] == ':') :
                            zexit = True
                        gptText = gptText[1:]
                if (':' in gptText) :
                    zexit = False
                    while zexit == False :
                        if (gptText[0] == ':') :
                            zexit = True
                        gptText = gptText[1:]
                if ('http' in gptText) :
                    gptText = "Please refine your question"
            except:
                print("error - index out of range")    
            SpeakText(gptText)

        except sr.UnknownValueError:    
            print("Google Speech Recognition could not understand audio")
        except sr.RequestError as e:   
            print("Could not request results from Google Speech Recognition service; {0}".format(e))

         
    except sr.RequestError as e:
        print("Could not request results; {0}".format(e))
         
    except sr.UnknownValueError:
        print("Sounds ignored")
