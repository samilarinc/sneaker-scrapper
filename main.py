import urllib.request as urllib2
import bs4
from os import system

user_agent = 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.0.7) Gecko/2009021910 Firefox/3.0.7'

url1 = "https://wunder.com.tr/sneaker?limit=10000"
headers={'User-Agent':user_agent,} 

request = urllib2.Request(url1, None, headers)

data = urllib2.urlopen(request).read()
f = open("html.html", "w")
print(data, file = f)
f.close()
dosya = open("data.txt", "w")

with open("html.html", "r") as f:
    data = f.read()

x = bs4.BeautifulSoup(data, features="html.parser")
x = x.find('div', attrs = {'class' : 'content-wrapper'})
x = x.find('div', attrs = {'class' : 'content'})
x = x.find('div', attrs = {'class' : 'row product-layout-category product-layout-grid'})
x = x.find_all('div', attrs = {'class' : 'product-col wow fadeIn'})
for i in x:
    i = i.find('a')
    discount = i.find('div', attrs = {'class' : 'product-item-discount'})
    i = i.find('div', attrs = {'class' : 'product-item-desc'})
    if discount != None:
        discount = discount.find('svg').find('text').find('tspan').text.replace('\\n', '').strip()
        if discount.find('\\xc3\\x9c') != -1:
            print("TUKENDI", file = dosya)
        else:
            print(discount, file = dosya)
    brand = i.find('p').find('span').find('strong')
    name = i.find('span', attrs= {'class' : 'font-size-16'})
    price = i.find('p', attrs = {'class' : 'product-item-price'})
    price_new = price.find('span', attrs = {'class' : 'price-new'})
    if price_new != None:
        print(price_new.text, file = dosya)
    else:
        print(price.text.replace(' ', '').replace('\\n', ''), file = dosya)
    print(brand.text, file = dosya)
    print(name.text.replace('\\', '').replace("''", '"'), file = dosya)
    print(file = dosya)



"/html/body/div[7]/div/div[2]/div/div[3]/div[1]/a/div[2]"
"/html/body/div[7]/div/div[2]/div/div[3]/div[2]/a/div[2]"
"/html/body/div[7]/div/div[2]/div/div[3]/div[3]/a/div[2]"

# input("Press enter to finish...")
dosya.close()