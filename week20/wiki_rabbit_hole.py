import requests
from bs4 import BeautifulSoup
import random
import argparse


def main(args):
    # get text input
    parser = argparse.ArgumentParser(description='Get internet rabbit holes from wikipedia')
    parser.add_argument('-a', '--amount', help='Input for amount of internet rabbit holes you want to create', required=False)
    parser.add_argument('-o', '--open', help='Input for whether or not you want to open the website in a browser or have the text displaying in the command line (y/n)', required=False)
    args = parser.parse_args()
    
    holes = 1
    
    if args.amount:
        holes = int(args.amount)
    
    open_link_input = args.open
    open_link = False
    
    for x in range(0, holes):
        if open_link_input is 'y' or open_link_input is 'Y':
            open_rabbit_hole()
        else:
            print_rabbit_hole()


def print_rabbit_hole():
    # create rabbit hole
    rabbit_hole = create_rabbit_hole(True)
    
    import wikipedia
    wiki_title = rabbit_hole.replace('_', ' ')
    print('\n' + wiki_title)
    print('---------------------')
    print(wikipedia.summary(rabbit_hole))
    


def open_rabbit_hole():
    # create rabbit hole
    rabbit_hole = create_rabbit_hole()
    
    import webbrowser
    webbrowser.open(rabbit_hole)


def create_rabbit_hole(text = False):

    site= "https://en.wikipedia.org/wiki/Wikipedia:Unusual_articles"
    req = requests.get(site)
    page = req.text
    soup = BeautifulSoup(page, "html.parser")

    links = [cell['href'] for cell in soup.select('.wikitable b a')]
    
    if text is True:
        urls = [link[6:] for link in links]
    else:
        urls = ['https://en.wikipedia.org' + link for link in links]
    
    rabbit_hole = urls[random.randint(0, len(urls))]
    
    return rabbit_hole


if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
