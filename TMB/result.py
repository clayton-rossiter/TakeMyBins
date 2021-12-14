from dataclasses import dataclass



@dataclass
class ScrapeResult:
    '''class to hold the individual values of each bin and its details'''
    bin_type: str
    bin_colour: str
    collection_days: list[str]

    @property
    def table_row(self) -> list[str]:
        """returns table row entry for prettytable"""
        return [self.bin_type, self.bin_colour, self.collection_days[0]]

