from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from datetime import date
import time
from bs4 import BeautifulSoup

#pay attention to the path and download the right google chrome driver for your OS

def get_source_code(url): 
	driver = webdriver.Chrome(executable_path = '/home/dagnei/Documentos/projetos/price-tracker/chromedriver')
	driver.get(url)
	input_box1 = driver.find_element_by_xpath('//*[@id="i6"]/div[4]/div/div/div[1]/div/div/input')
	input_box1.send_keys('O')
	input_box2 = driver.find_element_by_xpath('//*[@id="i6"]/div[6]/div[2]/div[2]/div[1]/div/input')
	input_box2.send_keys('rlando' + Keys.ENTER)
	search_button = driver.find_element_by_xpath('//*[@id="yDmH0d"]/c-wiz[2]/div/div[2]/div/c-wiz/div/c-wiz/div[2]/div[1]/div[2]/div/button')
	search_button.click()


	time.sleep(3)
	source = driver.page_source
	return source

def get_info(source):
	soup = BeautifulSoup(source, 'html.parser')
	best_flights = soup.find('div',{'jsname' : 'AqkRyc'})
	best_flights = best_flights.find_all('div',{'class':'mz0jqb taHBqe Qpcsfe'})
	n=0
	info =[]
	for flight in best_flights:
		stopovers= flight.find('span',{'class':'pIgMWd ogfYpf'}).get_text()
		stopovers = stopovers.replace(' paradas','')
		stopovers = int(stopovers)
		price = flight.find('div',{'class':'YMlIz FpEdX jLMuyc'}).get_text()
		price = price.replace('R$','')
		price = float(price.replace('.',''))
		airline = flight.find('div',{'class':'TQqf0e sSHqwe tPgKwe ogfYpf'}).get_text()
		info.append([airline, stopovers, price])
	return info
	
	

source = get_source_code('https://www.google.com/travel/flights')
info = get_info(source)
print(info)
for flight in info:
	print('==========================')
	print(f'Companhia: {flight[0]}'
		f'\nParadas: {flight[1]}'
		f'\nPreço: R${flight[2]:.2f}')
