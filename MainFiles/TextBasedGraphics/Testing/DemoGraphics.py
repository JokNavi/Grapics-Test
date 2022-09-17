# Define all Lists
class Graphics:

    # Creates the single lines lists
    def CreateLists():
        def CreateCurrentLine():
            currentLine = ["> ", "A"]
            return currentLine

        # Makes the input lists into one list
        def ConcatenateFullList():
            gameVisuals = []
            currentLine = CreateCurrentLine()
            for line in range(20):
                gameVisuals.append(currentLine)
            return gameVisuals
        
        #print the full list in seperate lines
        def PrintLines(gameVisuals):
            for lineNumber in range(20):
                line = gameVisuals[lineNumber]
                print(*line, sep="")

        #print the full list in seperate numbered lines
        def PrintNumberedLines(gameVisuals):
            for lineNumber in range(20):
                line = gameVisuals[lineNumber]
                line = list(map(lambda x: x.replace('>', f"{str(lineNumber)}>"), line))
                print(*line, sep="")

        
        gameVisuals = ConcatenateFullList()
        PrintLines(gameVisuals)
        #PrintNumberedLines(gameVisuals)
    CreateLists()



Graphics()
