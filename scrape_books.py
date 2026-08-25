"""
CodeAlpha - Task 1: Web Scraping
Scrapes book data (title, price, rating, availability) from
books.toscrape.com — a site built specifically for scraping practice.

Run locally:
    pip install requests beautifulsoup4 pandas
    python scrape_books.py
"""

import requests
from bs4 import BeautifulSoup
import pandas as pd
import time

BASE_URL = "http://books.toscrape.com/catalogue/page-{}.html"
HEADERS = {"User-Agent": "Mozilla/5.0 (educational scraping project)"}

RATING_MAP = {
    "One": 1, "Two": 2, "Three": 3, "Four": 4, "Five": 5
}


def scrape_page(page_num: int) -> list[dict]:
    """Scrape a single catalogue page and return a list of book dicts."""
    url = BASE_URL.format(page_num)
    response = requests.get(url, headers=HEADERS, timeout=10)
    response.encoding = "utf-8"

    if response.status_code != 200:
        return []

    soup = BeautifulSoup(response.text, "html.parser")
    books = soup.find_all("article", class_="product_pod")

    page_data = []
    for book in books:
        title = book.h3.a["title"]

        price_text = book.find("p", class_="price_color").text
        price_digits = "".join(c for c in price_text if c.isdigit() or c == ".")
        price = float(price_digits)

        rating_class = book.find("p", class_="star-rating")["class"]
        rating_word = [c for c in rating_class if c != "star-rating"][0]
        rating = RATING_MAP.get(rating_word, None)

        availability = book.find("p", class_="instock availability").text.strip()
        in_stock = "In stock" in availability

        page_data.append({
            "title": title,
            "price_gbp": price,
            "rating": rating,
            "in_stock": in_stock,
        })

    return page_data


def scrape_all(max_pages: int = 50) -> pd.DataFrame:
    """Scrape all catalogue pages until an empty page is hit."""
    all_books = []

    for page in range(1, max_pages + 1):
        page_data = scrape_page(page)
        if not page_data:
            print(f"Stopped at page {page} (no more books).")
            break

        all_books.extend(page_data)
        print(f"Scraped page {page}: {len(page_data)} books")
        time.sleep(0.5)  # be polite to the server

    return pd.DataFrame(all_books)


if __name__ == "__main__":
    df = scrape_all()
    df.to_csv("books_data.csv", index=False)
    print(f"\nDone. Saved {len(df)} books to books_data.csv")
    print(df.head())