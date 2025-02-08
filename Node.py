# import queueingFunction
import heapq as min_heap
import copy

class Node:
    totalNumNodeExpanded = 0

    def __init__(self, data):
        self.parent = None
        self.data = data
        self.children = []
        self.depth = 0
        self.algorithm = ""

    def addAlgorithmType(self, algorithm):
        self.algorithm = algorithm

    def __lt__(self, nodeToCompare):

        if self.algorithm == "UCS":
         return self.depth < nodeToCompare.depth

        if self.algorithm == "MST":
            if self.misplacedTiles() + self.depth == nodeToCompare.misplacedTiles() + nodeToCompare.depth:
                return self.depth < nodeToCompare.depth #break tie
            else:
             return self.misplacedTiles() + self.depth < nodeToCompare.misplacedTiles() + nodeToCompare.depth

        if self.algorithm == "MNH":
            if self.pathCost() + self.depth == nodeToCompare.depth + nodeToCompare.pathCost():
                return self.depth < nodeToCompare.depth #break tie with depth
            else:
                return self.depth + self.pathCost() < nodeToCompare.depth + nodeToCompare.pathCost()


    def getOperators(self):
        # [move blank left, move blank right, move blank up, move blank down
        validMoves =[True, True, True, True]
        for i in range(3) :
            for j in range(3):
                if self.data[i][j]  == 0:
                    if j == 2:
                        validMoves[0] = False
                    if j == 0:
                        validMoves[1] = False
                    if i == 0:
                        validMoves[2] = False
                    if i == 2:
                        validMoves[3] = False
        return validMoves


    def misplacedTiles(self):
        misplacedTilesNum = 0
        goalState = [[1, 2, 3], [4, 5, 6], [7, 0, 8]]
        for i in range(3):
            for j in range(3):
                if self.data[i][j] != 0:
                    if self.data[i][j] != goalState[i][j]:
                        misplacedTilesNum += 1
        return misplacedTilesNum



        #how many tiles are not in their place   # from the current state return the path cost
        #  a = [[5, 3, 2],
        #      [4, 0, 6],
        #      [1, 7, 8]]
        # in this example 4 and 6 are only in their correct place so this function will return 8-2 = 6 as the g(n) and used for the misplaced tile heuristic

    def pathCost(self):
        goalPositions = { 1: (0, 0), 2: (0, 1), 3: (0, 2), 4: (1, 0), 5: (1, 1), 6: (1, 2), 7: (2, 0), 8: (2, 1), 0: (2, 2) }
        costToGoal = 0
        for i in range(3):
            for j in range(3):
                if self.data[i][j] != 0:
                    distX, distY = goalPositions[self.data[i][j]]
                    costToGoal += abs(i - distX) + abs(j - distY)
        return costToGoal
        # from the current state return the path cost
        ## a = [[5, 3, 2],
        #      [4, 0, 6],
        #      [1, 7, 8]]
        #like in this example, how far is 5 from its actual position
        #one element will be at most 4 position far from its actual position, add them for all the path and return g(n)



    #check for possible operators
    def expand(self, queueList, seenStack):

        validOperators = self.getOperators()
        newNodes = []

        for i in range(3) :
            for j in range(3):
                #find 0
                if self.data[i][j] == 0:
                    #move blank right

                    if validOperators[0]:
                        expandRight = copy.deepcopy(self)
                        expandRight.data[i][j] = self.data[i][j+1]
                        expandRight.data[i][j+1] = 0
                        expandRight.depth = self.depth + 1
                        expandRight.parent = self
                        newNodes.append(expandRight)

                    #move blank left
                    if validOperators[1]:
                        expandLeft = copy.deepcopy(self)
                        expandLeft.data[i][j] = expandLeft.data[i][j - 1]
                        expandLeft.data[i][j - 1] = 0
                        expandLeft.depth = self.depth + 1
                        expandLeft.parent = self
                        newNodes.append(expandLeft)

                    #move blank up
                    if validOperators[2]:
                        expandUp = copy.deepcopy(self)
                        expandUp.data[i][j] = expandUp.data[i-1][j]
                        expandUp.data[i-1][j] = 0
                        expandUp.depth = self.depth + 1
                        expandUp.parent = self
                        newNodes.append(expandUp)

                    #move blank down
                    if validOperators[3]:
                        expandDown = copy.deepcopy(self)
                        expandDown.data[i][j] = expandDown.data[i+1][j]
                        expandDown.data[i+1][j] = 0
                        expandDown.depth = self.depth + 1
                        expandDown.parent = self
                        newNodes.append(expandDown)

                    for c in range(len(newNodes)):
                        if tuple(map(tuple, newNodes[c].data)) not in seenStack:
                            self.children.append(newNodes[c])
                            min_heap.heappush(queueList, newNodes[c])
                            seenStack[tuple(map(tuple, newNodes[c].data))] = True
                            Node.totalNumNodeExpanded += 1

                    print(f"Expanding node at depth {self.depth} with misplacedTiles {self.misplacedTiles()}")

                    break



