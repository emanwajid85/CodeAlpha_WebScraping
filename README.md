# CodeAlpha_WebScraping

## Task
Web Scraping — CodeAlpha Data Analytics Internship (Task 1)

## Overview
This project scrapes book data (title, price, star rating, stock status) from
[books.toscrape.com](http://books.toscrape.com), a site purpose-built for
scraping practice. The script pages through the full catalogue and saves the
results to a CSV for further analysis.

## What it does
- Extracts **title**, **price (GBP)**, **star rating (1–5)**, and **stock status**
  for every book in the catalogue
- Automatically pages through the site until no more books are found
- Saves the collected data to `books_data.csv`
- Includes a small delay between requests to be respectful of the server

## How to run
```bash
pip install requests beautifulsoup4 pandas
python scrape_books.py
```

Output: `books_data.csv` with one row per book.

## Tech used
- `requests` — fetch page HTML
- `BeautifulSoup` — parse and extract data from HTML
- `pandas` — structure and export the scraped data

## Next steps
This dataset feeds directly into the EDA and Data Visualization tasks —
e.g. price distribution by rating, how many books are in/out of stock,
average price per rating tier.
