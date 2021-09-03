import urllib.request as urllib2
import urllib.error
import bs4

headers = {'User-Agent': 'XYZ/8.0'}

url_wunder = "https://wunder.com.tr/sneaker?limit=10000"
url_nike = "https://www.nike.com/tr/launch"
url_sneaks_up = "https://www.sneaksup.com/sneaker?pagenumber=1"

request_wunder = urllib2.Request(url_wunder, None, headers=headers)
request_nike = urllib2.Request(url_nike, None, headers=headers)
request_sneaks_up = urllib2.Request(url_sneaks_up, None, headers=headers)

def getWunder(request:urllib2.Request):
    data = urllib2.urlopen(request).read()
    dosya = open("data.txt", "w")

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
            elif discount.strip() == "TÜKENDİ":
                print(discount.strip(), file = dosya)
            else:
                print(f"{discount.strip()} İNDİRİM", file = dosya)
        brand = i.find('p').find('span').find('strong')
        name = i.find('span', attrs= {'class' : 'font-size-16'})
        price = i.find('p', attrs = {'class' : 'product-item-price'})
        price_new = price.find('span', attrs = {'class' : 'price-new'})
        if price_new != None:
            print(price_new.text.strip(), file = dosya)
        else:
            print(price.text.replace(' ', '').replace('\\n', '').strip(), file = dosya)
        print(brand.text.strip(), file = dosya)
        print(name.text.replace('\\', '').replace("''", '"').strip(), file = dosya)
        print(file = dosya)
    dosya.close()

def getNike(request:urllib2.Request):
    for _ in range(10):
        try:
            data = urllib2.urlopen(request).read()
            break
        except urllib.error.URLError:
            continue
    f = open("html.html", "w")
    print(data, file = f)

    f = open("html.html", "r")
    data = f.read()
    data = bs4.BeautifulSoup(data, features="html.parser")
    data = data.find_all('span')
    for i in data:
        print(i.text)
    # print(len(data.text))

def getSneaksUp(request:urllib2.Request):
    # for _ in range(10):
    #     try:
    #         data = urllib2.urlopen(request).read()
    #         break
    #     except urllib.error.URLError:
    #         continue
    # f = open("html.html", "w")
    # print(data, file = f)

    f = open("html.html", "r")
    data = f.read()
    data = bs4.BeautifulSoup(data, features="html.parser")
    data = data.find('ul', attrs={'class' : 'no-list footer-menu-link-group'})
    data = data.find_all('li', attrs={'class' : 'd-block'})
    
    links = []
    for i in data:
        i = i.find('a')
        i = i.get('href')
        links.append(i)
    for i in range(len(links)):
        link = f"https://www.sneaksup.com{links[i]}?pagenumber=1"
        links[i] = link
    
    datas = []
    for i in links:
        request = urllib2.Request(i, None, headers=headers)
        for _ in range(10):
            try:
                data = urllib2.urlopen(request).read()
                break
            except urllib.error.URLError:
                continue
        datas.append(data)
    for i in datas:
        pass












# getWunder(request_wunder)
# getNike(request_nike) ### NOT WORKING !
getSneaksUp(request_sneaks_up)