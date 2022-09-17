# Chatbot
Speech recognition feeding GPT-3, with the response being spoken back.


GENERAL INFO - How to install on your laptop/desktop

 - You need to have Python3 installed (e.g. 3.10) , a useful IDE (e.g. VsCode) and some basic programming knowledge
 - There are 2 main python programs:
   - The "WIN10" version called "WIN10_chatbot.py" is self contained i.e. it doesn't call "speak.py".
   - The "Jetson Nano" version called "jetson_nano_chatbot.py" uses a separate program called "speak.py" for speech output
 - To use theses programs, you will have to install the following modules (works on python3.10). In WIN10, execute the following in an elevated  "CMD Prompt" window (Run as Administrator). If executing in Jetson Nano, add SUDO before the commands 
   - pip3 install pyttsx3
   - pip3 install openai
   - pip3 install speechRecognition
   - pip3 install PyAudio
 - The speech recognition part is using the "recognise_google" method. For more information on alternatives, refer to https://pypi.org/project/SpeechRecognition/. 
 - The Chatbot engine is GPT-3. For more information, refer to https://openai.com/blog/openai-api/ 

GPT3 INFO - How to get an API key

To get this working with GPT-3, you will need to modify the code to enter your GPT-3 API Key (In the WIN10 Python program, look at about line 30). You can get an API key as follows:
 - In a browser go to https://openai.com/api/ and create your own account
 - When you are logged in, click top right on the "Personal" icon and select "View API keys". In the next screen, press "Create new secret key" and copy the key that gets created. The format of the key will be something like "zz-xxxxxxxxxxyyyyyyyyyyzzzzzzzzzzaaaaaaaaaabbbbbbbb" 
 - Copy this key into the python program (about line 30) so that it looks something like this. N.B. This mocked up value will not work - you must create your own! 
   - openai.api_key = "zz-xxxxxxxxxxyyyyyyyyyyzzzzzzzzzzaaaaaaaaaabbbbbbbb"


USAGE - Brief info on how it works
 - The concept is this 
   - After the python program has finished initialising itself, it will speak its introduction and thereafter, pause at the "listening" prompt. The program is now waiting for sounds to exceed a set background noise level. 
   - When someone speaks, the sound level will exceed the background noise level and this triggers the python program to record the audio until either a period of silence or a timeout has been exceeded. The period of silence is used as an indicator that speaking has finished earlier than the timeout, and this kicks off the next part of the process where the python program stops listening and now tries to identify the sounds it has heard, as a series of words. These words are translated into text form with each word separated by a space and stored in a text variable called "myText". 
   - This variable "myText" is now enhanced with "personal variable" information e.g. your name, age and location using function "InfoTextSet". The values for these personal variables are seen near the top of the program starting at line 9. Go ahead and change these values as you see fit - It is there to pass information to the chatbot about the Human speaker. If you adapt this program so that the speaker has already been identified (e.g. by face recognition), you could pass the known values about the Human speaker for a more contextful chatbot experience e.g. name, age, location. 
   - The python program now passes this variable "myText" via a GPT-3 API into the GPT-3 cloud system.
   - The GPT-3 cloud system processes this input text sentence using its own AI processes, and tries to construct a semantically relevant text sentence to use as as a response.
   - The GPT-3 cloud system now passes the response text sentence back to the python program via the GPT-3 API, and the python program stores it in another text variable called "gptText". 
   - In the python program, the text variable "gptText" is now filtered to remove some characters that are not required for the speech part
   - In the python program, the now formatted text variable "gptText" is passed to the speech part of the program so that it can be spoken back to you. After the spoken part has finished, the python program then returns back to the start i.e. the "listening" prompt will be re-displayed, so you can say something else.
 - To get this working, try executing it first with a headset. If the headset is working OK, then the program should automatically pick up which device to use (Nano can be tricky here).
 - Only speak after you see "listening". The program automatically detects when you have finished speaking and if all OK, you should then see "processing". The spoken output will then be issued and after it has finished, you will see "listening" again
 - Try asking "Who are you". The reply should say "Buddy" but be aware that if your device performance is poor, you may have to wait quite a few seconds for the speech recognition part to complete. If you don't get anything spoken back after 20 seconds, something is wrong - Check the device connections 
 - Try saying the following and hear what you get back - Check the python code to see how these responses were programmed 
   - What is your name?
   - What is my name? 
   - How old am I?
   - When is my birthday?  
 - If you adapt the "prompt" info to include where you actually live, Ask  "What is the nearest pub called and what is its telephone number" and you may be suprised that it works as well as it does! 
