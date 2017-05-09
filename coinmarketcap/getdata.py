import csv
import json
from pprint import pprint

from box import Box
from coinmarketcap import Market


aod = Market().ticker()

def url(coinlabel, asset=False):

    slug = "assets" if asset else "currencies"
    return "http://coinmarketcap.com/{}/{}".format(slug, coinlabel)

def tofloat(s):
    if s:
        return float(s)
    else:
        return 0.0

with open('vr.csv', 'wb') as csvfile:
    spamwriter = csv.writer(csvfile)

    spamwriter.writerow(
        "Name Rank Volume Price(BTC) Vol/Price Vol/Rank URL1".split())

    for row in aod:
        row = Box(row)

        # print row['24h_volume_usd']
        vol = tofloat(row['24h_volume_usd'])
        price = tofloat(row.price_btc)
        rank = int(row.rank)

        if not (vol and price):
            print "Skipping {0}".format(row.name)
            continue

        if vol < 10000:
            continue

        spamwriter.writerow([
            row.name, row.rank, vol, "{:.8f}".format(price),
            int(vol / price), int(vol/rank),
            url(row.id)
        ])
