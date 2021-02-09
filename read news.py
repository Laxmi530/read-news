# Reading news from the website https://newsapi.org
# Here we use json requests module

from win32com.client import Dispatch
import requests
import json


def speak(str):
    speak = Dispatch('SAPI.SpVoice')
    speak.Speak(str)

speak('News for today.....Lets begin')
url = 'https://newsapi.org/v2/top-headlines?sources=the-times-of-india&apiKey=d093053d72bc40248998159804e0e67d'
news = requests.get(url).text
news_dict = json.loads(news)
arts = news_dict['articles']
for article in arts:
    speak(article['description'])
    speak('Moving on to the top news.....Please listen carefully')
speak('Thanks for listening')

