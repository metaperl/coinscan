import csv
import json
from pprint import pprint

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

with open('vr.csv', 'w') as csvfile:
    spamwriter = csv.writer(csvfile)

    spamwriter.writerow(
        "Name Rank   Rank/Vol Volume Price(BTC)  Vol/Price  URL1 URL2".split())

    for row in aod:
        row = Box(row)

        # print row['24h_volume_usd']
        vol = tofloat(row['24h_volume_usd'])
        price = tofloat(row.price_btc)
        rank = int(row.rank)

        if not (vol and price):
            print "Skipping {}: vol=${:.2f}, price=${:.2f}".format(
                row.name,
                vol,
                price
            )
            continue

        if vol < 1000:
            print "Skipping {}: vol=${:.2f}".format(
                row.name,
                vol,
            )
            continue

        spamwriter.writerow([
            row.name,

            row.rank,
            "{:.8f}".format(rank/vol),
            vol,
            "{:.8f}".format(price),
            int(vol/price),

            url(row.id),
            url2(row.symbol),

        ])
