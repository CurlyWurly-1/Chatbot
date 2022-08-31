# Python program to translate
# speech to text and text to speech
 
 
import speech_recognition as sr
from subprocess import Popen
import os
import openai

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
speech = sr.Microphone(device_index=11)


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
     
     
# Loop infinitely for user to
# speak
mic_list = sr.Microphone.list_microphone_names()
print(mic_list)

# use the microphone as source for input.
with sr.Microphone(device_index=11) as source:
    #listens for the user's input
    print("Adusting for background noise")
    audio = r.adjust_for_ambient_noise(source) 


while(1):   
     
    # Exception handling to handle
    # exceptions at the runtime
    try:
         
        # use the microphone as source for input.
        with sr.Microphone(device_index=11) as source:
            #listens for the user's input
            print("Listening")
#            audio = r.adjust_for_ambient_noise(source)    
            audio = r.listen(source)
            print("processing")             

        try:    
            MyText = r.recognize_google(audio, language = 'en-UK')    
            print("Q: "+MyText)            
            GptText = GPT_Completion(MyText)
            print(GptText)   
            p1 = Popen(['python3', 'speak.py', GptText,])    # For Jetson Nano
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
