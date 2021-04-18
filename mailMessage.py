from __future__ import print_function
import os.path
from googleapiclient import errors
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from email.mime.text import MIMEText
import base64



class Email: 
    def __init__(self,mailTo,flights):
        self.mailTo = mailTo
        self.flights = flights

    def create_message(self):
        flights_info = 'Voos:\n '
        for flight in self.flights:
            flights_info += (f'Companhia: {flight[0]}'
                        f'\nParadas: {flight[1]}'    
                        f'\nPreço: R${flight[2]:.2f}'
                        f'\nData da consulta: {flight[3]}\n')
        message_text =( f'Verifiquei que os seguintes voos estão com um preço bom:'
                        f'\n{flights_info}'
                        '\nPode dar uma olhada no site: https://www.google.com/travel/flights')
        print(message_text)
        myMail = 'email'    # sender email
        message = MIMEText(message_text)
        message['to'] = self.mailTo
        message['from'] = myMail
        message['subject'] = 'O preço das passagens parece ter abaixado.'
        raw=base64.urlsafe_b64encode(message.as_bytes()).decode()
        return {'raw':raw}

    

    def authorization(self):
        SCOPES = 'https://www.googleapis.com/auth/gmail.send'

        creds = None
        if os.path.exists('token.json'):
            creds = Credentials.from_authorized_user_file('token.json', SCOPES)

        if not creds or not creds.valid:
            if creds and creds.expired and creds.refresh_token:
                creds.refresh(Request())
            else:
                flow = InstalledAppFlow.from_client_secrets_file('credentials.json', SCOPES)
                creds = flow.run_local_server(port = 0 )
            with open ('token.json', 'w') as token :
                token.write(creds.to_json())
        service = build('gmail', 'v1', credentials = creds)
        return service


    def send_message(self):
        service = self.authorization()
        try:
            message = (service.users().messages().send(userId='me',body = self.create_message()).execute())
            print(f'Email enviado.')
            return message
        except errors.HttpError as error:
            print(f'An error occurred: {error} ')

