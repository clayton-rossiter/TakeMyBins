# TakeMyBins

## How to run it
First clone this git repo:
```
git clone https://github.com/clayton-rossiter/TakeMyBins.git
```
then install all requirements:
```
pip install -r requirements.txt
```
Simply run the main command to receive a table in your command prompt:
```
python main.py
```

## What it does
I was a bit tired of going online to see when my next bin collection was... so I built a simple web scraper using [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/).  
The scraper takes a look at the [Worthing Council bin day collection page](https://www.adur-worthing.gov.uk/bin-day/) by using a ```requests``` text response and parses the necessary information once the address is provided.
The current possible outputs are:
- PrettyTable


## Testing
The code is tested using the ```unittest``` module, and can be run using:
```
python -m unittest discover
```
To see the code coverage, using ```coverage``` instead:
```
coverage run -m unittest discover
coverage report
```