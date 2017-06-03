import csv
import json
from pprint import pprint

from box import Box
from coinmarketcap import Market


aod = json.loads(Market().ticker())

MIN_VOLUME = 20000

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

with open('vr.csv', 'w') as csvfile:
    spamwriter = csv.writer(csvfile)

    spamwriter.writerow(
        "Name Volume(USD) Price(BTC) 1h_Gain 24h_Gain 7d_Gain URL1 URL2".split())

    for row in aod:
        row = Box(row)

        # print row['24h_volume_usd']
        vol = tofloat(row['24h_volume_usd'])
        price = tofloat(row.price_btc)

        if not (vol and price):
            print "Vol or Price Missing. Skipping {}: vol=${:.2f}, price=${:.2f}".format(
                row.name,
                vol,
                price
            )
            continue

        if vol < MIN_VOLUME:
            print "Low volume skip of {}: vol=${:.2f}".format(
                row.name,
                vol,
            )
            continue

        spamwriter.writerow([
            row.name,
            vol,

            "{:.8f}".format(price),
            row['percent_change_1h'],
            row['percent_change_24h'],
            row['percent_change_7d'],

            url(row.id),
            url2(row.symbol),
        ])
