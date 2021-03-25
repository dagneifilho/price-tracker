import requests
import bs4
import smtplib
from email.message import EmailMessage

def Scraper(url):

    headers = {
        'pragma': 'no-cache',
        'cache-control': 'no-cache',
        'dnt': '1',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (X11; CrOS x86_64 8172.45.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.64 Safari/537.36',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'sec-fetch-site': 'none',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-dest': 'document',
        'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
    }
    res = requests.get(url, headers = headers)

    soup = bs4.BeautifulSoup(res.text, 'html.parser')
    if 'amazon' in url.lower():
        name = soup.find(id = 'productTitle').get_text()    
        name = name.replace('\n', '')
        price = soup.find(id = 'priceblock_ourprice').get_text()
        price = price.replace('.', '')
        price = float(price[2::].replace(',', '.'))



    elif 'submarino' in url.lower():
        name = soup.find(id = 'product-name-default').get_text()
        price = soup.find('span', class_ = 'price__SalesPrice-sc-1i11rkh-2 jjADsQ TextUI-sc-12tokcy-0 CIZtP').get_text()
        price = price.replace('.', '')
        price = float(price[3::].replace(',', '.'))
    

    product = [name, price]
    return product


url = 'https://www.amazon.com.br/Baby-doll-Renda-Gr%C3%A9cia-Promo%C3%A7%C3%A3o/dp/B084NXWDDW/ref=pd_sbs_4?pd_rd_w=0VQci&pf_rd_p=f2ff7d31-774f-476b-ad0b-255506b1ebcf&pf_rd_r=W0ZVVG5ADXWZEF8P6RCJ&pd_rd_r=0c3dec9d-1d8f-47c6-8120-7c220049d57e&pd_rd_wg=677Du&pd_rd_i=B084NV4DDN&psc=1'
#product = Scraper(url)


#print(product[0])
#print(product[1])
