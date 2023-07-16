import requests
from bs4 import BeautifulSoup
import os

chapter_lists = []
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/115.0"}
content1 = requests.get("https://ww5.mangakakalot.tv/manga/manga-dx980806",headers = headers)
#下載網址: https://ww5.mangakakalot.tv/
html1 = content1.text
soup1 = BeautifulSoup(html1,"html.parser")
lis = soup1.findAll("ul")
for h1s in lis:
    manga_name = h1s.find("h1")
manga_name = manga_name.string
print(manga_name)
os.mkdir(manga_name)

all_divs = soup1.findAll("div",attrs={"class": "row"})
for title in all_divs:
    chapters = title.findAll("a")
    for name in chapters:
        ch = ("https://ww5.mangakakalot.tv" + name.get("href"))
        chapter_lists.append(ch)
chapter_lists.reverse()
print(chapter_lists)
print("manga-chapter: " + str(len(chapter_lists))) 
x = len(chapter_lists)

for y in range (x):
    content2 = requests.get(str(chapter_lists[y]),headers = headers)
    html2 = content2.text
    soup2 = BeautifulSoup(html2,"html.parser")
    all_images = soup2.findAll("img",attrs={"class": "img-loading"})
    i=0; j=0
    images_list = []
    for image in all_images:
        i += 1
        print (str(y+1) + "-" + str(i) + "." + image.get("data-src"))
        images_list.append(image.get("data-src"))
    os.mkdir(manga_name+"/"+"chapter"+str(y+1))
    for index, img_link in enumerate(images_list):
        if j<i:
            img_data = requests.get(img_link).content
            with open(manga_name+"/"+"chapter"+str(y+1)+"/"+"page"+str(index+1)+".jpg", "wb+") as f:
                f.write(img_data)
            j+=1
        else:
            f.close()
            break
    y += 1