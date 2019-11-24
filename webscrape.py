# For importing HTML data
from lxml import html
import requests

# For formatting money
from decimal import Decimal, ROUND_DOWN

import statistics
from pprint import pprint

def ebayScrape(searchString):
    # Pull data from website into a tree structure
    # Still need to learn more about how this tree structure works
    fullURL = ebay_search(searchString)
    page = requests.get(fullURL)
    tree = html.fromstring(page.content)

    # Create an array of prices from tree data
    prices = tree.xpath('//span[@class="bold bidsold"]/text()')

    # Get prices list length
    array_length = len(prices)

    errCount = 0
    cnt1 = 0
    pricesFloat = []
    # Build an array of prices
    for i in range(array_length):
        index1 = prices[i].find('$') + 1
        prices[i] = prices[i][index1:]
        prices[i] = prices[i].replace(" ","")
        prices[i] = prices[i].replace(",","")
        try:
            float(prices[i])
            pricesFloat.append(float(prices[i]))
            cnt1 = cnt1 + 1
        except:
            errCount = errCount + 1

    # print('Error Count: ',errCount)
    resultStats(pricesFloat)

def ebay_search(searchString):
    # Ebay search formatting
    # Returns formatting ebay url
    cSearchString = searchString.replace(" ", "+")
    start_url = 'https://www.ebay.com/sch/i.html?_nkw='
    end_url = '&_in_kw=1&_ex_kw=&_sacat=0&LH_Sold=1&_udlo=&_udhi=&LH_BIN=1&LH_ItemCondition=4&_samilow=&_samihi=&_sadis=15&_stpos=53215-3940&_sargn=-1%26saslc%3D1&_salic=1&_sop=12&_dmd=1&_ipg=50&LH_Complete=1&_fosrp=1'
    full_url = (start_url + cSearchString + end_url)
    return full_url

def resultStats(pricesFloat):
    meanPrice = sum(pricesFloat)/len(pricesFloat)
    meanPrice = Decimal(str(meanPrice)).quantize(Decimal('.01'), rounding=ROUND_DOWN)
    #print('Mean price: $',meanPrice)

    medianPrice = pricesFloat[round(len(pricesFloat)/2)]
    print('Median Price: $',medianPrice)

    standardDev = statistics.stdev(pricesFloat)
    standardDev = Decimal(str(standardDev)).quantize(Decimal('.01'), rounding=ROUND_DOWN)
    print('Standard Deviation: $',standardDev)
    
    # print(sorted(pricesFloat, key = float))

