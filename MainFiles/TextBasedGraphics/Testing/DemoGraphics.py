# Define all Lists
class Graphics:
    
    def CreateLists():
        def CreateCurrentLine():
            currentLine = ["> ","A", "NewLine"]
            return currentLine

        def ConcatenateList(currentLine):
            gameVisuals = []
            for line in range(20):
                for item in range(len(currentLine)):
                    gameVisuals.append(currentLine[item])
            return gameVisuals

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

        currentLine = CreateCurrentLine()
        gameVisuals = ConcatenateList(currentLine)
        indexOfEndLine = findIndex(gameVisuals, "NewLine")
        indexOfStartLine = findIndex(gameVisuals, "> ")
        for lineNumber in range(20):
            line = gameVisuals[indexOfStartLine[lineNumber]:indexOfEndLine[lineNumber]]
            stringLine = ""
            for item in line:
                stringLine = stringLine + item
            print(stringLine)

#['> ', 'NewLine', '> ', 'NewLine', '> ', 'NewLine', '> ', 'NewLine', '> ', 'NewLine', '> ', 'NewLine', '> ', 'NewLine', '> ', 'NewLine', '> ', 'NewLine', '> ']
    CreateLists()
Graphics()
