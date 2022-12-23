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

def breadthFirstSearch(problem: SearchProblem):
    """Search the shallowest nodes in the search tree first."""
    from util import Queue
    bfsQueue = Queue()

    noRepeats = [] # lists all nodes that have already been visited
    path = [] # holds the correct path, which is pushed to the queue

    bfsQueue.push((problem.getStartState(),[]))

    """Main search loop that keeps adding nodes to the queue until a goal path has been found."""
    while(not bfsQueue.isEmpty()):
        loc,path = bfsQueue.pop() # pull the first-pushed entry in the queue (the shallowest node in the search tree)
        noRepeats.append(loc) # this location won't be used again
        if problem.isGoalState(loc):
            return path # at the goal? return the path and stop searching
        """Everything below happens if a goal path has not yet been found: the loop restarts afterwards."""
        nextRow = problem.getSuccessors(loc) # search the next level of possible paths from the location taken from the queue
        for item in nextRow: # check for every possible next move
            if item[0] not in noRepeats: # only if it has not yet been searched, of course
                noRepeats.append(item[0])
                newPath = path + [item[1]] 
                bfsQueue.push((item[0],newPath)) # push the resulting node to the queue
    return []

def depthFirstSearch(problem: SearchProblem):
    """Search the deepest nodes in the search tree first."""
    from util import Stack
    dfsStack = Stack()

    noRepeats = [] # lists all nodes that have already been visited
    path = [] # holds the correct path, which is pushed to the stack

    dfsStack.push((problem.getStartState(),[]))

    """Main search loop that keeps adding nodes to the stack until a goal path has been found."""
    while(not dfsStack.isEmpty()):
        loc,path = dfsStack.pop() # pop the last pushed entry in the stack (the deepest node in the search tree)
        noRepeats.append(loc) # this location won't be used again
        if problem.isGoalState(loc): 
            return path # at the goal? return the path and stop searching
        """Everything below happens if a goal path has not yet been found: the loop restarts afterwards."""
        nextLevel = problem.getSuccessors(loc) # search the next level of possible paths from the location taken from the stack
        for item in nextLevel: # check for every possible next move
            if item[0] not in noRepeats: # only if it has not yet been searched, of course
                newPath = path + [item[1]] 
                dfsStack.push((item[0],newPath)) # push the resulting node to the stack
    return []

def uniformCostSearch(problem: SearchProblem):
    """Search the node of least total cost first."""
    from util import PriorityQueue
    initial = problem.getStartState()
    if problem.isGoalState(initial) :
        return [] # at the goal already? then there is no need to search
    itemsCostPaths = PriorityQueue()
    noRepeats = [] # lists all nodes that have already been visited
    itemsCostPaths.push((initial, []), 0)

    while (True):
        if itemsCostPaths.isEmpty():
            return []

        prob, path = itemsCostPaths.pop() # pull the first-pushed entry from the queue
        noRepeats.append(prob) # this location won't be used again
        if(problem.isGoalState(prob)):
            return path # at the goal? return the path and stop searching

        successors = problem.getSuccessors(prob)

        for succ in successors:
            deeperPath = path + [succ[1]] # if a path is found for a child, it's also added to the original path

            if succ[0] not in noRepeats :
                noRepeats.append(succ[0]) # this successor won't be visited again
                itemsCostPaths.push((succ[0], deeperPath), problem.getCostOfActions(deeperPath))

            else :
                # if it is in repeats, see if a newer path is cheaper
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
    """Search the node that has the lowest comIbined cost and heuristic first."""
    from util import PriorityQueue
    initial = problem.getStartState()
    if problem.isGoalState(initial) :
        return [] # at the goal already? then there is no need to search
    pathCost = PriorityQueue()
    pathCost.push((initial, []), heuristic(initial, problem))
    noRepeats = [] # lists all nodes that have already been visited
    while True :
        if pathCost.isEmpty() :
            return []
        
        prob, path = pathCost.pop() # pull the first-pushed entry from the queue
        noRepeats.append(prob) # this location won't be used again

        if problem.isGoalState(prob) : 
            return path # at the goal? return the path and stop searching
        
        successors = problem.getSuccessors(prob) # look for all successor nodes for the current node

        for succ in successors :
            deeperPath = path + [succ[1]]
            if succ[0] not in noRepeats :
                noRepeats.append(succ[0])
                pathCost.push((succ[0], deeperPath), problem.getCostOfActions(deeperPath) + heuristic(succ[0], problem))

            else :
                #if it is in repeats, see if a newer path is cheaper
                for item in pathCost.heap :
                    if item[0] == succ[0] :
                        old = problem.getCostOfActions(item[1]) + heuristic(item[0], problem)
                        new = problem.getCostOfActions(deeperPath) + heuristic (succ[0], problem)

                        if new < old :
                            pathCost.update((succ[0], deeperPath), new)
                        break 
# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
