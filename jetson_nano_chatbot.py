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
myLocation   = "Ruabon"

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
    openai.api_key = "<PUT_YOUR API_FROM OPENAPI HERE>"
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


# Find out which device you want to use, and amend lines 26 and 51 with the device number (starting from zero) 
#['tegra-hda: HDMI 0 (hw:0,3)', 
#'tegra-snd-t210ref-mobile-rt565x: - (hw:1,0)','
#'tegra-snd-t210ref-mobile-rt565x: - (hw:1,1)', 
#'tegra-snd-t210ref-mobile-rt565x: - (hw:1,2)', 
#'tegra-snd-t210ref-mobile-rt565x: - (hw:1,3)',
#'tegra-snd-t210ref-mobile-rt565x: - (hw:1,4)', 
#'tegra-snd-t210ref-mobile-rt565x: - (hw:1,5)',
#'tegra-snd-t210ref-mobile-rt565x: - (hw:1,6)', 
#'tegra-snd-t210ref-mobile-rt565x: - (hw:1,7)', 
#'tegra-snd-t210ref-mobile-rt565x: - (hw:1,8)', 
#'tegra-snd-t210ref-mobile-rt565x: - (hw:1,9)', 
#'CD002: USB Audio (hw:2,0)', 
#'Canyon CNS CWC5 Webcam: USB Audio (hw:3,0)', 'hdmi', 'pulse', 'music', 'default']


print("Speaking my introduction")   
gptText = "Hi " + myName + ", I am " + botName + ", Please talk to me or ask a question whenever you see the listening prompt"   
p1 = Popen(['python3', 'speak.py', gptText,])    # For Jetson Nano
p1_status = p1.wait()

     
# Mic List
mic_list = sr.Microphone.list_microphone_names()
print(mic_list)

try:
    device_no = int(12)
    with sr.Microphone(device_index=device_no) as source:
        print("Please be quiet - Adjusting for background noise")
        #listens for the user's input
        r.adjust_for_ambient_noise(source)
except:
    print("Device 12 didn't work, trying device 11")
    device_no = int(11)
    with sr.Microphone(device_index=device_no) as source:
        print("Please be quiet - Adjusting for background noise")
        #listens for the user's input
        r.adjust_for_ambient_noise(source)    


while(1):   
     
    # Exception handling to handle
    # exceptions at the runtime
    try:
         
        # use the microphone as source for input.
        with sr.Microphone(device_index=device_no) as source:
            #listens for the user's input
#            print("Adjusting")
            r.adjust_for_ambient_noise(source, duration =0.2)    
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

            p1 = Popen(['python3', 'speak.py', gptText,])    # For Jetson Nano
#            (output, err) = p1.communicate()  
            #This makes the wait possible
            p1_status = p1.wait()
            #This will give you the output of the command being executed
#            print ("Command output: " + output)

        except sr.UnknownValueError:    
            print("Google Speech Recognition could not understand audio")
        except sr.RequestError as e:   
            print("Could not request results from Google Speech Recognition service; {0}".format(e))

    except sr.RequestError as e:
        print("Could not request results; {0}".format(e))
         
    except sr.UnknownValueError:
        print("Sounds ignored")

