import requests
from bs4 import BeautifulSoup
import re

HEADERS = {
    "User-Agent": "Mozilla/5.0",
    "Accept-Language": "en-US,en;q=0.9",
}
def clean_price(price_str):
    return float(re.sub(r'[^\d.]', '', price_str)) if price_str else None


def scrape_ebay_deals(keyword: str, max_results=5):
    query = keyword.replace(" ", "+")
    url = f"https://www.ebay.com/sch/i.html?_nkw={query}"
    headers = {"User-Agent": "Mozilla/5.0"}

    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, "html.parser")
    cards = soup.select(".s-item")

    deals = []
    for card in cards[:max_results]:
        title_el = card.select_one(".s-item__title")
        price_el = card.select_one(".s-item__price")
        link_el = card.select_one("a.s-item__link")

        if title_el and price_el and link_el:
            deals.append({
                "site": "eBay",
                "title": title_el.text.strip(),
                "price": clean_price(price_el.text),
                "rating": "N/A",
                "link": link_el["href"]
            })
    return deals 