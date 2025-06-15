from langchain.tools import Tool
from scrape_amazon import scrape_amazon_deals
from scrape_daraz import scrape_daraz_deals
from scrape_ebay import scrape_ebay_deals


def aggregate_and_rank(keyword):
    results = []
    results.extend(scrape_amazon_deals(keyword))
    results.extend(scrape_daraz_deals(keyword))
    results.extend(scrape_ebay_deals(keyword))
    
    results = [d for d in results if d.get("price") is not None]
    
    ranked = sorted(results, key=lambda x: x["price"])
    
    return ranked[:10]



amazon_tool = Tool(
    name="Amazon Scraper",
    description="Scrapes Amazon for product deals based on search keywords.",
    func=scrape_amazon_deals,
)

daraz_tool = Tool(
    name="Daraz Scraper",
    description="Scrapes Daraz for product deals based on search keywords.",
    func=scrape_daraz_deals,
)

ebay_tool = Tool(
    name="eBay Scraper",
    description="Scrapes eBay for product deals based on search keywords.",
    func=scrape_ebay_deals,
)


# aggration tools
aggregate_tool = Tool(
    name="Aggregate Deal Finder",
    description="Aggregates product deals from Amazon, Daraz, and eBay, then ranks them by price.",
    func=aggregate_and_rank,
)