import speech_recognition as sr
import nltk

r = sr.Recognizer()
with sr.Microphone() as source:
    audio = r.adjust_for_ambient_noise(source)
    print("Say something!")
    audio = r.listen(source)

try:
    s = (r.recognize_google(audio))
    message = (s.lower())
    print(message)

except sr.UnknownValueError:
    print("$could not understand audio")
except sr.RequestError as e:
    print("Could not request results$; {0}".format(e))

tokens = nltk.word_tokenize(str(message))

import win32com.client
speaker = win32com.client.Dispatch("SAPI.SpVoice")
speaker.Speak(message)

print(tokens)

tagged = nltk.pos_tag(tokens)

print(tagged[0:6])