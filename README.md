# ssensr

A stock monitor built for ssense.com to track when an item becomes avaliable for purchase. It uses your email address to send an email to your phone number by using its sms domain.

## Getting Started

These instructions will help you get this script running until the item is in stock or interrupted by the user.

### Prerequisites

This script requires your machine to be running on python3 with two extra modules, beautifulsoup4 and requests, to be installed. It is a lot easier to install packages with pip as it configures everything for you. I have to use pip3 since I have pip installed with python2 on my device.

https://www.crummy.com/software/BeautifulSoup/bs4/doc/
https://requests.readthedocs.io/en/master/

You will need to edit the credential.txt file with your email, password, and phone number. If your email is Gmail, you will need to make an application password through Google by following this link: https://support.google.com/accounts/answer/185833?hl=en. Make sure the fields inside the double quotes ("") are changed then save the file. Phone number field does not require a -.

```
  "email" : "myemail@gmail.com",
	"password" : "pw_from_google",
  "phone" : "1111111111"
```


### Installing

A step by step example of how you can install the required modules using pip.

```
pip install beautifulsoup4
```
then

```
pip install requests
```

A success message will display after you have installed each module correctly.

## Running

You can run this script by calling python3 in terminal or use any IDE of your choice.

```
python3 script.py
```

After running it successfully, the script will prompt you to answer a few questions regarding to what settings you would like to use. Enter in your carrier name, link to ssense's URL (starting with https://www.ssense.com), and which size you would like to monitor. You'll know that everything is configured correctly when the script prints out whether the the item is in stock. If it is out of stock, it will print out the time stamp. If it is in stock, it will text you.

## Testing
You can test whether the text is sending to the right location by entering in a valid item that is currently in stock.





