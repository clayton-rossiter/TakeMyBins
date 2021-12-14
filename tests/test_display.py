import unittest

from TMB.result import ScrapeResult
from TMB.display import display_as_prettytable


class TestResultsPrettyTable(unittest.TestCase):

    def setUp(self) -> None:
        self.result_recycling = ScrapeResult(bin_type='Recycling', bin_colour='Blue', collection_days=['Friday 17 December 2021'])
        self.result_refuse = ScrapeResult(bin_type='Refuse', bin_colour='Grey', collection_days=['Friday 24 December 2021'])
        self.results = [self.result_recycling, self.result_refuse]
        self.headers = ["Bin Type", "Bin Colour","Next Collection"]
    
    def test_normal_operation(self):
        '''test no faults are raised when'''
        display_as_prettytable(self.results)

    def test_raises_fault_if_incorrect_number_of_headers_provided(self):
        '''raises exception if number of headers is not 3'''
        with self.assertRaises(ValueError):
            display_as_prettytable(self.results, self.headers[:-1])