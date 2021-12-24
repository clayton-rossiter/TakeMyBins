from dataclasses import dataclass
from datetime import datetime


@dataclass
class ScrapeResult:
    '''class to hold the individual values of each bin and its details'''
    bin_type: str
    bin_colour: str
    collection_days: list[str]
    datetime_parser: str = "%A %d %b %Y"
    datetime_format = "%Y-%m-%d"

    @property
    def table_row(self) -> list[str]:
        """returns table row entry for prettytable for next collection day only"""
        return [self.bin_type, self.bin_colour, self.collection_days[0]]

    def parse_collection_days(self) -> list[str]:
        '''takes raw collection days and parses into flutter friendly format'''
        return [datetime.strptime(collection_day, self.datetime_parser).strftime(self.datetime_format) for collection_day in self.collection_days]


def expand_for_json(results: list[ScrapeResult]) -> list[dict]:
    '''takes existing results and expands based on collection_days'''
    expanded_results = [{
        'bin_type': result.bin_type,
        'bin_colour': result.bin_colour,
        'collection_day': collection_day
    } for result in results for collection_day in result.parse_collection_days()]
    return expanded_results

