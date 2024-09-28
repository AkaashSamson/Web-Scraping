import requests
from bs4 import BeautifulSoup

mov_url = 'https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/'

response = requests.get(mov_url)
top100_webpage = response.text

soup = BeautifulSoup(top100_webpage, 'html.parser')
top100movies = soup.find_all(name='h3', class_='title')

movies_list = [movie.getText() for movie in top100movies]
movies_list.reverse()
print(movies_list)
with open('top100movies.txt', 'w', encoding='utf-8') as file:
    for movie in movies_list:
        file.write(f"{movie}\n")