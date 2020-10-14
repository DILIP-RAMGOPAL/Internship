from bs4 import *
import requests as rq
import os
r2=rq.get("https://www.indiaglitz.com/aamir-khan-photos-hindi-actor-2738542-7950")
soup=BeautifulSoup(r2.text,"html.parser")
link=[]
x=soup.select('img[src^="https://1847884116.rsc.cdn77.org/hindi/gallery/actor/aamirkhan/"]')
for img in x:
    link.append(img['src'])
os.mkdir("aamirkhan")
i=1
for img_link in link:
    img_data=rq.get(img_link).content
    with open("aamirkhan/"+str(i)+".jpeg",'wb+') as f:
        f.write(img_data)
    i+=1
print("Transfered ",i-1," images")

