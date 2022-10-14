

from Agent import Agent
import random

class RandomAI ( Agent ):

    def getAction ( self, stench, breeze, glitter, bump, scream ):
        if glitter:
            return Agent.Action.GRAB;

        return self.__actions [ random.randrange ( len ( self.__actions ) ) ]
    
    __actions = [
        Agent.Action.TURN_LEFT,
        Agent.Action.TURN_RIGHT,
        Agent.Action.FORWARD,
        Agent.Action.CLIMB,
        Agent.Action.SHOOT,
        Agent.Action.GRAB
    ]