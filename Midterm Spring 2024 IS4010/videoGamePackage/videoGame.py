# Name:Elizabeth Stapleton
# email: stapleet@mail.uc.edu
# Assignment Number: stapleet_MidtermExam
# Due Date: 03/07/2023
# Course/Section: IS4010
# Semester/Year: Spring 2024
# Brief Description of the assignment: This module is the videoGame.py that contains the play function.
# Citations:
# Anything else that's relevant:




# videoGame.py

if __name__ != "__main__":
    import random
    def play():
        '''
        returns True if you won, False if you lost 
        '''
        if random.randint(0,100) == 10:
            raise Exception("Game Crashed")
        return random.choice([True, False])