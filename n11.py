import requests
from bs4 import BeautifulSoup

url = "https://www.trendyol.com/cep-telefonu-x-c103498?pi=4"
#url = "https://www.n11.com/bilgisayar/dizustu-bilgisayar?ipg=1"
count=1

html = requests.get(url).content
soup = BeautifulSoup(html, "html.parser")

list = soup.find_all("div", {"class": "p-card-wrppr with-campaign-view"},limit=100)

for div in list:
  name1 = div.a.find("span", {"class": "prdct-desc-cntnr-name hasRatings"}).text
  name2 = div.a.find("span", {"class": "prdct-desc-cntnr-ttl"}).text
  name3 = name2+" "+name1
  link = "https://www.trendyol.com/" + div.a.get("href")
  oldprice = div.a.find("div",{"class":"prc-box-orgnl"})
  price = div.a.find("div", {"class":"prc-box-dscntd"}).text
  print(f"{count}-{name2} markalı {name1} modelin fiyatı {price}'dir. Link: {link}")
  count+=1

