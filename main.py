from TMB.scrape import Scraper
from TMB.display import display_as_local_flask_api, display_as_prettytable


def main():
    scraper = Scraper()
    results = scraper.scrape()
    # display_as_prettytable(results)
    display_as_local_flask_api(results)


if __name__ == '__main__':
    main()