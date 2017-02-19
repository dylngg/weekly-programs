import argparse
import wikipedia


def main(args):
    # get text input
    parser = argparse.ArgumentParser(description='Get information about unknown subjects (from wikipedia)')
    parser.add_argument('-t', '--text', help='Input for the text you want to know more about', required=True)
    args = parser.parse_args()
    
    if args.text and len(args.text) >= 1 and str(args.text) is not ' ':
        text = str(args.text)
    else:
        raise ValueError('Incorrect Text Input')
    
    options = search_wikipedia(text)
    
    print('Possible Meanings:')
    [print(' [' + str(i) + '] ' + option) for i, option in enumerate(options)]
    choices = input('Which option do you want to learn more about? (for multiple options use ","): ')
    choices.split(',')
    chosen_items = [int(choice) for choice in choices if choice is not ',' and choice is not ' ']
    
    for num in chosen_items:
        item =options[int(num)]
        print(get_summary(item) + '\n')
        
        report_input = input('Do you want the full report? (y/n): ')
        if 'y' in report_input.lower():
            print(get_full_report(item))
        
        print()


def search_wikipedia(text):
    options = wikipedia.search(text)
    
    return options

def get_summary(text):
    page = wikipedia.page(text)
    report = page.title + ' (' + page.url + ')\n-------------------\n'
    report += wikipedia.summary(text)
    
    return report


def get_full_report(text):
    page = wikipedia.page(text)
    full_report = page.title + ' (' + page.url + ')\n-------------------\n'
    full_report += page.content
    
    return full_report


if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
