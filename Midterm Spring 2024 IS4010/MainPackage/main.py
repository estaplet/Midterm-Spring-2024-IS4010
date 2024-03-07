# Name:Elizabeth Stapleton
# email: stapleet@mail.uc.edu
# Assignment Number: stapleet_MidtermExam
# Due Date: 03/07/2023
# Course/Section: IS4010
# Semester/Year: Spring 2024
# Brief Description of the assignment: This module is the main .py that imports the play function.
# Citations:
# Anything else that's relevant:


# main.py

from videoGamePackage.videoGame import *


if __name__ == "__main__":
    totalPlays = 1000
    won = 0
    lost = 0
    
    
    # try/else error handling message to prevent game from crashing
    try: 
        
        for i in range(0, totalPlays):
    
            if play():
                won = won + 1
            else:
                lost = lost + 1
    except:
        None
    
    # calculates the percentage won
    percentageWon = won/totalPlays
    
    # print statement for total plays, number of wins, number of losses, and percentage won
    print("Total plays:",totalPlays, "won = ",won, "lost = ",lost,
              "percentage won = ",percentageWon)
