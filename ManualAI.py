

from Agent import Agent

class ManualAI ( Agent ):

    def getAction ( self, stench, breeze, glitter, bump, scream ):
        # Print Command Menu
        print ( "Press 'w' to Move Forward  'a' to 'Turn Left' 'd' to 'Turn Right'" )
        print ( "Press 's' to Shoot         'g' to 'Grab'      'c' to 'Climb'" )
        
        #Get Input
        userInput = input ( 'Please input: ' ).strip()
        while not userInput:
            userInput = input().strip()
        
        # Return Action Associated with Input
        if userInput[0] == 'w':
            return Agent.Action.FORWARD
            
        if userInput[0] == 'a':
            return Agent.Action.TURN_LEFT
            
        if userInput[0] == 'd':
            return Agent.Action.TURN_RIGHT
            
        if userInput[0] == 's':
            return Agent.Action.SHOOT
            
        if userInput[0] == 'g':
            return Agent.Action.GRAB
            
        return Agent.Action.CLIMB