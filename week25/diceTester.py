import dice

def main(args):
    dice1 = dice.Dice()
    print(dice1)
    
    dice2 = dice.Dice(8)
    dice2.set_dice_faces(1,1,2,3,5,8,13,21)
    print(dice2)
    print(dice2.roll_dice())

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))

