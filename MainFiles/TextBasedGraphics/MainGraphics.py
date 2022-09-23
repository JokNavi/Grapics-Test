from mailbox import mboxMessage
import time
import copy
import keyboard

errorMesage = ""
devMode = False

def ErrorCheck():
    global errorMesage
    if(len(errorMesage) > 1):
        print(errorMesage)
        errorMesage = ""


class Graphics:
    def __init__(self, screenSize, prefix, spacing, border):
        self.YSCREENSIZE = screenSize
        self.XSCREENSIZE = screenSize*3
        self.PREFIX = prefix
        self.SPACING = spacing
        self.BORDER = border

    def CreateDefaultFrame(self, BORDERMODE):
        # Creates a single line as a list, takes self.prefix and self.spacing as input
        def CreateALine(TOKEN):
            line = [self.SPACING for _ in range(self.XSCREENSIZE)]
            line.insert(0, TOKEN)
            line.append(self.BORDER)
            return line

        # Create gameVisual list and add a border, no matter if it's empty or not
        numberdBorder = [counter+1 for counter in range(self.YSCREENSIZE)]
        numberdBorder = ["0" + str(numberdBorder[counter]) if numberdBorder[counter]< 10 else str(numberdBorder[counter]) for counter in range(self.YSCREENSIZE)]
        borderLine = [self.BORDER for _ in range(self.XSCREENSIZE+len(self.PREFIX)+1)]
        if BORDERMODE == "Numbered":
            gameVisuals = [CreateALine(numberdBorder[counter])
                           for counter in range(self.YSCREENSIZE)]
        elif BORDERMODE == "Default":
            gameVisuals = [CreateALine("->") for _ in range(self.YSCREENSIZE)]
        else:
            global errorMesage
            errorMesage = "Error. That border mode doesn't exist yet. :)"

        gameVisuals.insert(0, borderLine)
        gameVisuals.append(borderLine)
        return gameVisuals

    def LowerFrame(self, lower):
        lowerList = [" " for _ in range(lower)]
        print(*lowerList, sep="\n")

    def PlayFrame(self, gameVisuals):
        for lineCounter in range(len(gameVisuals)):
            print(*gameVisuals[lineCounter], sep="")

class AddVisuals:
    def __init__(self, SCREENSIZE):
        self.YSCREENSIZE = SCREENSIZE
        self.XSCREENSIZE = SCREENSIZE*3

    def ShapeInputHandler(SCREENSIZE):
        print("\n#ADD-SHAPE-MENU!\n")
        print("- Shapes can be: Dot, Line")
        print(f"- Size can be: 1 to {SCREENSIZE}")
        print(f"- X Coords can be: 1 to {SCREENSIZE*3}\n")
        print("Input your desired shape, size, X and Y down below.")
        print("Use this format: Shape, Size, X, Y")
        SHAPE, SIZE, X, Y = input(">: ").split(",")
        return SHAPE, int(SIZE), int(X), int(Y)

    def CheckBorder(self, GAMEVISUALS, LINE, SLOTVALUE):
        hits = ["Hit" for _ in range(1) if LINE.index(SLOTVALUE) == 0 or LINE.index(
            SLOTVALUE) == self.XSCREENSIZE or GAMEVISUALS.index(LINE) == 0 or GAMEVISUALS.index(LINE) == self.YSCREENSIZE]
        if (len(hits) > 0):
            return True
        return False


    def IsEven(self, SIZE):
        if(SIZE % 2 == 0):
            return 0
        else:
            return 1

    def AddDot(self, gameVisuals, X, Y):
        OLDGAMEVISUALS = copy.deepcopy(gameVisuals)
        LINE = gameVisuals[Y]
        LINE[X] = "*"
        if(AddVisuals.CheckBorder(self, gameVisuals, LINE, "*")):
            global errorMesage
            errorMesage = "Error. Cannot place shape there as it would overlap with the border."
            return OLDGAMEVISUALS
        else:
            gameVisuals[Y] = LINE
            return gameVisuals
        

    def AddLine(self, gameVisuals, SIZE, X, Y):
        OLDGAMEVISUALS = copy.deepcopy(gameVisuals)
        ISEVEN = AddVisuals.IsEven(self, SIZE)
        HALFSIZE = SIZE//2
        LINE = gameVisuals[Y]
        LINE[(X-HALFSIZE):(X+HALFSIZE)+ISEVEN] = ["-" for _ in range(SIZE)]
        if(AddVisuals.CheckBorder(self, gameVisuals, LINE, "-")):
            global errorMesage
            errorMesage = "Error. Cannot place shape there as it would overlap with the border."
            return OLDGAMEVISUALS
        else:
            gameVisuals[Y] = LINE
            return gameVisuals


