#Friday Python project
#Friday is a desktop voice assistant for windows made using python
#Author: Jitin
from os import spawnl
import pyttsx3
import datetime
import speech_recognition as sr  #Google speech recognition API
import wikipedia
import webbrowser
from bs4 import BeautifulSoup			#For webscrapping using python
import pywhatkit as pwt
from random import choice, randint
import requests
engine = pyttsx3.init('sapi5')           #TTS=Text to speech # <--- sapi 5 is for Windows
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)  # <--- voice id can be male(0) - David or female(1)-Zira



def speak(audio):
    engine.say(audio)
    engine.runAndWait()

'''Current temperature in hyderabad'''
def weather():
	search="temperature in hyderabad"
	url=f"https://www.google.com/search?q={search}"
	r=requests.get(url)
	data=BeautifulSoup(r.text,"html.parser")
	temp=data.find("div",class_ = "BNeawe").text
	speak(f"current{search} is {temp}")

def wishme():
	hour=int(datetime.datetime.now().hour)
	if hour>=0 and hour<12:
		speak("Good Morning boss, I am FRDIDAY.")
	elif hour>=12 and hour<18:
		speak("Good Afternoon boss, I am FRDIDAY.")
	else:
		speak("Good evening boss, I am FRDIDAY.")
	speak("Today is ")
	speak(datetime.datetime.now().strftime("%Y-%m-%d"))
	speak("and the time is ")
	speak(datetime.datetime.now().strftime("%H:%M:%S"))

def takeComand():
	'''Takes microphone input from user and returns string output'''
	r=sr.Recognizer()
	with sr.Microphone() as source:
		print("Listening...")
		r.pause_threshold=1
		audio=r.listen(source)
	'''Exception handling using try-except block'''
	try:
		print("Recognizing...")
		query=r.recognize_google(audio,language='en_in')
		print(f"User said {query}\n")
	except Exception as e:
		speak("I'm afraid I don't understand")
		return "None"
	return query

	
def music():
	'''Plays Youtube music'''
	webbrowser.open("https://www.youtube.com/channel/UC-9-kyTW8ZkZNDHQJ6FgpwQ")

		
if __name__=="__main__" :
	wishme()
	weather()
	while True:
		query=takeComand().lower()
		'''Logic for FRIDAY'''
		if 'wikipedia' in query:
			speak('Searching in Wikipedia')
			query=query.replace("wikipedia","")
			results=wikipedia.summary(query,sentences=2)
			speak("According to wikipedia\n")
			speak(results)
		elif 'youtube' in query:
			webbrowser.open("https://www.youtube.com/")
		elif 'google' in query:
			speak('Searching in google, boss!')
			query=query.replace("search google for","")
			pwt.search(query)
			pwt.close_tab(5)
		elif 'music' in query:
			music()
		elif 'quit' in query or 'bye' in query:
			# choice = random.__dir__()
			choice=randint(0,2)
			if choice==1:
				speak("Happy to help!")
			else:
				speak("Bye")
			break
