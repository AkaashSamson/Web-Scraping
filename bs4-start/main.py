from bs4 import BeautifulSoup

with open("D:/Python_practs/Web-Scraping/bs4-start/website.html") as file:
    contents = file.read()

soup = BeautifulSoup(contents, 'html.parser')

all_anchor_tags = soup.find_all(name="a")
# print(all_anchor_tags)

for tag in all_anchor_tags:
    #print(tag.getText())
    print(tag.get("href"))

heading = soup.find(name="h1", id="name")
print(heading)
print()

section_heading = soup.find(name="h3", class_="heading")
print(section_heading)
print()

company_url = soup.select_one(selector="p a")
print(company_url)
print()

name = soup.select_one("#name")
print(name)
print()

headings = soup.select(".heading")
print(headings)
print()
