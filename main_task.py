import webscrape
import websearch


def service_func():
    print('...')

searchList = []

if __name__ == '__main__':
    # webscrape.py executed as script
    service_func()
    searchString = input('Search: ')
    #print('Searching for:',searchString)
    webscrape.ebayScrape(searchString)

    #websearch.search_routine(searchString)