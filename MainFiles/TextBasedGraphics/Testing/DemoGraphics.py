# Define all Lists
class Graphics:

    # Creates the single lines lists
    def CreateLists():
        def CreateCurrentLine():
            currentLine = ["> ", "A", "NewLine"]
            return currentLine

        # Makes the input lists into one list
        def ConcatenateList(currentLine):
            gameVisuals = []
            for line in range(20):
                for item in range(len(currentLine)):
                    gameVisuals.append(currentLine[item])
            return gameVisuals

        # Used to find the index of certain characters.
        # Only works on lists and only lists that don't have two of the sought after words next to eachother.
        def findIndex(list, text):
            positions = []
            index = 0
            if(list.index(text, index) > 0):
                for line in range(20):
                    index = list.index(text, index+1)
                    positions.append(index)
            else:
                index = list.index(text, index)
                positions.append(index)
                for line in range(20-1):
                    index = list.index(text, index+1)
                    positions.append(index)
            return positions

        def PrintLines(gameVisuals, indexOfEndLine, indexOfStartLine):
            for lineNumber in range(20):
                line = gameVisuals[indexOfStartLine[lineNumber]:indexOfEndLine[lineNumber]]
                stringLine = ""
                for item in line:
                    stringLine = stringLine + item
                print(stringLine)

        currentLine = CreateCurrentLine()
        gameVisuals = ConcatenateList(currentLine)
        indexOfEndLine = findIndex(gameVisuals, "NewLine")
        indexOfStartLine = findIndex(gameVisuals, "> ")
        PrintLines(gameVisuals, indexOfEndLine, indexOfStartLine)
    CreateLists()


Graphics()
