import click
import requests
from bs4 import BeautifulSoup
from dataclasses import dataclass
from rich import print


@dataclass
class Podcast:
    title: str
    link: str
    desc: str
    date: str


def get_data(feed_url):
    resp = requests.get(feed_url)
    return BeautifulSoup(resp.text, features="xml")


def parse_xml(soup):
    item = soup.find("item")
    return Podcast(
        title=item.find("title").text,
        link=item.find("enclosure")["url"],
        desc=item.find("description").text,
        date=item.find("pubDate").text,
    )


@click.command()
@click.argument("feed_url")
def scrape(feed_url):
    pod = get_data(feed_url)
    ep = parse_xml(pod)
    print(ep)


if __name__ == "__main__":
    scrape()
