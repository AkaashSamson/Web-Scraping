from bs4 import BeautifulSoup
import requests

# with open("D:/Python_practs/Web-Scraping/bs4-start/website.html") as file:
    # contents = file.read()

response = requests.get('https://news.ycombinator.com/news')
yc_webpage = response.text

soup = BeautifulSoup(yc_webpage, 'html.parser')
#print(soup.title)

# atags = soup.find(name='span', class_='timeline')
atags = soup.find_all('span', class_='titleline')

article_score = soup.find_all(name='span', class_='score')

for idx,tag,sc in zip(range(0, len(atags)), atags, article_score):
    title = tag.find(name='a').getText()
    link = tag.find(name='a').get('href')
    print(f"{idx+1}: {title} ({sc.getText()}) - {link}")