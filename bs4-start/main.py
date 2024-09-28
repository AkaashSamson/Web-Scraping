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
proper_list = []
for idx,tag,sc in zip(range(0, len(atags)), atags, article_score):
    title = tag.find(name='a').getText()
    link = tag.find(name='a').get('href')
    score = int(sc.getText().split()[0])
    # print(f"{idx+1}: {title} ({sc.getText().split()[0]}) - {link}")
    proper_list.append({'title': title, 'link': link, 'score': score})

#Sort the list of dictionaries by score
sorted_list = sorted(proper_list, key=lambda k: k['score'], reverse=True)

for idx, item in enumerate(sorted_list):
    print(f"{idx+1}: {item['title']} ({item['score']}) - {item['link']}")