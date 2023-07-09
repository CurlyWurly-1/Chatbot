# Python program to translate
# speech to text and text to speech
 
import speech_recognition as sr
from subprocess import Popen
import os
import openai
botName      = "Buddy"
myName       = "Pete"
myAge        = "202"
myBirthDate  = "1st April 1801" 
myBirthPlace = "Cardiff"
myLocation   = "Chester"

def InfoTextSet (botName, myName, myAge, myBirthDate, myBirthPlace, myLocation):
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
    openai.api_key = "<PUT YOUR API KEY HERE>"
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
 
def speak_and_wait(gptText) :
    p1 = Popen(['python3', 'speak.py', gptText,])    # For Jetson Nano
    p1_status = p1.wait()

## THIS IS FOR MUTING ALSA MESSAGES!! - START #######
def py_error_handler(filename, line, function, err, fmt):
    pass
## THIS IS FOR MUTING ALSA MESSAGES!! - END   #######


##########################################################
## START OF CODE
##########################################################

## THIS IS FOR MUTING ALSA MESSAGES!! - START #######
import ctypes
ERROR_HANDLER_FUNC = ctypes.CFUNCTYPE(None, ctypes.c_char_p, ctypes.c_int,
                                      ctypes.c_char_p, ctypes.c_int,
                                      ctypes.c_char_p)
c_error_handler = ERROR_HANDLER_FUNC(py_error_handler)
try:
    asound = ctypes.cdll.LoadLibrary('libasound.so.2')
    asound.snd_lib_error_set_handler(c_error_handler)
except OSError:
    pass
## THIS IS FOR MUTING ALSA MESSAGES!! - END   #######


# Initialize the recognizer
r = sr.Recognizer()

print("Speaking my introduction")   
gptText = "Hi " + myName + ", I am " + botName + ", Please talk to me or ask a question whenever you see the listening prompt"   
speak_and_wait(gptText)
     
while(1):   
     
    try:

        with sr.Microphone() as source:
            #listens for the user's input
            audio = r.adjust_for_ambient_noise(source, duration=0.2)    
            print("Listening")
            audio = r.listen(source, phrase_time_limit=8)
            print("processing")             

        try:    
            myText = r.recognize_google(audio, language = 'en-UK')    
            print("Q: "+myText)            
            myText = InfoTextSet(botName, myName, myAge, myBirthDate, myBirthPlace, myLocation) + myText
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
                if gptText != "": 
                    print("error - index out of range")    
            speak_and_wait(gptText)

        except sr.UnknownValueError:    
            print("Google Speech Recognition could not understand audio")
        except sr.RequestError as e:   
            print("Could not request results from Google Speech Recognition service; {0}".format(e))

    except sr.RequestError as e:
        print("Could not request results; {0}".format(e))
         
    except sr.UnknownValueError:
        print("Sounds ignored")

