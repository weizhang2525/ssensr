from bs4 import BeautifulSoup
import requests
import time
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart



url = 'https://www.ssense.com/en-us/men/product/balenciaga/black-campaign-hoodie/3357139'

def sendMessage(text):
    smtp = "smtp.gmail.com"
    port = 587
    server = smtplib.SMTP(smtp, port)

    server.starttls()
    server.login(email, pas)

    msg = MIMEMultipart()

    msg['From'] = email
    msg['To'] = sms_gateway

    msg['Subject'] = "Item in stock!!"

    body = text

    msg.attach(MIMEText(body, 'plain'))

    sms = msg.as_string()

    server.sendmail(email, sms_gateway, sms)

    server.quit()

def getSizes(inputSize):
    page = requests.get(url)

    soup = BeautifulSoup(page.content, 'html.parser')

    sizes = soup.find_all('option')

    while True:
        for size in sizes[1:]:
            s = size.text.strip()
            if ("Sold Out" not in s) and (inputSize.upper() == s.split()[0]):
                sendMessage("check out at https://www.ssense.com/en-us/men/product/balenciaga/black-campaign-hoodie/3357139")
                break   
        break


if __name__ == '__main__':
    # print(time.ctime())
    size = input("Enter size (e.g. s or S for small): ")
    getSizes(size)
    # sendMessage()
    
