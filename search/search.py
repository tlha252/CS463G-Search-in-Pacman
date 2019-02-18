# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to
# http://inst.eecs.berkeley.edu/~cs188/pacman/pacman.html
#
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


"""
In search.py, you will implement generic search algorithms which are called
by Pacman agents (in searchAgents.py).
"""

import util

class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples,
        (successor, action, stepCost), where 'successor' is a
        successor to the current state, 'action' is the action
        required to get there, and 'stepCost' is the incremental
        cost of expanding to that successor
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.  The sequence must
        be composed of legal moves
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other
    maze, the sequence of moves will be incorrect, so only use this for tinyMaze
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s,s,w,s,w,w,s,w]

# genericSearch is a function I added to reduce the redundancy in search.py
# DFS and BFS essentially have the same code but they use a different data structure
# for their 'magic union operator'. This function takes in the problem passed, and the
# union operator and models the pseudocode given to us in the class notes
def genericSearch(problem, unionOperator):
    if (unionOperator): # if unionOperator is true, it is being called by DFS so set openList to Stack
        openList = util.Stack()
    else: # if unionOperator is false, it is being called by BFS so set openList to Queue
        openList = util.Queue()
    closedList = [] #intializes closed list
    startingState = problem.getStartState() #intializes starting state by pulling from problem
    latestCoordinate = startingState #sets current state to the starting state
    openList.push((startingState,[],0)) #Push the starting state unto the list
    #For state representation, I use a format that is models what is returned by problem.getSuccessors
    # States look like: (coordinate, directions, cost)

    # PSEUDOCODE: WHILE (NOT IS GOALCURRENT) AND OPEN != 0
    while not problem.isGoalState(latestCoordinate) and not openList.isEmpty():
        # Reverse Order. Pop off at beginning of while loop
        # PSEUDOCODE: CURRENT = FIRST(OPEN)
        latestCoordinate, latestMove, latestCost = openList.pop() #Pops first value off open list, and stores the coordiante, moves, and cost of that state in 3 different variables
        if (latestCoordinate in closedList): # Makes sure DFS does not expand any open nodes
            continue;
        # PSEUDOCODE: CLOSED = CLOSED + {CURRENT}
        closedList.append(latestCoordinate) #adds the current state to closed list after values have been stored and already visited state check
        # PSEUDOCODE: IF ISGOAL(CURRENT) THEN REPORT SUCCESS
        if problem.isGoalState(latestCoordinate): #
            return latestMove
        # PSEUDOCODE: ELSE REPORT FAILURE. AKA restart while loop
        # PSEUDOCODE: OPEN = OPEN - {CURRENT} + [SUCESSORS(CURRENT, OPS) - CLOSED]
        for childCoordinate, childMove, childCost in problem.getSuccessors(latestCoordinate): #For loop that goes through every state related variable in child nodes and adds to open list
            openList.push((childCoordinate, latestMove+[childMove], childCost)) #CHILDCOST WAS LATEST COST BUT ALL COST ARE THE SAME
    # return [] return empty list of moves just in case nothing is found but i do not think that ever happens so remove at end if not needed
# end of genericSearch()

def depthFirstSearch(problem):
    """
    Search the deepest nodes in the search tree first

    Your search algorithm needs to return a list of actions that reaches
    the goal.  Make sure to implement a graph search algorithm

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print "Start:", problem.getStartState()
    print "Is the start a goal?", problem.isGoalState(problem.getStartState())
    print "Start's successors:", problem.getSuccessors(problem.getStartState())
    """
    "*** YOUR CODE HERE ***"
    unionOperator = True
    return genericSearch(problem, unionOperator)
    # util.raiseNotDefined()

def breadthFirstSearch(problem):
    """
    Search the shallowest nodes in the search tree first.
    """
    "*** YOUR CODE HERE ***"
    unionOperator = False
    return genericSearch(problem, unionOperator)
    # util.raiseNotDefined()

def uniformCostSearch(problem):
    "Search the node of least total cost first. "
    "*** YOUR CODE HERE ***"
    # startingState = problem.getStartState() #initializes starting state
    # openList = util.Queue() #intializes openList to the stack definitions provided in util.property
    # openList.push((startingState,[],0))
    # closedList = set()
    #
    # while not openList.isEmpty() and not problem.isGoalState(currentState):
    #
    # # util.raiseNotDefined()

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    "Search the node that has the lowest combined cost and heuristic first."
    "*** YOUR CODE HERE ***"
    util.raiseNotDefined()


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
