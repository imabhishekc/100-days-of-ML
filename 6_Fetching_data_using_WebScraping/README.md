# Books to Scrape - Web Scraping Demo

This project demonstrates how to scrape data from the [Books to Scrape](http://books.toscrape.com/) website using Python and BeautifulSoup.

> ⚠️ This site is built specifically for practicing web scraping — no real products or sensitive data involved.

---

## Features

This scraper collects the following data for books listed on the site:

- ✅ Title
- ✅ Price
- ✅ Star Rating
- ✅ Genre *(from the book's detail page)*

The demo scrapes data from the **first 2 pages** (40 books in total) and saves it to a clean CSV file.

---

## Tools Used

- `requests` – For sending HTTP requests  
- `BeautifulSoup` – For parsing HTML and extracting data  
- `pandas` – For creating a DataFrame and saving to CSV

---

## Output Sample

| Title                    | Price | Rating | Genre              |
|--------------------------|-------|--------|--------------------|
| A Light in the Attic     | 51.77 | 3      | Poetry             |
| Tipping the Velvet       | 53.74 | 1      | Historical Fiction |
