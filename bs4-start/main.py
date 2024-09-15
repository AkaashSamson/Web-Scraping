from bs4 import BeautifulSoup

with open("D:/Python_practs/Web-Scraping/bs4-start/website.html") as file:
    contents = file.read()

soup = BeautifulSoup(contents, 'html.parser')

print()
print(soup.title)
print()
print(soup.title.string)
print()
print(soup.prettify())