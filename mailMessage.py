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
    def __init__(self,mailTo,product,price,url):
        self.mailTo = mailTo
        self.product = product
        self.price = price
        self.url = url


    def create_message(self):
        
        message_text =( f'The product: {self.product}'
                    f'\nIs available in: {self.url}'
                    f'\nFor R$ {self.price}')
        print(message_text)
        myMail = 'pricetrackerbydagnei@gmail.com'
        message = MIMEText(message_text)
        message['to'] = self.mailTo
        message['from'] = myMail
        message['subject'] = 'We tracked the price of your product. '
        return {'raw': base64.urlsafe_b64encode(message.as_string())}

    

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
            message = (service.users().messages().send(userId='me',body = self.create_message).execute())
            print(f'Message Id: {message[id]}')
            return message
        except errors.HttpError as error:
            print(f'An error occurred: {error} ')


