
from secrets import choice
import sys
import os
import math
from World import World
import time
import world_generator
from wumpus_gui import *

def Tournament_Select(sets):
    while True:
        try:
            print("---------------")
            print(sets)
            response = input("Which tournament set number would you like to run? (#)\n")
            response = int(response)
            return response
        except:
            print("Invalid Number: Response must be an integer (#)")

def Debug_Mode():
    while True:
        response = input("Run display mode? (y/n)\n")
        if response.lower() == "y" or response.lower() == "yes":
            return True
        elif response.lower() == "n" or response.lower() == "no":
            return False
        else:
            print("Invalid Input: Response must be yes or no. (y/n)")
def Rerun_Random_World():
    while True:
        print("---------------")
        response = input("Run another world? (y/n)\n")
        if response.lower() == "y" or response.lower() == "yes":
            return True
        elif response.lower() == "n" or response.lower() == "no":
            return False
        else:
            print("Invalid Input: Response must be yes or no. (y/n)")
               
def Check_Directories():
    try:
        SETDIRECTORIES = os.listdir("Worlds")
    except:
        return []
    for d in SETDIRECTORIES:
        if "TournamentSet" not in d:
            SETDIRECTORIES.remove(d)
    if SETDIRECTORIES and "TournamentSet" in SETDIRECTORIES[0]:
        return SETDIRECTORIES
    else:
        return []

def Check_Create_Tournament(val):
    return False
    while True:
        if not val:
            response = input("No tournament sets detected. Would you like to generate set of 10,000? (y/n)\n")
            if response.lower() == "y" or response.lower() == "yes":
                world_generator.main()
                return True
            elif response.lower() == "n" or response.lower() == "no":
                print("Running on random generated world.")
                return False
            else:
                print("Invalid Input: Response must be yes or no. (y/n)")
        else:
            return True
def main (wrld_file = None ):
    args = sys.argv
    # print(args)
    sd = Check_Directories()
    has_directory = False
    if len(sd) != 0:
        has_directory = True
    if not Check_Create_Tournament(has_directory):
        while True:
            world = World(True, file= wrld_file)
            score = world.run(screen)
            print ("Your agent scored: " + str(score))
            show_msg_up('Game Over', screen)
            show_msg_down('score: '+str(score), screen)
            time.sleep(5)
            game()

screen = board_graphics_init()
pygame.display.set_caption('wumpus world')

def game():
    screen.fill((0, 0, 0))
    choice = main_menu(screen)
    if choice == 1:
        screen.fill((0, 0, 0))
        main()

    elif choice == 2:
        file = open('world/custom_world.txt', 'r')
        screen.fill((0, 0, 0))
        main(file)
    elif choice == 3:
        pygame.quit()

game()