import colorcode
import argparse
import sys


def main(args):
    # Input for color
    parser = argparse.ArgumentParser(description='Options for Generating color')
    parser.add_argument('-t', '--type', help='Input for color type(hex, rgb, hsv & cmyk)', required=False)
    args = parser.parse_args()

    type_of_color = str(args.type).lower()
    random_color = colorcode.ColorCode()

    if type_of_color == 'hex':
        print(random_color.generate_hex())

    elif type_of_color == 'rgb':
        print(random_color.generate_rgb())

    elif type_of_color == 'hsv':
        print(random_color.generate_hsv())

    elif type_of_color == 'cmyk':
        print(random_color.generate_cmyk())

    else:
        print(random_color.generate_hex())


if __name__ == "__main__":
    sys.exit(main(sys.argv))
