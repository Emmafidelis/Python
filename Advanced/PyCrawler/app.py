import requests
from bs4 import BeautifulSoup

response = requests.get("https://stackoverflow.com/questions")
soup = BeautifulSoup(response.text, "html.parser")

questions = soup.select(".s-post-summary")
for question in questions:
  print(question.select_one(".s-link").get_text())
  print(question.select_one(".s-post-summary--stats-item-number").get_text())
# print(questions[0].attrs)
# print(questions[0].get("id", 0))
# print(questions[0].select(".s-link"))
# print(questions[0].select_one(".s-link"))
# print(questions[0].select_one(".s-link").get_text())