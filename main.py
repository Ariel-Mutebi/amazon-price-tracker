import os
import smtplib
import requests
from dotenv import load_dotenv
from bs4 import BeautifulSoup

load_dotenv()
AMAZON_URL = "https://a.co/d/ipL3f6L"
MAXIMUM_PRICE_FOR_GOOD_DEAL = 50
SMTP_PORT = 587 # My ISP has blocked port 25.

just_act_normal = {
    "User-Agent": os.environ.get("MY_USER_AGENT"),
    "Accept-Language": "en-US,en;q=0.9",
}
response = requests.get(AMAZON_URL, headers=just_act_normal)
response.raise_for_status()

let_him_cook = BeautifulSoup(response.text, "html.parser")
product_title = let_him_cook.find(id="productTitle").getText().strip()
dollars = let_him_cook.find(class_="a-price-whole").getText()
cents = let_him_cook.find(class_="a-price-fraction").getText()
price_floating_point = float(dollars + cents) # this is actually string concatenation

if price_floating_point < MAXIMUM_PRICE_FOR_GOOD_DEAL:
    print("Sending email...")

    email_body = f"You can now buy {product_title} at a price of ${price_floating_point}.\nLink:{AMAZON_URL}"

    with smtplib.SMTP(os.environ.get("SMTP_HOST"), SMTP_PORT) as connection:
        connection.starttls()
        connection.login(os.environ.get("SENDER_EMAIL"), os.environ.get("APP_PASSWORD"))
        connection.sendmail(
            from_addr=os.environ.get("SENDER_EMAIL"),
            to_addrs=os.environ.get("RECIPIENT_EMAIL"),
            msg="Subject: Amazon Low Price Alert\n\n" + email_body
        )