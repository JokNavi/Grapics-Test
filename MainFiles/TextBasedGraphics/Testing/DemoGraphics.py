import keyboard
import time


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
            currentLine = CreateCurrentLine()
            for line in range(20):
                gameVisuals.append(currentLine)
            return gameVisuals

        gameVisuals = DefaultFullList()
        return gameVisuals

    def OverWriteBorders(gameVisuals):
        for line in range(len(gameVisuals)):
            currentLine = list(gameVisuals[line])
            currentLine.pop(0)
            currentLine.pop(1)
            currentLine.insert(0, ">")
            currentLine.insert(1, " ")
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
    def AddShapes(shape, size, CoordX, CoordY):
        CoordX = CoordX*3
        CoordY = CoordY - 1
        gameVisuals = Graphics.CreateDefaultList()

        def AddFloor():
            currentLine = ["> "]
            for item in range(20*3):
                currentLine.append("_")
            gameVisuals[CoordY] = currentLine
            return gameVisuals

        def AddSquare():
            def SizeOne():
                currentY = list(gameVisuals[CoordY])
                currentY.pop(CoordX)
                currentY.insert(CoordX, "*")
                gameVisuals[CoordY] = currentY
                return gameVisuals

            def SizeTwo():
                halfSize = int(size / 2)
                currentY = list(gameVisuals[CoordY-halfSize])
                currentX = CoordX - halfSize
                for counter in range(size):
                    for item in range((size*2)+halfSize):
                        currentY.pop(currentX + item)
                        currentY.insert(currentX + item, "=")
                    gameVisuals[CoordY+counter] = currentY
                    currentY = list(gameVisuals[CoordY-halfSize+counter])

                finalGameVisuals = Graphics.OverWriteBorders(gameVisuals)
                return finalGameVisuals

            if(size == 1):
                SizeOne()
            elif size > 1:
                SizeTwo()

        def AddCircle():
            def SizeOne():
                currentY = list(gameVisuals[CoordY])
                currentY.pop(CoordX)
                currentY.insert(CoordX, "*")
                gameVisuals[CoordY] = currentY
                return gameVisuals

            def SizeTwo():
                # Top Line
                currentY = list(gameVisuals[CoordY+1])
                currentX = CoordX - 1
                for item in range(3):
                    currentY.pop(currentX + item)
                    currentY.insert(currentX + item, "=")
                gameVisuals[CoordY+1] = currentY

                # Center Line
                currentY = list(gameVisuals[CoordY])
                currentX = CoordX - 3
                for item in range(7):
                    currentY.pop(currentX + item)
                    currentY.insert(currentX + item, "=")
                gameVisuals[CoordY] = currentY

                # Bottom Line
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
    def gameLoop(gameVisuals):
        while True:
            Graphics.RunGame(gameVisuals, "Default")
            time.sleep(0.5)
            if keyboard.is_pressed("esc"):
                break

    gameVisuals = Graphics.CreateDefaultList()
    gameVisuals = Physiscs.AddShapes("Circle", 2, 10, 10)
    # gameLoop(gameVisuals)

    Graphics.RunGame(gameVisuals, "Numbered")


Game()
