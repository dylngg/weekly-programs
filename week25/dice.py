import random


class Dice():
    
     # init
    def __init__(self, number_of_faces = 6):
        self.number_of_faces = number_of_faces
        self.outcome = None
        self.dice_possibilites = [n + 1 for n in range(0, number_of_faces)]
    
    
    def __str__(self):
        return str(self.dice_possibilites)
    
    
    def roll_dice(self):
        outcome = self.dice_possibilites[random.randint(0, self.number_of_faces) - 1]
        self.outcome = outcome
        
        return outcome
    
    
    def set_dice_faces(self, face_values):
        if type(face_values) is not list:
            raise TypeError('Argument passed in is not a list')
        elif len(face_values) != self.number_of_faces:
            raise ValueError('Too many or too little face values. Expected', self.number_of_faces, 'faces.')
        else:
            for i, face in enumerate(face_values):
                self.dice_possibilites[i] = face
