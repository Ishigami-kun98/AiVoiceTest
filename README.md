# AiVoiceTest
Used just for self learning about using API of ElevenLab's AI

What is this project?
It is a simple UI for users to wrote text and have them speeches by the AI which are developed in ElevenLabs.
The UI is designed with tkinter and since it is just for sperimental uses, i didn't pay too much attention on the graphics design.
The project AI is realized by using voice of a game character which i found on web using the script downloadFile, however this script works only for the site i used. 
The script concatenateVoice is used to concatenate all ogg file in voiceToClone folder and the result is stored in combinedVoice.
Actually the main script is the fundamental one, the rest is just used for me to train and get material for the AI, but if u find lots of voice that are splitted in few files, u can put them all in VoiceToClone folder and use the concatenateVoice Script to combine them for ur voice test.

Requirement
-Python 3.9 the version i m using
-Pillow
-BS4
-pydub
-pygame
-time

