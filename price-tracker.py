import requests
import bs4
import smtplib
from email.message import Email
from flights import flights_info
from db import data_toSQL
import time



#Get the information about the flights and store in a list.

url = 'https://www.google.com/travel/flights'
while True:
    try:
        flights = flights_info(url)
        flights.get_source_code()
        flights.get_info()
        info = flights.info
        break
    except:
        print('An error occurred, trying again.')
        time.sleep(1)

print(info)
for flight in info:
    print('==========================')
    print(f'Companhia: {flight[0]}'
        f'\nParadas: {flight[1]}'
        f'\nPreço: R${flight[2]:.2f}'
        f'\nData da consulta: {flight[3]}')
    airline = flight[0]
    stopOvers= flight[1]
    price = flight[2]
    dt = flight[3]


    data = data_toSQL(airline,dt,stopOvers,price)
    data.insert()
    good_price = []
    if price < 0.90*data.mean_price() or price < 3000:
        good_price.append(flight)

if len(good_price) > 0 :
    #Send email
    email = Email('email',good_price)
    email.create_message()
    email.send_message()
