import requests
from bs4 import BeautifulSoup
import re

HEADERS = {
    "User-Agent": "Mozilla/5.0",
    "Accept-Language": "en-US,en;q=0.9",
}
def clean_price(price_str):
    return float(re.sub(r'[^\d.]', '', price_str)) if price_str else None


def scrape_amazon_deals(keyword: str, max_results=5):
    query = "+".join(keyword.split())
    url = f"https://www.amazon.com/s?k={query}"
    
    responce = requests.get(url, headers=HEADERS)
    soup = BeautifulSoup(responce.text, 'html.parser')
    results = soup.select('div.s-main-slot div[data-component-type="s-search-result"]')
    
    deals = []
    
    for item in results[:max_results]:
        title_el = item.select_one("h2 a span")
        price_el = item.select_one(".a-price .a-offscreen")
        rating_el = item.select_one(".a-icon-alt")
        link_el = item.select_one("h2 a")
        
        if title_el and price_el and link_el:
            deals.append({
                "site": "Amazon",
                "title": title_el.text.strip(),
                "price": clean_price(price_el.text),
                "rating": rating_el.text.strip() if rating_el else "N/A",
                "link": f"https://www.amazon.com{link_el['href']}"
            })
    return deals