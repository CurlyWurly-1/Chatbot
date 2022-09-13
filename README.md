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
 - Be aware that the speech recognition part runs in your desktop/laptop, so the speed of speech recognition relies on how fast the CPU is. 

GPT3 INFO - How to get an API key

To get this working with GPT-3, you will need to modify the code to enter your GPT-3 API Key (In the WIN10 Python program, look at about line 30). You can get an API key as follows:
 - In a browser go to https://openai.com/api/ and create your own account
 - When you are logged in, click top right on the "Personal" icon and select "View API keys". In the next screen, press "Create new secret key" and copy the key that gets created. The format of the key will be something like "zz-xxxxxxxxxxyyyyyyyyyyzzzzzzzzzzaaaaaaaaaabbbbbbbb" 
 - Copy this key into the python program (about line 30) so that it looks something like this. N.B. This mocked up value will not work - you must create your own! 
   - openai.api_key = "zz-xxxxxxxxxxyyyyyyyyyyzzzzzzzzzzaaaaaaaaaabbbbbbbb"


USAGE - Brief info on how it works
 - The concept is this 
   - The python program pauses at the "listening" prompt and now starts listening for sounds.
   - If someone speaks, the python program attempts to translate whatever is spoken into text when the speaker has finished speaking. N.B. The speech recognition part of the python program detects the end of a sentence because it looks for period of silence. 
   - The python program now inputs the text into the GPT-3 cloud system via the GPT-3 API.
   - The GPT-3 cloud system processes the input text using its own AI proceses, and tries to construct a semantically relevant response text sentence.
   - The GPT-3 cloud system now passes this response text sentence back to the python program via the GPT-3 API. 
   - In the python program, This response text sentence is now passed to the speech part of the program so that the response text can be spoken back to you. After the spoken part has finished, the program returns to the "listening" prompt, so you can say something else.
 - To get this working, try executing it first with a headset. If the headset is working OK, then the program should automatically pick up which device to use (Nano can be tricky here).
 - Only speak after you see "listening". The program automatically detects when you have finished speaking and if all OK, you should then see "processing". The spoken output will then be issued and after it has finished, you will see "listening" again
 - Try asking "Who are you". The reply should say "Buddy" but be aware that if your device performance is poor, you may have to wait quite a few seconds for the speech recognition part to complete. If you don't get anything spoken back after 20 seconds, something is wrong - Check the device connections 
 - Try saying the following and hear what you get back - Check the python code to see how these responses were programmed 
   - What is your name?
   - What is my name? 
   - How old am I?
   - When is my birthday?  
 - If you extended the "prompt" info to include where you live now, you could ask what are the best restaurents near where I live 

