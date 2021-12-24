from flask import Flask, jsonify

from TMB.result import expand_for_json
from TMB.scrape import Scraper



'''takes list of scrape results and returns as jsonified API response'''
app = Flask(__name__)
scraper = Scraper()
results = scraper.scrape()

@app.route('/')
def get_bin_days():
    '''private function to return json response for each ScrapeResult'''
    expanded_results = expand_for_json(results)
    return jsonify(expanded_results)

if __name__ == '__main__':
    app.run()