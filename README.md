# Chatbot
Speech recognition feeding GPT-3, with the response being spoken back.

These programs were written for python3 - you will have to install some modules. 
There are 2 main programs:
 - The Jetson Nano version called "jetson_nano_chatbot.py" will execute "speak.py" for speech output
 - The WIN10 version called "WIN10_chatbot.py" is self contained i.e. it doesn't call "speak.py". To use this in WIN10, use the latest python3 version (e.g. 3.10) and execute the following in a "CMD Prompt" window (Run as Administrator)
   - pip3 install pyttsx3
   - pip3 install openai
   - pip3 install speechRecognition
