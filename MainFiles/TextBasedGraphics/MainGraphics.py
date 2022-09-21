import math
import keyboard
import time

errorMesage = ""


class Graphics:
    def __init__(self, screenSize, prefix, spacing, border):
        self.YSCREENSIZE = screenSize
        self.XSCREENSIZE = screenSize*3
        self.PREFIX = prefix
        self.SPACING = spacing
        self.BORDER = border

    def CreateDefaultFrame(self):
        # Creates a single line as a list, takes self.prefix and self.spacing as input
        def CreateALine():
            line = [self.SPACING for _ in range(self.XSCREENSIZE)]
            line.insert(0, "->")
            line.append(self.BORDER)
            return line

        # Create gameVisual list and add a border, no matter if it's empty or not
        borderLine = [self.BORDER for _ in range(
            self.XSCREENSIZE+len(self.PREFIX)+1)]
        gameVisuals = [CreateALine() for _ in range(self.YSCREENSIZE)]
        gameVisuals.insert(0, borderLine)
        gameVisuals.append(borderLine)
        return gameVisuals

    def PlayFrame(self, gameVisuals):
        for lineCounter in range(len(gameVisuals)):
            print(*gameVisuals[lineCounter], sep="")

    def LowerFrame(self, lower):
        lowerList = [" " for _ in range(lower)]
        print(*lowerList, sep="\n")


class AddVisuals:
    def __init__(self, SCREENSIZE):
        self.YSCREENSIZE = SCREENSIZE
        self.XSCREENSIZE = SCREENSIZE*3

    def ShapeInputHandler(self, SCREENSIZE):
        print("#ADD-SHAPE-MENU! \n")
        print("- Shapes can be: Dot, Line")
        print(f"- Size can be: 1 to {SCREENSIZE}")
        print(f"- X Coords can be: 1 to {SCREENSIZE*3}\n")
        print("Input your desired shape and size down below.")
        return

    def CheckBorder(self, GAMEVISUALS, LINE, slotValue):
        hits = ["Hit" for _ in range(1) if LINE.index(slotValue) == 0 or LINE.index(
            slotValue) == self.XSCREENSIZE or GAMEVISUALS.index(LINE) == 0 or GAMEVISUALS.index(LINE) == self.YSCREENSIZE]
        if len(hits) > 0:
            return True
        else:
            return False

    def IsEven(self, SIZE):
        if(SIZE % 2 == 0):
            return 0
        else:
            return 1

    def AddDot(self, gameVisuals, X, Y):
        LINE = gameVisuals[Y]
        LINE[X] = "*"
        gameVisuals[Y] = LINE
        return gameVisuals

    def AddLine(self, gameVisuals, SIZE, X, Y):
        slotValue = "-"
        ISEVEN = AddVisuals.IsEven(self, SIZE)
        HALFSIZE = math.floor(SIZE/2)
        LINE = gameVisuals[Y]
        LINE[(X-HALFSIZE):(X+HALFSIZE)+ISEVEN] = [slotValue for _ in range(SIZE)]
        if(AddVisuals.CheckBorder(self, gameVisuals, LINE, slotValue)):
            global errorMesage
            errorMesage = "Error. Cannot place shape there as it would overlap with the border."
            gameVisuals = gameVisuals
        else:
            gameVisuals[Y] = LINE
        return gameVisuals


class GameHandler:

    def GraphicsInputHandler(self):
        lower = 30
        screenSize = 24
        prefix = "->"
        spacing = " "
        border = "#"
        return lower, screenSize, prefix, spacing, border

    def ErrorHandler():
        global errorMesage
        print(errorMesage)
        errorMesage = ""

    def GameLoop(self, GRAPHICS, gameVisuals, LOWER, SCREENSIZE):
        ADDVISUALS = AddVisuals(SCREENSIZE)
        GRAPHICS.PlayFrame(gameVisuals)
        while True:
            time.sleep(0.05)
            if keyboard.is_pressed("esc"):
                print("Program closing...")
                return
            elif keyboard.is_pressed("space"):
                GRAPHICS.LowerFrame(LOWER)
                GRAPHICS.PlayFrame(gameVisuals)
                time.sleep(0.02)
            elif keyboard.is_pressed("a"):
                # ADDVISUALS.ShapeInputHandler(SCREENSIZE)
                gameVisuals = ADDVISUALS.AddLine(gameVisuals, 3, 1, 3)
                GRAPHICS.LowerFrame(LOWER)
                GRAPHICS.PlayFrame(gameVisuals)
                time.sleep(0.02)
            elif(len(errorMesage) > 0):
                GameHandler.ErrorHandler()


class InitiateProgram:

    GAMEHANDLER = GameHandler()
    LOWER, SCREENSIZE, PREFIX, SPACING, BORDER = GAMEHANDLER.GraphicsInputHandler()
    GRAPHICS = Graphics(SCREENSIZE, PREFIX, SPACING, BORDER)
    gameVisuals = GRAPHICS.CreateDefaultFrame()
    GAMEHANDLER.GameLoop(GRAPHICS, gameVisuals, LOWER, SCREENSIZE)


InitiateProgram()
