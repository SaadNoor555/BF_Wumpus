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

import sys
import os
import math
from World import World
import world_generator

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
def main ( ):
    args = sys.argv
    # print(args)
    sd = Check_Directories()
    has_directory = False
    if len(sd) != 0:
        has_directory = True
    if not Check_Create_Tournament(has_directory):
        while True:
            world = World(True)
            score = world.run()
            print ("Your agent scored: " + str(score))
            if not Rerun_Random_World():
                return
    print('hi')
    while True:
        sd = Check_Directories()
        world_number = Tournament_Select(sd)
        if os.path.exists("Worlds\\TournamentSet"+str(world_number)):
                break
        else:
            print("Invalid Tournament Set: \nWorlds\\TournamentSet"+str(world_number)+" directory does not exist.")
    print("---------------")
        
    # Important Variables
    debug      = Debug_Mode()
    verbose    = True 
    randomAI   = False
    manualAI   = False
    folder     = True
    worldFile  = "Worlds\\TournamentSet"+str(world_number)
    outputFile = ""
    firstToken = "--"
    # if len(args)>1:
    #     firstToken = args[1]
    # If there are options
    if firstToken[0] == '-':
        # Parse Options
        for char in firstToken[1:]:
            if char == '-':
                continue
            elif char == 'f' or char == 'F':
                folder = True
            elif char == 'v' or char == 'V':
                verbose = True
            elif char == 'r' or char == 'R':
                randomAI = True
            elif char == 'm' or char == 'M':
                manualAI = True
            elif char == 'd' or char == 'D':
                debug = True
            else:
                print ( "Wumpus_World [Options] [InputFile] [OutputFile]" )
                print ( )
                print ( "Options:" )
                print ( "\t-m Use the ManualAI instead of MyAI." )
                print ( "\t-r Use the RandomAI instead of MyAI." )
                print ( "\t-d Debug mode, which displays the game board" )
                print ( "\t   after every mode. Useless with -m." )
                print ( "\t-h Displays help menu and quits." )
                print ( "\t-f treats the InputFile as a folder containing" )
                print ( "\t   worlds. This will trigger the program to" )
                print ( "\t   display the average score and standard" )
                print ( "\t   deviation instead of a single score. InputFile" )
                print ( "\t   must be entered with this option." )
                print ( )
                print ( "InputFile: A path to a valid Wumpus World File, or" )
                print ( "           folder with -f. This is optional unless" )
                print ( "           used with -f." )
                print ( )
                print ( "OutputFile: A path to a file where the results will" )
                print ( "            be written. This is optional." )
                print ( )
                return;

        if randomAI and manualAI:
            # If both AI's on, turn one off and let the user know.
            manualAI = False
            print("[WARNING] Manual AI and Random AI both on; Manual AI was turned off.")

        if len(args) >= 3:
            worldFile = args[2]
        if len(args) >= 4:
            outputFile = args[3]
    else:
        if len(args) >= 2:
            worldFile = args[1]
        if len(args) >= 3:
            outputFile = args[2]

    if worldFile == "":
        if folder:
            print ( "[WARNING] No folder specified; running on a random world." )
        world = World ( debug, randomAI, manualAI )
        score = world.run()
        print ( "The agent scored: " + str(score) )
        return
            
    if folder:
        listOfWorlds = None
        
        try:
            listOfWorlds = os.listdir ( worldFile )
        except:
            print ( "[ERROR] Failed to open directory." )
            return

        numOfScores = 0
        sumOfScores = 0
        sumOfScoresSquared = 0

        for file in listOfWorlds:
            if verbose:
                print ( "Running world: " + str(file) )

            score = None
            try:
                newLineDelim = "\n"
                if "\r\n".encode() in open(worldFile + "/" + file,"rb").read():
                    newLineDelim = "\r\n"
                world = World ( debug, randomAI, manualAI, open ( worldFile + "/" + file, 'r', newline=newLineDelim ) )
                score = world.run()
            except Exception:
                numOfScores = 0
                sumOfScores = 0
                sumOfScoresSquared = 0
                break;

            numOfScores += 1
            #print("Score: "+str(score)+"\n\n-----------------\n")
            sumOfScores += score
            sumOfScoresSquared += score*score

        avg = None
        std_dev = None
        
        if numOfScores != 0:
            avg = sumOfScores / numOfScores
            std_dev = math.sqrt ( (sumOfScoresSquared - ((sumOfScores*sumOfScores) / numOfScores) ) / numOfScores)
        else:
            avg = float('nan')
            std_dev = float('nan')

        if outputFile == "":
            print ( "The agent's average score: " + str(avg) )
            print ( "The agent's standard deviation: " + str(std_dev) )
        else:
            outFile = open ( outputFile, 'w' )
            outFile.write ( "SCORE: " + str(avg) + '\n' )
            outFile.write ( "STDEV: " + str(std_dev) )
            outFile.close ( )
        while True:
            r = input("Tournament Set Finished. Enter (q) to close.\n")
            if r.lower() == "q":
                return

    try:
        if verbose:
            print ( "Running world: " + worldFile )

        newLineDelim = "\n"
        if "\r\n".encode() in open(worldFile,"rb").read():
            newLineDelim = "\r\n"
        world = World ( debug, randomAI, manualAI, open ( worldFile, 'rt', newline=newLineDelim ) )
        score = world.run()

        if outputFile == "":
            print ( "The agent scored: " + str(score) )
        else:
            try:
                outFile = open ( outputFile, 'w' )
                outFile.write ( "SCORE: " + str(score) )
                outFile.close ( )
            except:
                print ( "[ERROR] Failure to write to output file." )
    except Exception:
        print ( "[ERROR] Failure to open file." )

main()
