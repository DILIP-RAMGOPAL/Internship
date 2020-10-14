from bs4 import *
import requests as rq
import os
import shutil

#to take all data from given website 

r2=rq.get("https://www.indiaglitz.com/aamir-khan-photos-hindi-actor-2738542-7950")
soup=BeautifulSoup(r2.text,"html.parser")
link=[]

#To select images whoes source link starts with the given src 
#here to only select aamir khan images

x=soup.select('img[src^="https://1847884116.rsc.cdn77.org/hindi/gallery/actor/aamirkhan/"]')
for img in x:
    link.append(img['src'])
i=1
dir = 'aamirkhan'

#create folder named aamirkhan. also replace if folder already exist

if os.path.exists(dir):
    shutil.rmtree(dir)
os.makedirs(dir)

#to copy all downloaded images to aamirkhan folder

for img_link in link:
    img_data=rq.get(img_link).content
    with open("aamirkhan/"+str(i)+".jpeg",'wb+') as f:
        f.write(img_data)
    i+=1
print("Transfered ",i-1," images")

