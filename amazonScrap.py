from concurrent.futures import ThreadPoolExecutor

from bs4 import BeautifulSoup
from pandas import DataFrame
import cloudscraper

# List of scraped articles
list = []

def get_articles(research, page):
    research = research.replace(" ", "+")
    url = "https://www.amazon.fr/s?k=" + research + "&page=" + page + "&crid=243EN552MY0KK&qid=1682490983&sprefix=playstation+5%2Caps%2C232&ref=sr_pg_" + page

    scraper = cloudscraper.create_scraper(delay=5)
    header = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/112.0'}
    r = scraper.get(url, headers=header)
    soup = BeautifulSoup(r.text, 'html.parser')
    container = soup.find_all('div', class_="sg-col-inner")

    for res in container:
        title = res.find('span', class_="a-size-base-plus a-color-base a-text-normal")
        if title is not None and title.text != "":
            title = title.text
            link = "https://www.amazon.fr" + res.find('a', class_="a-link-normal s-underline-text s-underline-link-text s-link-style a-text-normal")['href']
            price = res.find('span', class_="a-offscreen")
            if price is not None:
                price = price.text
            else:
                price = "No price found"
            rating = res.find('span', class_="a-icon-alt")
            if rating is not None:
                rating = rating.text
            else:
                rating = "No rating found"
            numberOfRates = res.find('span', class_="a-size-base s-underline-text")
            if numberOfRates is not None:
                numberOfRates = numberOfRates.text
            else:
                numberOfRates = "No number of rates found"

            list.append([title, link, price, rating, numberOfRates])


def launch_scraping():
    # Get the research and the number of pages to scrap
    research = input("What do you want to research? ")
    no_pages = int(input("How many pages do you want to scrap? "))

    # Scrap the articles
    for i in range(1, no_pages + 1):
        with ThreadPoolExecutor(max_workers=8) as executor:
            executor.submit(get_articles, research, str(i))

    # Create the csv file
    pf = DataFrame(list, columns=['Title', 'Link', 'Price', 'Rating', 'Number of rates'])
    pf.to_csv('AmazonArticles.csv', index=False, encoding='utf-8')

    print("Scraping done! (AmazonArticles.csv created)")

if __name__ == "__main__":
    launch_scraping()
