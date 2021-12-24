from prettytable import PrettyTable
from flask import Flask, jsonify

from TMB.result import ScrapeResult, expand_for_json


def display_as_prettytable(results: list[ScrapeResult], headers: list[str]=["Bin Type", "Bin Colour","Next Collection"]) -> None:
    '''takes list of scrape results and displays as a prettytable'''
    if len(headers) != 3:
        raise ValueError("The headers should contain 3 values as a list!")
    t = PrettyTable()
    t.field_names = headers
    for result in results:
        t.add_row(result.table_row)
    print(t)


def display_as_local_flask_api(results: list[ScrapeResult], host: str='127.0.0.1'):
    '''takes list of scrape results and returns as jsonified API response'''
    app = Flask(__name__)

    @app.route('/')
    def get_bin_days():
        '''private function to return json response for each ScrapeResult'''
        expanded_results = expand_for_json(results)
        return jsonify(expanded_results)

    app.run(host=host)
        


