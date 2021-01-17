import requests
from bs4 import BeautifulSoup
import smtplib
import time
items = [] #Enter items in a list with the original price, example: items = [["https://www.amazon.ca/AMD-Ryzen-3600-12-thread-processor/dp/B07STGGQ18", 330.00]]

#Enter in your user agent by going to google and searching: "my user agent." Replace your user agent after the "User-Agent":
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36"}

def checkPrice():
    #function that will check the price of the items in the items list
    page = requests.get(URL, headers=headers)

    soup = BeautifulSoup(page.content, 'html.parser')

    title = soup.find(id="productTitle").get_text()
    print("Checking price for " + title.strip())
    price = soup.find(id="priceblock_ourprice").get_text()

    if(origPrice > 100):
    
        conv_price = float(price[1:7])
    else:
        conv_price = float(price[1:6])

    print("Original Price {}\n Current Price: {}".format(origPrice, conv_price))

    if(conv_price < origPrice):
        print("Price dropped!")
        sendMail(title.strip(), URL, origPrice, conv_price)
    else:
        print("No difference")


def sendMail(title, URL, original, new):
    #function to send the email alert of updated price
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    password = "PASSWORD HERE"
    email = "TYPE IN EMAIL HERE"
    server.login(email, password) 

    subject = f"Price dropped for {title}"

    body = f"Old Price: {original}\nNew Price: {new}\nDifference: {original - new}\n{URL}"

    msg = f"Subject: {subject}\n\n{body}"

    server.sendmail(
        email,
        email,
        msg
    )
    print("Sent email")

    server.quit()
    
while True:
    #Program changed to only run every 24 hours/ 86400 seconds
    print("============================================================================================")
    for i in items:
        URL = i[0]
        origPrice = i[1]
        checkPrice()
    time.sleep(86400) #change the frequency of emails here