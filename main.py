import pyttsx3
import speech_recognition as sr
import os
import sys
import webbrowser
def talk (words):
    engine = pyttsx3.init()
    engine.say (words)
    engine.runAndWait()
talk ("Привет, скажи что-нибудь  мне хорошее")