import heapq as min_heap

from eight_puzzle.Node import Node
# from eight_puzzle.queueingFunction import QueueingFunction

# hardcoded puzzles;
# add matrix's of puzzle
a = [[1, 2, 3], [4, 5, 6], [7, 0, 8]]
b = [[1, 2, 3], [5, 0, 6], [4, 7, 8]]
c = [[1, 3, 6], [5, 0, 2], [4, 7, 8]]
d = [[1, 3, 6], [5, 0, 7], [4, 8, 2]]
e = [[1, 6 ,7], [5, 0, 3], [4, 8, 2]]
f = [[7, 1, 2], [4, 8, 5], [6, 3, 0]]
g = [[0, 7, 2], [4, 6, 1], [3, 5, 8]]


def main():
    puzzleMode = int(input("Enter 1 for default puzzle, 2 to make your own puzzle: "))
    if puzzleMode == 1:
        selectAlgorithm(defaultPuzzleSelect())

    # if puzzleMode == "2":
    #     # ask for puzzle information
    #     formedPuzzle = 1;
    #     selectAlgorithm(formedPuzzle)


def selectAlgorithm(puzzleToSolve):
    selectedAlgorithm = int(input("Enter 1 for Uniform Cost Search, 2 for A* with the Misplaced Tile heuristic and 3 for A* with the Manhattan Distance heuristic: "))
    if selectedAlgorithm == 1:
        uniformCostSearch(puzzleToSolve, 0)
    if selectedAlgorithm == 2:
        uniformCostSearch(puzzleToSolve, 1)
    if selectedAlgorithm == 3:
        uniformCostSearch(puzzleToSolve, 2)


def defaultPuzzleSelect():
    choicePuzzle = int(input("Enter the default puzzle you would like to select; 1: Easy, 2: Medium, 3: Hard "))
    if choicePuzzle == 1:
        return a
    if choicePuzzle == 2:
        return b
    if choicePuzzle == 3:
        return c
    if choicePuzzle == 4:
        return d
    if choicePuzzle == 5:
        return e
    if choicePuzzle == 6:
        return f
    if choicePuzzle == 7:
        return g


def uniformCostSearch(puzzle, heuristic):
    #goal-state

    goalState= [[1, 2, 3], [4,5,6], [7,8,0]]

    startingState = Node(puzzle)
    if heuristic == 0:
        startingState.algorithm = "UCS"
    elif heuristic == 1:
        startingState.algorithm = "MST"
    elif heuristic == 2:
        startingState.algorithm = "MNH"

    queueStack = []
    printStack = []
    seenList = {}

    maxQueueSize = 0

    min_heap.heappush(queueStack, startingState)

    seenList[tuple(map(tuple, startingState.data))] = True


    while  len(queueStack) > 0:
        maxQueueSize = max(maxQueueSize, len(queueStack))
        currentNode = min_heap.heappop(queueStack)
        printStack.append(currentNode.data)

        if currentNode.data == goalState:



            print()
            print("Solution found")
            print(f"Goal state was found at depth {currentNode.depth}")
            print(f"Number of Nodes expanded: {Node.totalNumNodeExpanded}")
            print(f"Max Queue Size: {maxQueueSize}")
            return
        # for i in range(3):
        #     for j in range(3):
        #         print(currentNode.data[i][j], end=" ")
        #     print()
        printStack.append(currentNode.data)
        currentNode.expand(queueStack, seenList)




main()











