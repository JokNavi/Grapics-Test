import keyboard
import time
import math


# Define all Lists
class Graphics:

    # Creates the single lines lists
    def CreateDefaultList():
        def CreateCurrentLine():
            currentLine = ["> "]
            for item in range(20*3):
                currentLine.append(".")
            return currentLine

        # Makes the input lists into one list
        def DefaultFullList():
            gameVisuals = []
            for line in range(20):
                gameVisuals.append(CreateCurrentLine())
            return gameVisuals

        gameVisuals = DefaultFullList()
        return gameVisuals

    def OverWriteBorders(gameVisuals):
        for line in range(len(gameVisuals)):
            currentLine = list(gameVisuals[line])
            currentLine = currentLine[2:]
            currentLine.insert(0, "> ")
            gameVisuals[line] = currentLine
        return gameVisuals

    def RunGame(gameVisuals, printWhat):
        # print the full list in seperate lines
        def PrintLines():
            for line in range(20):
                print(*gameVisuals[line], sep='')

        # print the full list in seperate numbered lines
        def PrintNumberedLines():
            for lineNumber in range(20):
                line = gameVisuals[lineNumber]
                line = list(map(lambda x: x.replace(
                    '>', f"{str(lineNumber)}>"), line))
                print(*line, sep="")

        if (printWhat == "Numbered"):
            PrintNumberedLines()
        elif (printWhat == "Default"):
            PrintLines()
        else:
            print("Error, non existent game type!")


class Physiscs:

    # add shapes in positions, multiple sizes
    def AddShapes(gameVisuals, shape, size, coordX, coordY):
        coordX = coordX+1
        coordY = coordY-1
        halfSize = math.floor(size/2)

        def AddLine():
            currentLine = gameVisuals[coordY]
            for CurrentCoordX in range((size)):
                currentLine[(coordX - halfSize)+1+CurrentCoordX] = "-"
            gameVisuals[coordY] = currentLine
            finalGameVisuals = Graphics.OverWriteBorders(gameVisuals)
            return finalGameVisuals

        def AddSquare():
            def SizeOne():
                line = list(gameVisuals[coordY])
                line.pop(coordX+2)
                line.insert(coordX, "*")
                gameVisuals[coordY] = line
                return gameVisuals

            def SizeTwo():
                for counter in range(2):
                    line = list(gameVisuals[(coordY - 1)+counter])
                    for counterTwo in range(size):
                        line[((coordX - 1) + counterTwo)] = "#"
                    gameVisuals[(coordY - 1)+counter] = line
                finalGameVisuals = Graphics.OverWriteBorders(gameVisuals)
                return finalGameVisuals

            def SizeThree():
                for counter in range(math.floor(size/3)*2):
                    line = list(gameVisuals[coordY-math.floor(size/3)+counter])
                    for counterTwo in range(size):
                        line[(coordX - math.floor(size/2)+counterTwo+1)] = "#"
                    gameVisuals[coordY-math.floor(size/3)+counter] = line
                finalGameVisuals = Graphics.OverWriteBorders(gameVisuals)
                return finalGameVisuals

            if (size == 1):
                SizeOne()
            elif (size == 2):
                SizeTwo()
            elif size > 2:
                SizeThree()

        def AddCircle():
            def SizeOne():
                line = list(gameVisuals[coordY])
                line.pop(coordX)
                line.insert(coordX, "*")
                gameVisuals[coordY] = line
                return gameVisuals

            def SizeTwo():

                line = gameVisuals[coordY+1]
                for slotCounter in range((size)):
                    line[((coordX-halfSize+1))+slotCounter+2] = "#"
                gameVisuals[coordY+1] = line

                line = gameVisuals[coordY]
                for slotCounter in range((size)+2):
                    line[(coordX-halfSize)+slotCounter+2] = "#"
                gameVisuals[coordY] = line

                line = gameVisuals[coordY-1]
                for slotCounter in range((size)):
                    line[((coordX-halfSize+1))+slotCounter+2] = "#"
                gameVisuals[coordY-1] = line

                finalGameVisuals = Graphics.OverWriteBorders(gameVisuals)
                return finalGameVisuals

            if (size == 1):
                SizeOne()
            elif size > 1:
                SizeTwo()

        match shape:
            case "Square":
                AddSquare()
            case "Circle":
                AddCircle()
            case "Line":
                AddLine()

        return gameVisuals

    def gravity():
        pass



class Game:

    def ResetGraphics():
        gameVisuals = Graphics.CreateDefaultList()
        return gameVisuals

    def GameLoop(gameVisuals, borderType):
        while True:
            Graphics.RunGame(gameVisuals, borderType)
            for _ in range(7):
                time.sleep(0.1)
                if keyboard.is_pressed("esc"):
                    return

    def Start(startUp, borderType):
        gameVisuals = Game.ResetGraphics()
        #TYPE SHAPES FROM HERE
        #Physiscs.AddShapes(gameVisuals, "Shape", Size, X, Y)



        Physiscs.AddShapes(gameVisuals, "Square", 5, 54, 10)
        Physiscs.AddShapes(gameVisuals, "Circle", 1, 25, 15)
        Physiscs.AddShapes(gameVisuals, "Line", 20, 25, 20)



        #TO HERE
        if startUp == "Single":
             Graphics.RunGame(gameVisuals, borderType)
        elif startUp == "Loop":
            gameVisuals = Game.ResetGraphics()
            Game.GameLoop(gameVisuals, borderType)

#Game.Start("RunTypes", "BorderTypes")
Game.Start("Loop", "Default")
print("EndOfProgram")

#RunTypes = Single/Loop
#BorderTypes = Default/Numbered
