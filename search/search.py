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

from typing import List

import util
from game import Directions


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




def tinyMazeSearch(problem: SearchProblem) -> List[Directions]:
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s, s, w, s, w, w, s, w]

def depthFirstSearch(problem: SearchProblem) -> List[Directions]:
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print("Start:", problem.getStartState())
    print("Is the start a goal?", problem.isGoalState(problem.getStartState()))
    print("Start's successors:", problem.getSuccessors(problem.getStartState()))
    """
    "*** YOUR CODE HERE ***"
    #luat stari , pus intr-o lista vizitat
    my_stack = util.Stack()
    visited = set()

    start_state = problem.getStartState()
    my_stack.push((start_state,[]))

    while not my_stack.isEmpty():
        state,path = my_stack.pop()

        if problem.isGoalState(state):
            return path

        if state not in visited:
            visited.add(state)

            for successor,action,cost in problem.getSuccessors(state):
                if successor not in visited:
                    new_path = path + [action]
                    my_stack.push((successor,new_path))

    return []



    #util.raiseNotDefined()

def breadthFirstSearch(problem: SearchProblem) -> List[Directions]:
    """Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"
    my_queue = util.Queue()
    visited = list()

    start_state = problem.getStartState()
    my_queue.push((start_state,[]))

    while not my_queue.isEmpty():
        state,path = my_queue.pop()

        if problem.isGoalState(state):
            return path

        if state not in visited:
            visited.append(state)

            for successor,action,cost in problem.getSuccessors(state):
                if successor not in visited:
                    new_path = path + [action]
                    my_queue.push((successor,new_path))

    return []


    #util.raiseNotDefined()

def uniformCostSearch(problem: SearchProblem) -> List[Directions]:
    """Search the node of least total cost first."""
    "*** YOUR CODE HERE ***"
    my_priority_queue = util.PriorityQueue()

    visited = set()

    start_state  = problem.getStartState()
    my_priority_queue.push((start_state, []) , priority=0)
    while not my_priority_queue.isEmpty():
        state,path = my_priority_queue.pop()

        if problem.isGoalState(state):
            return path

        if state not in visited:
            visited.add(state)

            for succesor , action , cost in problem.getSuccessors(state):
                if succesor not in visited:
                    new_path = path + [action]
                    new_cost = problem.getCostOfActions(new_path)
                    my_priority_queue.push((succesor,new_path),priority=new_cost)

    return []



    util.raiseNotDefined()

def nullHeuristic(state, problem=None) -> float:
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem: SearchProblem, heuristic=nullHeuristic) -> List[Directions]:
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"
    my_priority_queue = util.PriorityQueue()
    cost_so_far = {}


    start_state = problem.getStartState()
    my_priority_queue.push((start_state, []), 0 + heuristic(start_state, problem))
    cost_so_far[start_state] = 0

    while not my_priority_queue.isEmpty():
        state, path = my_priority_queue.pop()


        if problem.isGoalState(state):
            return path


        for successor, action, stepCost in problem.getSuccessors(state):
            new_cost = cost_so_far[state] + stepCost
            if successor not in cost_so_far or new_cost < cost_so_far[successor]:
                cost_so_far[successor] = new_cost
                priority = new_cost + heuristic(successor, problem)
                my_priority_queue.push((successor, path + [action]), priority)

    return []

#util.raiseNotDefined()

# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
