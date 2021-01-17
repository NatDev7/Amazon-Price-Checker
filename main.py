import requests
from bs4 import BeautifulSoup
import smtplib
import time
items = [] #Enter items in a list with the original price, example: items = [["https://www.amazon.ca/AMD-Ryzen-3600-12-thread-processor/dp/B07STGGQ18", 330.00]]

#Enter in your user agent by going to google and searching: "my user agent." Replace your user agent after the "User-Agent":
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36"}
