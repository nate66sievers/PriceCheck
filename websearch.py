import webbrowser


def ebay_search(searchString):
    # Ebay search formatting
    cSearchString = searchString.replace(" ", "+")
    start_url = 'https://www.ebay.com/sch/i.html?_nkw='
    end_url = '&_in_kw=1&_ex_kw=&_sacat=0&LH_Sold=1&_udlo=&_udhi=&LH_BIN=1&LH_ItemCondition=4&_samilow=&_samihi=&_sadis=15&_stpos=53215-3940&_sargn=-1%26saslc%3D1&_salic=1&_sop=12&_dmd=1&_ipg=50&LH_Complete=1&_fosrp=1'
    full_url = (start_url + cSearchString + end_url)
    return full_url

def clist_search_mil(searchString):
    # Ebay search formatting
    cSearchString = searchString.replace(" ", "+")
    start_url = 'https://milwaukee.craigslist.org/search/sss?query='
    full_url = (start_url + cSearchString)
    return full_url

def clist_search_chi(searchString):
    # Ebay search formatting
    cSearchString = searchString.replace(" ", "+")
    start_url = 'https://chicago.craigslist.org/search/sss?query='
    full_url = (start_url + cSearchString)
    return full_url

def facebook_search_mil(searchString):
    # Ebay search formatting
    cSearchString = searchString.replace(" ", "%20")
    start_url = 'https://www.facebook.com/marketplace/milwaukee/search/?query='
    end_url = '&vertical=C2C&sort=BEST_MATCH'
    full_url = (start_url + cSearchString + end_url)
    return full_url

def search_routine(searchString):
    # User search input
    #print('Enter ebay search name')
    #searchString = str(input())

    # Search ebay
    search_url = ebay_search(searchString)
    webbrowser.open(search_url)

    # Search milwaukee craigslist
    search_url = clist_search_mil(searchString)
    webbrowser.open(search_url)

    # Search chicago craigslist
    search_url = clist_search_chi(searchString)
    webbrowser.open(search_url)

    # Search facebook marketplace
    search_url = facebook_search_mil(searchString)
    webbrowser.open(search_url)

    print('Complete')