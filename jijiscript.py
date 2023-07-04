import requests
from bs4 import BeautifulSoup as soup
url = "https://jiji.ng/jobs"
webpage = requests.get(url)
Soup = soup(webpage.content,"html.parser")
jobs = Soup.findAll("div",{"class":"b-list-advert-base__data__title"})
jobtype = Soup.findAll("div",{"class":"b-list-advert-base__item-attr"})
salary = Soup.findAll("div",{"class":"qa-advert-price"})
#print(f"{salary[0].text.strip()}\n{jobs[0].text.strip()}\n{jobtype[0].text.strip()}")
count=0
for i,j,k in zip(jobs,jobtype,salary):
    count+=1
    print(count,"\n",i.text.strip() ,"\n",j.text.strip(),"\n",k.text.strip())
