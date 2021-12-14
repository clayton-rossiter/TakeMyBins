from prettytable import PrettyTable

from TMB.result import ScrapeResult


def display_as_prettytable(results: list[ScrapeResult], headers: list[str]=["Bin Type", "Bin Colour","Next Collection"]):
    '''takes list of scrape results and displays as a prettytable'''
    if len(headers) != 3:
        raise ValueError("The headers should contain 3 values as a list!")
    t = PrettyTable()
    t.field_names = headers
    for result in results:
        t.add_row(result.table_row)
    print(t)