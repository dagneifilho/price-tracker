import requests
import bs4

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
        title = soup.find(id = 'productTitle').get_text()
        subtitle = soup.find(id = 'productSubtitle').get_text()
        name = title + ' ' + subtitle
        name = name.replace('\n', '')
        price = soup.find(id = 'soldByThirdParty').get_text()
        price = price.replace('.', '')
        price = float(price[3::].replace(',', '.'))



    elif 'submarino' in url.lower():
        name = soup.find(id = 'product-name-default').get_text()
        price = soup.find('span',{'class': 'price__SalesPrice-sc-1i11rkh-2 jjADsQ TextUI-sc-12tocky-0 CIZtp'}).get_text()
        price = price.replace('.', '')
        price = float(price[3::].replace(',', '.'))
    
    """elif 'kabum' in url.lower():
        name = soup.find('h1'{'class': 'titulo_det'})
       """  
    product = [name, price]
    return product

url = 'https://www.submarino.com.br/produto/123384500/kit-livros-serie-millennium-4-volumes-1?pfm_carac=millenium%20livro&pfm_index=3&pfm_page=search&pfm_pos=grid&pfm_type=search_page'
product = Scraper(url)
print(product[0])
print(product[1])