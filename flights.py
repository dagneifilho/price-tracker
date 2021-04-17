from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from datetime import date
import time
from bs4 import BeautifulSoup

#pay attention to the path and download the right google chrome driver for your OS
class flights_info:
	def __init__(self,url):
		self.url = url
		

	def get_source_code(self): 
		
	
		driver = webdriver.Chrome(executable_path = 'C:/Users/Pichau/Desktop/projects/price-tracker/chromedriver.exe')
		driver.get(self.url)
		input_box1 = driver.find_element_by_xpath('//*[@id="i6"]/div[4]/div/div/div[1]/div/div/input')
		input_box1.send_keys('O')
		input_box2 = driver.find_element_by_xpath('//*[@id="i6"]/div[6]/div[2]/div[2]/div[1]/div/input')
		input_box2.send_keys('rlando' + Keys.ENTER)
		search_button = driver.find_element_by_xpath('//*[@id="yDmH0d"]/c-wiz[2]/div/div[2]/div/c-wiz/div/c-wiz/div[2]/div[1]/div[2]/div/button')
		time.sleep(1)
		search_button.click()
		time.sleep(3)
		source = driver.page_source
		
		self.url_for_scraping = driver.current_url
		self.source = source
		driver.quit()
		

	def get_info(self):
		soup = BeautifulSoup(self.source, 'html.parser')
		best_flights = soup.find('div',{'jsname' : 'AqkRyc'})
		best_flights = best_flights.find_all('div',{'class':'mz0jqb taHBqe Qpcsfe'})
		other_flights = soup.find()
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
			dt = date.today()
			info.append([airline, stopovers, price, dt])

		self.info = info
	
