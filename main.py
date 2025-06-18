import os
import requests
from dotenv import load_dotenv
from bs4 import BeautifulSoup

load_dotenv()
AMAZON_URL = "https://a.co/d/ipL3f6L"

# browser headings so Amazon won't notice that this is a bot.
just_act_normal = {
    "User-Agent": os.environ.get("MY_USER_AGENT"),
    "Accept-Language": "en-US,en;q=0.9",
}
response = requests.get(AMAZON_URL, just_act_normal)
response.raise_for_status() # Argh, status 500 again? Still getting ratted out!

# They just won't let bro cook, will they?
let_him_cook = BeautifulSoup(response.text, "html.parser")
print(let_him_cook.prettify())