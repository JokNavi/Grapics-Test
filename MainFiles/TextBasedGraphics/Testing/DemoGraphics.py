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

        if(printWhat == "Numbered"):
            PrintNumberedLines()
        elif(printWhat == "Default"):
            PrintLines()
        else:
            print("Error, non existent game type!")


class Physiscs:

    # add shapes in positions, multiple sizes
    def AddShapes(gameVisuals, shape, size, coordX, coordY):
        coordX = (coordX*3)-1
        coordY = coordY-1

        def AddFloor():
            currentLine = ["> "]
            for item in range(20*3):
                currentLine.append("_")
            gameVisuals[coordY] = currentLine
            return gameVisuals

        def AddSquare():
            def SizeOne():
                line = list(gameVisuals[coordY])
                line.pop(coordX)
                line.insert(coordX, "#")
                gameVisuals[coordY] = line
                return gameVisuals

            def SizeTwo():
                for counter in range(size):
                    line = list(gameVisuals[coordY+math.floor(size/2)+counter])
                    for counterTwo in range(size*3):
                        line[coordX - math.floor(size/2)+counterTwo-1] = "#"
                    gameVisuals[coordY + math.floor(size/2)+counter] = line
                finalGameVisuals = Graphics.OverWriteBorders(gameVisuals)
                return finalGameVisuals

            if(size == 1):
                SizeOne()
            elif size > 1:
                SizeTwo()

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
                    line[((coordX-math.floor(size/2)+1))+slotCounter] = "#"
                gameVisuals[coordY+1] = line

                line = gameVisuals[coordY]
                for slotCounter in range((size)+2):
                    line[(coordX-math.floor(size/2))+slotCounter] = "#"
                gameVisuals[coordY] = line

                line = gameVisuals[coordY-1]
                for slotCounter in range((size)):
                    line[((coordX-math.floor(size/2)+1))+slotCounter] = "#"
                gameVisuals[coordY-1] = line
                    
                finalGameVisuals = Graphics.OverWriteBorders(gameVisuals)
                return finalGameVisuals

            if(size == 1):
                SizeOne()
            elif size > 1:
                SizeTwo()

        match shape:
            case "Square":
                AddSquare()
            case "Circle":
                AddCircle()
            case "Floor":
                AddFloor()

        return gameVisuals

    def gravity():
        pass


class Game:
    def ResetGraphics():
        gameVisuals = Graphics.CreateDefaultList()
        return gameVisuals

    def gameLoop(gameVisuals):
        while True:
            Graphics.RunGame(gameVisuals, "Default")
            time.sleep(0.5)
            if keyboard.is_pressed("esc"):
                break
            elif keyboard.is_pressed("r"):
                gameVisuals = Game.ResetGraphics()
            elif keyboard.is_pressed("p"):
                shapeInput = input()

    gameVisuals = Graphics.CreateDefaultList()
    gameVisuals = Physiscs.AddShapes(gameVisuals, "Square", 3, 10, 10)
    gameVisuals = Physiscs.AddShapes(gameVisuals, "Square", 1, 10, 10)
    # gameLoop(gameVisuals)

    Graphics.RunGame(gameVisuals, "Default")


Game()
