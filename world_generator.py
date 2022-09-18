# ======================================================================
# FILE:        Generator.py
#
# AUTHOR:      Abdullah Younis
#
# DESCRIPTION: This file contains the Wumpus World Generator script. 
# ======================================================================

import sys
import random
import os

def randomInt ( limit ):
	return random.randrange(limit)
	
def genWorld ( colDimension, rowDimension, filename, tindex ):
	wc = 0
	wr = 0
	gc = 0
	gr = 0
	pits = []
	
	# Generate pits
	for r in range (rowDimension):
		for c in range (colDimension):
			print('generete korchi guyz')
			if (c != 0 or r != 0) and randomInt(100) < 1:
				pits.append((r,c))

	# Generate wumpus and gold
	wc = randomInt(colDimension)
	wr = randomInt(rowDimension)
	gc = randomInt(colDimension)
	gr = randomInt(rowDimension)

	while wc == 0 and wr == 0 and (wr, wc) not in pits:
		wc = randomInt(colDimension)
		wr = randomInt(rowDimension)

	while gc == 0 and gr == 0:
		gc = randomInt(colDimension)
		gr = randomInt(rowDimension)
		
		
	file = open("Worlds\\TournamentSet"+str(tindex)+"\\"+filename, "w")
	file.write( str(colDimension) + "\t" + str(rowDimension) + "\n" )
	file.write( str(wc) + "\t" + str(wr) + "\n" )
	file.write( str(gc) + "\t" + str(gr) + "\n" )

	file.write( str(len(pits)) + "\n" )
	for pit in pits:
		file.write( str(pit[0]) + "\t" + str(pit[1]) + "\n" )
	
	file.close();
	

#if len(sys.argv) != 5:
#	print ( "Usage: World_Generator Base_File_Name #ofWorlds rowDim colDim" )
#	exit(0)
def main():
	tournament_index = 1
	baseFileName = "World"
	numOfFiles   = int(10000)
	colDimension = int(random.randrange(4,8))
	rowDimension = int(random.randrange(4,8))

	while True:
		if os.path.exists("Worlds\\TournamentSet"+str(tournament_index)):
			tournament_index+=1
		else:
			os.makedirs("Worlds\\TournamentSet"+str(tournament_index))
			break
	for i in range(numOfFiles):
		print ( "Creating world number: " + str(i) + "." )
		if i>=0 and i<2500:
			genWorld( 4, 4, baseFileName + "_" + str(i) + ".txt", tournament_index )
		elif i>=2500 and i<3000:
			genWorld( 5, 4, baseFileName + "_" + str(i) + ".txt", tournament_index )
		elif i>=3000 and i<3500:
			genWorld( 6, 4, baseFileName + "_" + str(i) + ".txt", tournament_index )
		elif i>=3500 and i<4000:
			genWorld( 7, 4, baseFileName + "_" + str(i) + ".txt", tournament_index )
		elif i>=4000 and i<4500:
			genWorld( 4, 5, baseFileName + "_" + str(i) + ".txt", tournament_index )
		elif i>=4500 and i<5000:
			genWorld( 5, 5, baseFileName + "_" + str(i) + ".txt", tournament_index )
		elif i>=5000 and i<5500:
			genWorld( 6, 5, baseFileName + "_" + str(i) + ".txt", tournament_index )
		elif i>=5500 and i<6000:
			genWorld( 7, 5, baseFileName + "_" + str(i) + ".txt", tournament_index )
		elif i>=6000 and i<6500:
			genWorld( 4, 6, baseFileName + "_" + str(i) + ".txt", tournament_index )
		elif i>=6500 and i<7000:
			genWorld( 5, 6, baseFileName + "_" + str(i) + ".txt", tournament_index )
		elif i>=7000 and i<7500:
			genWorld( 6, 6, baseFileName + "_" + str(i) + ".txt", tournament_index )
		elif i>=7500 and i<8000:
			genWorld( 7, 6, baseFileName + "_" + str(i) + ".txt", tournament_index )
		elif i>=8000 and i<8500:
			genWorld( 4, 7, baseFileName + "_" + str(i) + ".txt", tournament_index )
		elif i>=8500 and i<9000:
			genWorld( 5, 7, baseFileName + "_" + str(i) + ".txt", tournament_index )
		elif i>=9000 and i<9500:
			genWorld( 6, 7, baseFileName + "_" + str(i) + ".txt", tournament_index )
		elif i>=9500 and i<10000:
			genWorld( 7, 7, baseFileName + "_" + str(i) + ".txt", tournament_index )



if __name__ == "__main__":
	main()
