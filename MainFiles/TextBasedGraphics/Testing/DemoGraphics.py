# Define all Lists
from difflib import Match


class Graphics:

    # Creates the single lines lists
    def CreateLists():
        def CreateCurrentLine():
            currentLine = ["> "]
            for item in range(20*3):
                currentLine.append(".")
            return currentLine

        # Makes the input lists into one list
        def DefaultFullList():
            gameVisuals = []
            currentLine = CreateCurrentLine()
            for line in range(20):
                gameVisuals.append(currentLine)
            return gameVisuals

        gameVisuals = DefaultFullList()
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
                line = list(map(lambda x: x.replace(
                    '>', f"{str(lineNumber)}>"), line))
                print(*line, sep="")

        if(printWhat == "Numbered"):
            PrintNumberedLines()
        elif(printWhat == "Default"):
            PrintLines()
        else:
            print("Error, non existent game type!")


class Physiscs:
    def AddShapes(shape, size, CoordX, CoordY):
        CoordX = CoordX*3
        CoordY = CoordY
        gameVisuals = Graphics.CreateLists()

        def AddSquare():
            def SizeOne():
                currentY = list(gameVisuals[CoordY])
                currentY.pop(CoordX)
                currentY.insert(CoordX, "*")
                gameVisuals[CoordY] = currentY
                return gameVisuals

            def SizeTwo():
                #Top Line
                currentY = list(gameVisuals[CoordY+1])
                currentX = CoordX - 1
                for item in range(3):
                    currentY.pop(currentX + item)
                    currentY.insert(currentX + item, "=")
                gameVisuals[CoordY+1] = currentY
                
                #Center Line
                currentY = list(gameVisuals[CoordY])
                currentX = CoordX -3
                for item in range(7):
                    currentY.pop(currentX + item)
                    currentY.insert(currentX + item, "=")
                gameVisuals[CoordY] = currentY

                #Bottom Line
                currentY = list(gameVisuals[CoordY-1])
                currentX = CoordX - 1
                for item in range(3):
                    currentY.pop(currentX + item)
                    currentY.insert(currentX + item, "=")
                gameVisuals[CoordY-1] = currentY
                
                return gameVisuals

            match size:
                case 1:
                    SizeOne()
                case 2:
                    SizeTwo()
                    
        match shape:
            case "Square":
                AddSquare()
        
        return gameVisuals

    def gravity():
        pass


class Game:
    gameVisuals = Graphics.CreateLists()
    gameVisuals = Physiscs.AddShapes("Square", 2, 10, 10)
    Graphics.RunGame(gameVisuals, "Default")


Graphics()
