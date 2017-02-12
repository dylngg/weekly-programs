import dice
import argparse


def main(args):
    parser = argparse.ArgumentParser(description='Roll Some Dice')
    parser.add_argument('-d', '--dice', help='Num of Dice', required=False)
    parser.add_argument('-f', '--faces', help='Set the amount of dice faces', required=False)
    parser.add_argument('-s', '--set', help='Set the dice faces', required=False)
    args = parser.parse_args()
    
    num_of_dice = 1
    if args.dice:
        num_of_dice = int(args.dice)
    
    num_of_faces = 6
    if args.faces:
        num_of_faces = int(args.faces)
    
    dice1 = dice.Dice(num_of_faces)
    
    if args.set:
        new_dice_faces = args.set.split(',')
        print(new_dice_faces)
        for face in range(0, num_of_faces):
            dice1.set_dice_faces(new_dice_faces)
    
    for roll in range(0, num_of_dice):
        print(dice1.roll_dice(), end=' ')
    
    print()
    
    
if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))

