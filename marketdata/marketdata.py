import csv
import json
import os
from pprint import pprint
import time

from box import Box
from coinmarketcap import Market


aod = json.loads(Market().ticker())

#print aod

def url(coinlabel, asset=False):

    slug = "assets" if asset else "currencies"
    return "http://coinmarketcap.com/{}/{}".format(slug, coinlabel)

def url2(symbol, asset=False):

    return "http://altcoinlive.com/bittrex-{}-{}".format(
        symbol.lower(),
        'btc')

def tofloat(s):
    if s:
        return float(s)
    else:
        return 0.0

datapath = time.strftime("data/%Y/%m/%d")
if not os.path.isdir(datapath):
    os.makedirs(datapath)
datafile = "{}/{}".format(datapath, time.strftime("%H-%M-%S"))

with open(datafile, 'w') as csvfile:
    spamwriter = csv.writer(csvfile)

    spamwriter.writerow(
        "Name Symbol Rank Price(BTC) Price(USD) 24HVolume MarketCap %Change_1h %Change_24h %Change_7d LastUpdated".split())

    for row in aod:
        row = Box(row)

        spamwriter.writerow([
            row.name,
            row.symbol,
            row.rank,
            row.price_usd,
            row.price_btc,
            row["24h_volume_usd"],
            row["market_cap_usd"],
            row["available_supply"],
            row["total_supply"],
            row["percent_change_1h"],
            row["percent_change_24h"],
            row["percent_change_7d"],
            row["last_updated"]
        ])
