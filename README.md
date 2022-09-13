# Chatbot
Speech recognition feeding GPT-3, with the response being spoken back.

 - These programs were written for python3. 
 - To use them, you will have to install some modules. 
 - Be aware that the speech recognition part runs on youe desktop/laptop, so the speed of speech recogntion relies on how fast your device is. 
 - There are 2 main programs:
   - The WIN10 version called "WIN10_chatbot.py" is self contained i.e. it doesn't call "speak.py". To use this in WIN10, use the latest python3 version (e.g. 3.10) and execute the following in a "CMD Prompt" window (Run as Administrator)
     - pip3 install pyttsx3
     - pip3 install openai
     - pip3 install speechRecognition
     - pip3 install PyAudio
   - The Jetson Nano version called "jetson_nano_chatbot.py" uses "speak.py" for speech output


GPT3 INFO

To get this working with GPT-3, you will need to modify the code to enter your GPT-3 API Key (In the WIN10 Python program, look at about line 30). You can get an API key as follows:
 - In a browser go to https://openai.com/api/ and create your own account
 - When you are logged in, click top right on the "Personal" icon and select "View API keys". In the next screen, press "Create new secret key" and copy the key that gets created. The format of the key will be something like "zz-xxxxxxxxxxyyyyyyyyyyzzzzzzzzzzaaaaaaaaaabbbbbbbb" 
 - Copy this key into the python program (about line 30) so that it looks something like this. N.B. This mocked up value will not work - you must create your own! 
   - openai.api_key = "zz-xxxxxxxxxxyyyyyyyyyyzzzzzzzzzzaaaaaaaaaabbbbbbbb"


USAGE
 - The concept of this python program is this - Whatever you say (at the "listening" prompt) will be translated into text by the speech recogntiion part of the program. This text is then fed to GPT-3 and if GPT-3 understands it correctly, it will return another text sentence which should be relevant and this will be spoken back out to you.
 - To get this working, try it with a headset. If the headset is working OK, then the program should automatically pick up which device to use.
 - Execute the program and when you see "listening", wait a bit and then say "Who are you" into your headset microphone. The reply should say "Buddy" but be aware that if your device performance is poor, you may have to wait quite a few seconds for the speech recognition part to complete. 

 - Try saying the following and hear what you get back - Check the python code to see how these responses were programmed 
   - What is your name?
   - What is my name? 
   - How old am I?
   - When is my birthday?  
