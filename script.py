from bs4 import BeautifulSoup
import requests
import time
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import json


url = 'https://www.ssense.com/en-us/men/product/balenciaga/black-campaign-hoodie/3357139'


def readFile():
    with open('creditental.txt') as json_file:
        data = json.load(json_file)
    return data

def sendMessage(text):
    info = readFile()

    email = info["email"]
    pas = info["password"]

    sms_gateway = info["sms_gateway"]

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
    inStock = False
    page = requests.get(url)

    soup = BeautifulSoup(page.content, 'html.parser')

    sizes = soup.find_all('option')

    for size in sizes[1:]:
        s = size.text.strip()
        if ("Sold Out" not in s) and (inputSize.upper() == s.split()[0]):
            # sendMessage("check out at https://www.ssense.com/en-us/men/product/balenciaga/black-campaign-hoodie/3357139")
            inStock = True    
            print("Text sent", time.ctime())
            return inStock
    print("Size not yet in stock", time.ctime())
    return inStock

def run():
    size = input("Enter size (e.g. s or S for small): ")
    while True:
        if getSizes(size) == True:
            break
        time.sleep(1)


if __name__ == '__main__':
   run()
    
