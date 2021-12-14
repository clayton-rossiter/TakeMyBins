import unittest
from requests.exceptions import MissingSchema

from TMB.scrape import Scraper
from TMB.result import ScrapeResult


class TestResults(unittest.TestCase):
    
    def test_works_as_normal(self):
        '''tests for normal functionality'''
        scraper = Scraper()
        results = scraper.scrape()
        self.assertIsInstance(results, list)
        self.assertTrue(len(results), 3)

        result = results[0]
        self.assertIsInstance(result, ScrapeResult)

    def test_raises_fault_if_url_schema_is_incorrect(self):
        '''test raises exception if url is not correct schema'''
        scraper = Scraper()
        scraper.URL = 'test'
        with self.assertRaises(MissingSchema):
            scraper.scrape()

    def test_raises_fault_if_url_status_code_is_not_200(self):
        '''test raises exception is url schema is correct but site in unreachable'''
        url_404 = r'https://google.com/clayton'
        scraper = Scraper()
        scraper.URL = url_404
        with self.assertRaises(ValueError):
            scraper.scrape()