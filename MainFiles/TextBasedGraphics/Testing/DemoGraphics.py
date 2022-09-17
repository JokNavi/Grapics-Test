# Define all Lists
class Graphics:

    # Creates the single lines lists
    def CreateLists():
        def CreateCurrentLine():
            currentLine = ["> "]
            for item in range(20*3):
                currentLine.append("-")
            return currentLine

        # Makes the input lists into one list
        def ConcatenateFullList():
            gameVisuals = []
            currentLine = CreateCurrentLine()
            for line in range(20):
                gameVisuals.append(currentLine)
            return gameVisuals

        gameVisuals = ConcatenateFullList()
        return gameVisuals

    def RunGame(gameVisuals, printWhat):
        # print the full list in seperate lines
        def PrintLines():
            for lineNumber in range(20):
                line = gameVisuals[lineNumber]
                print(*line, sep="")

        # print the full list in seperate numbered lines
        def PrintNumberedLines():
            for lineNumber in range(20):
                line = gameVisuals[lineNumber]
                line = list(map(lambda x: x.replace('>', f"{str(lineNumber)}>"), line))
                print(*line, sep="")

        if(printWhat == "Numbered"):
            PrintNumberedLines()
        elif(printWhat == "Default"):
            PrintLines()
        else: print("Error, non existent game type!")


    gameVisuals = CreateLists()
    RunGame(gameVisuals, "Default")


Graphics()
