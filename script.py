from bs4 import BeautifulSoup
import requests
import time
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import json


def loadCarrier():
    with open('carrier.txt') as carrier_file:
        carriers = json.load(carrier_file)
    return carriers


def loadJSON():
    with open('credential_wei.txt') as json_file:
        data = json.load(json_file)
    return data

def sendMessage(text, carrier):
    info = loadJSON()
    carriers = loadCarrier()

    email = info["email"]
    pas = info["password"]
    sms_gateway = "{}{}".format(info["phone"], carriers[carrier])

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

def getSizes(inputSize, url, carrier):
    inStock = False
    page = requests.get(url)

    soup = BeautifulSoup(page.content, 'html.parser')

    sizes = soup.find_all('option')

    for size in sizes[1:]:
        s = size.text.strip()
        if ("Sold Out" not in s) and (inputSize.upper() == s.split()[0]):
            sendMessage("check out at: " + url, carrier)
            inStock = True    
            print("Text sent", time.ctime())
            return inStock
    print("Size not yet in stock", time.ctime())
    soup.decompose()
    return inStock

def run():
    carrier = input("What is your carrier (e.g AT&T as att): ").lower()
    url = input("Enter url of item you want to monitor: ")
    size = input("Enter size (e.g. s or S for small): ")
    while True:
        if getSizes(size, url, carrier) == True:
            break
        time.sleep(2)


if __name__ == '__main__':
   run()

    
