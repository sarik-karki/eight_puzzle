# import queueingFunction
import heapq as min_heap
import copy

class Node:
    def __init__(self, data):
        self.parent = None
        self.data = data
        self.children = []
        self.depth = 0
        self.numNodeExpanded = 0
        self.algorithm = ""

    def addAlgorithmType(self, algorithm):
        self.algorithm = algorithm

    def __lt__(self, nodeToCompare, heuristic):
        # if  self.depth == nodeToCompare.depth:
        #     # return self.data < nodeToCompare.data
        # To do when heuristic comes through
        if self.algorithm == "UCS":
            return self.depth < nodeToCompare.depth
        elif self.algorithm == "MST":
            return self.misplacedTiles() < nodeToCompare.misplacedTiles()
        elif self.algorithm == "MNH":
            return


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


    def pathCost(self):
        # from the current state return the path cost
        ## a = [[5, 3, 2],
        #      [4, 0, 6],
        #      [1, 7, 8]]
        #like in this example, how far is 5 from its actual position
        #one element will be at most 4 position far from its actual position, add them for all the path and return g(n)
        return


    #check for possible operators
    def expand(self, queueList, seenStack):



        validOperators = self.getOperators()
        newNodes = []
        nodeAdded = False



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
                        expandRight.numNodeExpanded = self.numNodeExpanded + 1
                        expandRight.parent = self
                        newNodes.append(expandRight)


                    #move blank left
                    if validOperators[1]:
                        expandLeft = copy.deepcopy(self)
                        expandLeft.data[i][j] = expandLeft.data[i][j - 1]
                        expandLeft.data[i][j - 1] = 0
                        expandLeft.depth = self.depth + 1
                        expandLeft.numNodeExpanded = self.numNodeExpanded + 1
                        expandLeft.parent = self
                        newNodes.append(expandLeft)


                    #move blank up
                    if validOperators[2]:
                        expandUp = copy.deepcopy(self)
                        expandUp.data[i][j] = expandUp.data[i-1][j]
                        expandUp.data[i-1][j] = 0
                        expandUp.depth = self.depth + 1
                        expandUp.numNodeExpanded = self.numNodeExpanded + 1
                        expandUp.parent = self
                        newNodes.append(expandUp)


                    #move blank down
                    if validOperators[3]:
                        expandDown = copy.deepcopy(self)
                        expandDown.data[i][j] = expandDown.data[i+1][j]
                        expandDown.data[i+1][j] = 0
                        expandDown.depth = self.depth + 1
                        expandDown.numNodeExpanded = self.numNodeExpanded + 1
                        expandDown.parent = self
                        newNodes.append(expandDown)


                    for c in range(len(newNodes)):
                        if tuple(map(tuple, newNodes[c].data)) not in seenStack:
                            self.children.append(newNodes[c])
                            min_heap.heappush(queueList, newNodes[c])
                            seenStack[tuple(map(tuple, newNodes[c].data))] = True
                            nodeAdded = True

                    if nodeAdded:
                        self.numNodeExpanded += 1

                    break



    def get_depth(self):
        return self.depth

    def get_numNodeExpanded(self):
        return self.numNodeExpanded
