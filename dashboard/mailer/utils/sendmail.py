from . import oauth22 as oauth
import smtplib
import ssl
import base64
from email.message import EmailMessage
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email import policy
from random import randint
from dotenv import load_dotenv
from os import getenv

load_dotenv()

SENDER = getenv('MAIL_SENDER')
BASE_HOST = getenv('BASE_SERVER_HOST')

def get_auth_string():
    client_id = getenv('GOOGLE_CLIENT_ID')
    client_secret = getenv('GOOGLE_CLIENT_SECRET')
    refresh_token = getenv('REFRESH_TOKEN')
    
    # Generate new access token from refresh token
    token_response = oauth.RefreshToken(client_id, client_secret, refresh_token)
    access_token = token_response['access_token']
    
    # Generate Oauth2_String
    auth_string = oauth.GenerateOAuth2String(SENDER, access_token, base64_encode=False)

    return auth_string


def generate_drug_alert_email_message(receiver, drug_name, expiry_date, type='plain'):
    """
        Args:
            drug_name (String): The name of the drug
            expiry_date (String): The date the drug will expire
            type (String): value can be one of {'html', 'plain'} indicating the email be sent as html or plain text
            
        Returns: 
            composed mail message object 
    """
    content = ''
    if type == 'plain':
        content = f"The drug {drug_name} is expiring on {expiry_date}."
    elif type=='html':
        content = f"""
            <html lang="en">
            <head></head>
            <body>
                <h3> Expiry Alert for {drug_name} </h3>
                <div style="background-color: rgb(2, 6, 28); margin:5px; color:whitesmoke; font-size:1em; padding: 5px 10px; border-radius:3px">
                    The drug {drug_name} is expiring on {expiry_date}.
                </div>
            </body>
            </html>
        """

    message = MIMEText(content, 'html') if type=='html' else MIMEText(content, 'plain')
    message['From'] = SENDER
    message['To'] = receiver
    message['Subject'] = f'Expiry Alert for {drug_name}'

    return message


def send_drug_expiry_email_alert(receiver, drug_name, expiry_date, type='plain'):
    # try:
    OAUTH_STRING = get_auth_string()
    content_type = 'plain' if type != 'html' else type
    message = generate_drug_alert_email_message(
                    receiver, 
                    drug_name=drug_name, 
                    expiry_date=expiry_date, 
                    type=content_type)

    with smtplib.SMTP_SSL('smtp.gmail.com', context=ssl.create_default_context()) as server:
        # server.set_debuglevel(True)
        server.ehlo('test')
        server.docmd('AUTH', 'XOAUTH2 ' + base64.b64encode(OAUTH_STRING.encode('utf-8')).decode('utf-8'))

        server.sendmail(SENDER, receiver, message.as_string())
        print('Message sent.')
        return {
            'success':True,
            'message':f'Password reset link sent to {receiver}.'
        }

    # except Exception as ex:
    #     print(ex)
    #     return {
    #         'success':False,
    #         'message':f'Error sending password reset link to email, failed. Reason: {ex}'
    #     }

    
# otp = str(randint(100000, 999999))
# receiver = 'adeyemi.sa1@gmail.com'

# response = send_otp_to_mail(receiver, otp, type='html')
# print(response)
