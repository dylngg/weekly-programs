import random
import argparse


def main(args):
    # get text input
    parser = argparse.ArgumentParser(description='Generate trump ipusm')
    parser.add_argument('-p', '--paragraphs', help='Input for amount of paragraphs (Default: 3)',
                        required=False)
    args = parser.parse_args()

    # get number of paragraphs from args
    num_of_paragraphs = 3
    if args.paragraphs:
        num_of_paragraphs = int(args.paragraphs)

    # open the trump twitter floodgates
    with open('tweets.txt', 'r') as f:
        tweets = [line.strip() for line in f]

    print(generate_trump_ipsum(tweets, num_of_paragraphs))


def generate_trump_ipsum(tweets, num_of_paragraphs):
    # generate ipsum text
    ipsum_text = ''
    for x in range(0, num_of_paragraphs):
        paragraph = ''
        while len(paragraph) < 500:
            tweet_key = random.randint(0, len(tweets))
            paragraph += tweets[tweet_key] + ' '

            # remove tweet, so tweet doesn't appear more than once
            tweets.pop(tweet_key)

        ipsum_text += paragraph + '\n\n'

    return ipsum_text


if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
