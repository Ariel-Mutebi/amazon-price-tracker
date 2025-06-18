import os
import requests
from dotenv import load_dotenv
from bs4 import BeautifulSoup

load_dotenv()
AMAZON_URL = "https://a.co/d/ipL3f6L"

just_act_normal = {
    "User-Agent": os.environ.get("MY_USER_AGENT"),
    "Accept-Language": "en-US,en;q=0.9",
}
response = requests.get(AMAZON_URL, headers=just_act_normal)
response.raise_for_status()

let_him_cook = BeautifulSoup(response.text, "html.parser")
dollars = let_him_cook.find(class_="a-price-whole").getText()
cents = let_him_cook.find(class_="a-price-fraction").getText()
price_floating_point = float(dollars + cents) # this addition is actually string concatenation
print(price_floating_point)