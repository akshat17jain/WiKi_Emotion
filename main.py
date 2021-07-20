import text2emotion as te
import requests
from bs4 import BeautifulSoup as bs
import matplotlib.pyplot as plt

query = input("emotion analysis on ")
url = requests.get('https://en.wikipedia.org/wiki/'+query).text
page=bs(url,"html.parser")
text = ""
for word in page.find_all('p'):
	text += word.text

print("parsing done.")
print("this might take a while...")


emotion=te.get_emotion(text)
plt.bar(*zip(*emotion.items()))
plt.title("Emotional analysis of " + query)
plt.show()
