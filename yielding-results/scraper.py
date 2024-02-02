import requests
from selectolax.parser import HTMLParser


def make_request(url):
    resp = requests.get(url)
    return HTMLParser(resp.text)


def parse(books):
    return [
        {
            "title": book.css_first("h3 > a").attrs["title"],
            "price": book.css_first("p.price_color").text(),
        }
        for book in books.css("article.product_pod")
    ]


def next_page(books):
    try:
        return (
            "https://books.toscrape.com/catalogue/"
            + books.css_first("li.next a").attrs["href"]
        )
    except:
        return None


def main():
    url = "https://books.toscrape.com/catalogue/page-1.html"
    while True:
        print(url)
        scraped_data = make_request(url)
        print(parse(scraped_data))
        url = next_page(scraped_data)
        if url is None:
            break


if __name__ == "__main__":
    main()
