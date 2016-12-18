import sys
import argparse


def main(args):
    # get text input
    parser = argparse.ArgumentParser(description='Make text great again by replacing some letters with numbers')
    parser.add_argument('-t', '--text', help='Input for the text', required=True)
    args = parser.parse_args()

    replacable = {'B': '8', 'E': '3', 'I': '1', 'O': '0', 's': '5'}

    text_input = args.text.upper()
    print(text_input)

    for letter, num in replacable.items():
        print(letter + ': ' + num)
        text_input = text_input.replace(letter, num)

    print(text_input)

if __name__ == "__main__":
    sys.exit(main(sys.argv))
