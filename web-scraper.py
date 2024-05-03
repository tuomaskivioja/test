import requests
from bs4 import BeautifulSoup

res = requests.get('https://stackoverflow.com/questions/tagged/python')

soup = BeautifulSoup(res.text, 'html.parser')

questions = soup.find_all('div', {'class': 's-post-summary'})

for question in questions:
    question_text = question.find('h3', {'class': 's-post-summary--content-title'}).text
    print(question_text)

