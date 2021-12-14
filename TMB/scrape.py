from bs4 import BeautifulSoup
from bs4.element import Tag
import requests

from TMB.result import ScrapeResult


class Scraper:
    URL:str = r"https://www.adur-worthing.gov.uk/bin-day/?brlu-selected-address=100061879527&return-url=%2Fbin-day%2F"

    def scrape(self) -> list[ScrapeResult]:
        """scrapes the table data from the council website"""
        r = requests.get(self.URL)
        if r.status_code != 200:
            raise ValueError("Could not access website")
        soup = BeautifulSoup(r.text, "lxml")
        table = soup.find_all('table')[0]

        # loop through table rows and generate data
        rows = table.find_all('tr')
        results = [parse_row(row) for row in rows[1:-1]]
        return results
            

def parse_row(row: Tag) -> ScrapeResult:
    """parses a row from the master table to retrieve the bin collection information"""
    bin_type = row.find_all('th')[0].text
    eles = row.find_all('td')
    bin_colour = eles[0].text.strip()
    collection_days = [str(ele) for ele in eles[1].contents if not isinstance(ele,Tag)]
    return ScrapeResult(bin_type, bin_colour, collection_days)
