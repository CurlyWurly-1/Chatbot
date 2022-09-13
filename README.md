# Chatbot
Speech recognition feeding GPT-3, with the response being spoken back.

These programs were written for python3 - you will have to install some modules. Bw aware that the speech recognition part runs on youe desktop/laptop, so the speed of speech recogntion relies on how fast your device is. 
There are 2 main programs:
 - The Jetson Nano version called "jetson_nano_chatbot.py" will execute "speak.py" for speech output
 - The WIN10 version called "WIN10_chatbot.py" is self contained i.e. it doesn't call "speak.py". To use this in WIN10, use the latest python3 version (e.g. 3.10) and execute the following in a "CMD Prompt" window (Run as Administrator)
   - pip3 install pyttsx3
   - pip3 install openai
   - pip3 install speechRecognition
   - pip3 install PyAudio

GPT3 INFO

To get this working with GPT-3, you will need to add an access key (In the WIN10 Python program, look at about line 30 for where you need to add this key - it is the line starting  "openai.api_key = <...>". You can get an API key as follows:
 - In a browser go to https://openai.com/api/ and create an account
 - When you are logged in, click top right on the "Personal" icon and select "View API keys". In the next screen, press "Create new secret key" and copy the key that gets created. The format of the key will be something like "zz-xxxxxxxxxxyyyyyyyyyyzzzzzzzzzzaaaaaaaaaabbbbbbbb" 
 - Copy this key into line 30 so that it looks something like this. Use your own generated API key because this mocked up one will not work! 
   - openai.api_key = "zz-xxxxxxxxxxyyyyyyyyyyzzzzzzzzzzaaaaaaaaaabbbbbbbb"
