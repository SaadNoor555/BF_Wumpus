# ======================================================================
# FILE:        Main.py
#
# AUTHOR:      Abdullah Younis
#
# DESCRIPTION: This file is the entry point for the program. The main
#              function serves a couple purposes: (1) It is the
#              interface with the command line. (2) It reads the files,
#              creates the World object, and passes that all the
#              information necessary. (3) It is in charge of outputing
#              information.
#
# NOTES:       - Syntax:
#
#                   Wumpus_World [Options] [InputFile] [OutputFile]
#
#                  Options:
#                       -m Use the ManualAI instead of MyAI.
#                       -r Use the RandomAI instead of MyAI.
#                      -d Debug mode, which displays the game board
#                         after every mode. Useless with -m.
#                      -h Displays help menu and quits.
#                      -v Verbose mode displays world file names before
#                         loading them.
#                      -f treats the InputFile as a folder containing
#                         worlds. This will trigger the program to
#                         display the average score and standard
#                         deviation instead of a single score. InputFile
#                         must be entered with this option.
#
#                  InputFile: A path to a valid Wumpus World File, or
#                             folder with -f. This is optional unless
#                             used with -f or OutputFile.
#
#                  OutputFile: A path to a file where the results will
#                              be written. This is optional.
#
#              - If -m and -r are turned on, -m will be turned off.
#
#              - Don't make changes to this file.
# ======================================================================

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