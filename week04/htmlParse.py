import requests
from bs4 import BeautifulSoup

def main(args):
    # Get Webpage
    response = requests.get('http://hp.com')
    response.raise_for_status()

    soup = BeautifulSoup(response.text, "lxml")
    words = soup.get_text().split(' ')
    words = filter(None,words)
    print(len(words))
    i = 0
    while True:
        if i >= len(words):
            break
        
        print i
        i += 1
        print '    ', len(words)
        words[i].replace('\n','').strip()
        if 'http' in words[i] or '/' in words[i] or '\\' in words[i] or '' in words[i]:
            del words[i]
        
    print(words)

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
