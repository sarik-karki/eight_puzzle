# hardcoded puzzles;
# add matrix's of puzzle
a = [[1, 3, 2], [4, 5, 6], [8, 9, 0]]
b = 1
c = 1
d = 1
e = 1


def main():
    puzzleMode = input("Enter 1 for default puzzle, 2 to make your own puzzle")
    if puzzleMode == "1":
        selectAlgorithm(defaultPuzzleSelect())
    if puzzleMode == "2":
        # ask for puzzle information
        formedPuzzle = 1;
        selectAlgorithm(formedPuzzle)


def selectAlgorithm(puzzleToSolve):
    selectedAlgorithm = input(
        "Enter 1 for Uniform Cost Search, 2 for A* with the Misplaced Tile heuristic and 3 for A* with the Manhattan Distance heuristic: ")
    if selectedAlgorithm == 1:
        uniformCostSearch(puzzleToSolve, 0)
    if selectedAlgorithm == 2:
        misplacedTileHeuristic(puzzleToSolve, 1)
    if selectedAlgorithm == 3:
        manhattanDistanceHeuristic(puzzleToSolve, 2)


def defaultPuzzleSelect():
    choicePuzzle = input("Enter the default puzzle you would like to select; 1: Easy, 2: Medium, 3: Hard ")
    if choicePuzzle == "1":
        return a
    if choicePuzzle == "2":
        return b


def uniformCostSearch(puzzle, heuristic):


    solvedPuzzle = 1
    print(solvedPuzzle)


def misplacedTileHeuristic(puzzle, heuristic):
    solvedPuzzle = 1
    print(solvedPuzzle)


def manhattanDistanceHeuristic(puzzle, heuristic):
    solvedPuzzle = 1
    print(solvedPuzzle)
