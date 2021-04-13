import requests
import bs4
import smtplib
from email.message import EmailMessage
from flights import flights_info
import time


#Get the information about the flights and store in a list.

url = 'https://www.google.com/travel/flights'
flights = flights_info(url)

while True:
	try:
		flights.get_source_code()
		flights.get_info()
		info = flights.info
		break
	except:
		print('An error occurred, trying again.')
		time.sleep(4)



for flight in info:
	print('==========================')
	print(f'Companhia: {flight[0]}'
		f'\nParadas: {flight[1]}'
		f'\nPreço: R${flight[2]:.2f}'
		f'\nData da consulta: {flight[3]}')

#Store the data in a DB and compare to previous ones.
