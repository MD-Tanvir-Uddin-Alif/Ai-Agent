import requests
from bs4 import BeautifulSoup
import re

HEADERS = {
    "User-Agent": "Mozilla/5.0",
    "Accept-Language": "en-US,en;q=0.9",
}
def clean_price(price_str):
    return float(re.sub(r'[^\d.]', '', price_str)) if price_str else None



def scrape_daraz_deals(keyword: str, max_results=5):
    query = keyword.replace(" ", "+")
    url = f"https://www.daraz.com.bd/catalog/?q={query}"
    
    response = requests.get(url, headers=HEADERS)
    soup = BeautifulSoup(response.text, 'html.parser')
    
    cards = soup.select("div[data-qa-locator='product-item']")
    deals = []
    for card in cards[:max_results]:
        title = card.select_one("div[data-qa-locator='product-item'] a")
        price = card.select_one(".currency-format")
        link = card.select_one("a")["href"]

        if title and price and link:
            deals.append({
                "site": "Daraz",
                "title": title.text.strip(),
                "price": float(price.text.strip().replace("৳", "").replace(",", "")),
                "rating": "N/A", 
                "link": f"https:{link}"
            })
    return deals