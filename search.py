# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
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
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s, s, w, s, w, w, s, w]

def depthFirstSearch(problem: SearchProblem):
    print("Start:", problem.getStartState())
    print("Is the start a goal?", problem.isGoalState(problem.getStartState()))
    print("Start's successors:", problem.getSuccessors(problem.getStartState()))
    "*** YOUR CODE HERE ***"

    util.raiseNotDefined()

def breadthFirstSearch(problem: SearchProblem):
    """Search the shallowest nodes in the search tree first."""
    from util import Queue
    bfsQueue = Queue()

    visited = [] 
    path = [] 

    bfsQueue.push((problem.getStartState(),[]))

    hasAnswer = False
    while(not hasAnswer):
        loc,path = bfsQueue.pop()
        visited.append(loc)
        if problem.isGoalState(loc):
            return path
        nextRow = problem.getSuccessors(loc)
        for item in nextRow:
            if item[0] not in visited:
                newPath = path + [item[1]] 
                bfsQueue.push((item[0],newPath))

def depthFirstSearch(problem: SearchProblem):
    """Search the deepest nodes in the search tree first."""
    from util import Stack

    dfsStack = Stack()

    visited = []
    path = []

    dfsStack.push((problem.getStartState(),[]))

    hasAnswer = False
    while(not hasAnswer):
        loc,path = dfsStack.pop()
        visited.append(loc)
        if problem.isGoalState(loc):
            return path
        nextLevel = problem.getSuccessors(loc)
        for item in nextLevel:
            if item[0] not in visited:
                newPath = path + [item[1]] 
                dfsStack.push((item[0],newPath))
    return []

def uniformCostSearch(problem: SearchProblem):
    """Search the node of least total cost first."""
    "*** YOUR CODE HERE ***"
    from util import PriorityQueue
    initial = problem.getStartState()
    if problem.isGoalState(initial) :
        return []
    itemsCostPaths = PriorityQueue()
    noRepeats = []
    itemsCostPaths.push((initial, []), 0)

    while (True):
        if itemsCostPaths.isEmpty():
            return []

        prob, path = itemsCostPaths.pop()
        noRepeats.append(prob)
        if(problem.isGoalState(prob)):
            return path

        successors = problem.getSuccessors(prob)

        for succ in successors:
            deeperPath = path + [succ[1]]

            if succ[0] not in noRepeats :
                itemsCostPaths.push((succ[0], deeperPath), problem.getCostOfActions(deeperPath))

            else :
                #if it is in repeats, see if newer path is cheaper
                for item in itemsCostPaths.heap :
                    if item[0] == succ[0] :
                        old = problem.getCostOfActions(item[1])
                        new = problem.getCostOfActions(deeperPath)
                        if new < old :
                            itemsCostPaths.update((succ[0], deeperPath), new)
                        break 
                

   

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem: SearchProblem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"
    util.raiseNotDefined()


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