class GameHandler:
    def __init__(self, GRAPHICS, LOWER, SCREENSIZE):
        self.LOWER = LOWER
        self.GRAPHICS = GRAPHICS
        self.SCREENSIZE = SCREENSIZE
        self.YSCREENSIZE = SCREENSIZE
        self.XSCREENSIZE = SCREENSIZE*3

    def InitiateFrame(self):
            MESSAGE = ['Welcome to my favorite project so far.','#MyPrintScreen']
            for i in range(2):
                introMessage = [" " for _ in range((((self.SCREENSIZE*3)-len(MESSAGE[i]))//2)+2)]
                introMessage.append(MESSAGE[i])
                print(*introMessage, sep="")

    def AddShapeControlCenter(self, ADDVISUALS, gameVisuals):
        SHAPE, SIZE, X, Y = ADDVISUALS.ShapeInputHandler(self.SCREENSIZE)
        if SIZE < 1 or SIZE > self.YSCREENSIZE: 
            global errorMesage 
            errorMesage = "Error. size was Invalid."
        match SHAPE:
            case "Dot":
                gameVisuals = ADDVISUALS.AddDot(self, gameVisuals, X, Y)
                self.GRAPHICS.LowerFrame(self.LOWER)
                self.InitiateFrame()
                self.GRAPHICS.PlayFrame(gameVisuals)
            case "Line":
                gameVisuals = ADDVISUALS.AddLine(self, gameVisuals, SIZE, X, Y)
                self.GRAPHICS.LowerFrame(self.LOWER)
                self.InitiateFrame()
                self.GRAPHICS.PlayFrame(gameVisuals)
        return gameVisuals
            

    def GameLoop(self, gameVisuals):
        global errorMesage
        self.GRAPHICS.LowerFrame(self.LOWER)
        self.InitiateFrame()
        self.GRAPHICS.PlayFrame(gameVisuals)
        while True:
            ErrorCheck()
            if keyboard.is_pressed("esc"):
                print("Program closing...")
                return "Error. Closed program"
            elif keyboard.is_pressed("space"):
                self.GRAPHICS.LowerFrame(self.LOWER)
                self.InitiateFrame()
                self.GRAPHICS.PlayFrame(gameVisuals)
                time.sleep(0.7)
            elif keyboard.is_pressed("a"):
                self.AddShapeControlCenter(AddVisuals, gameVisuals)
                time.sleep(0.7)

class InitiateProgram():

    def GraphicsInputHandler(self):
        borderMode = "Numbered"
        lower = 30
        screenSize = 24
        prefix = "->"
        spacing = " "
        border = "#"
        return borderMode, lower, screenSize, prefix, spacing, border

    def LoopStart(self):
        BORDERMODE, LOWER, SCREENSIZE, PREFIX, SPACING, BORDER = self.GraphicsInputHandler()
        GRAPHICS = Graphics(SCREENSIZE, PREFIX, SPACING, BORDER)
        GAMEVISUALS = GRAPHICS.CreateDefaultFrame(BORDERMODE)
        GAMEHANDLER = GameHandler(GRAPHICS, LOWER, SCREENSIZE)
        GAMEHANDLER.GameLoop(GAMEVISUALS)

    def DevStart(self):
        BORDERMODE, LOWER, SCREENSIZE, PREFIX, SPACING, BORDER = self.GraphicsInputHandler()
        ADDVISUALS = AddVisuals(SCREENSIZE)
        GRAPHICS = Graphics(SCREENSIZE, PREFIX, SPACING, BORDER)
        gameVisuals = GRAPHICS.CreateDefaultFrame(BORDERMODE)

        gameVisuals = ADDVISUALS.AddDot(gameVisuals, 10, 5)

        GAMEHANDLER = GameHandler(GRAPHICS, LOWER, SCREENSIZE)
        GAMEHANDLER.GameLoop(gameVisuals)

INITIATEPROGRAM = InitiateProgram()
INITIATEPROGRAM.LoopStart()
