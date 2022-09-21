import time
import copy
import keyboard

errorMesage = ""
devMode = False


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
        numberdBorder = ["0" + str(numberdBorder[counter]) if numberdBorder[counter]
                         < 10 else str(numberdBorder[counter]) for counter in range(self.YSCREENSIZE)]

        borderLine = [self.BORDER for _ in range(
            self.XSCREENSIZE+len(self.PREFIX)+1)]
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
        print("\n#ADD-SHAPE-MENU!\n")
        print("- Shapes can be: Dot, Line")
        print(f"- Size can be: 1 to {SCREENSIZE}")
        print(f"- X Coords can be: 1 to {SCREENSIZE*3}\n")
        print("Input your desired shape, size, X and Y down below.")
        print("Use this format: Shape, Size, X, Y")
        SHAPE, SIZE, X, Y = input(">: ").split(",")
        return SHAPE, int(SIZE), int(X), int(Y)

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

    def GraphicsInputHandler(self):
        borderMode = "Numbered"
        lower = 30
        screenSize = 24
        prefix = "->"
        spacing = " "
        border = "#"
        return borderMode, lower, screenSize, prefix, spacing, border

    def ErrorHandler():
        global errorMesage
        print(errorMesage)
        errorMesage = ""

    def GameLoop(self, GRAPHICS, gameVisuals, LOWER, SCREENSIZE):
        if(len(errorMesage) > 0):
            GameHandler.ErrorHandler()
            return "Error!"
        INTROMESSAGE = [" " for _ in range(
            ((SCREENSIZE*3)-len("Welcome to my favorite project so far."))//2)]
        INTROMESSAGE.append("Welcome to my favorite project so far.")
        INTROMESSAGEBOTTOM = [" " for _ in range(
            ((SCREENSIZE*3)-len("MySimpleScreen"))//2)]
        INTROMESSAGEBOTTOM.append("MySimpleScreen")
        ADDVISUALS = AddVisuals(SCREENSIZE)
        GRAPHICS.PlayFrame(gameVisuals)

        while True:
            time.sleep(0.05)
            if keyboard.is_pressed("esc"):
                print("Program closing...")
                return
            elif keyboard.is_pressed("space"):
                GRAPHICS.LowerFrame(LOWER)
                print(*INTROMESSAGE, sep="")
                print(*INTROMESSAGEBOTTOM, sep="")
                GRAPHICS.PlayFrame(gameVisuals)
                time.sleep(0.02)
            elif keyboard.is_pressed("a"):
                if devMode:
                    ADDVISUALS.AddDot(gameVisuals, 10, 5)
                    GRAPHICS.LowerFrame(LOWER)
                    print(*INTROMESSAGE, sep="")
                    print(*INTROMESSAGEBOTTOM, sep="")
                    GRAPHICS.PlayFrame(gameVisuals)
                    time.sleep(0.02)
                else:
                    shape, size, x, y = ADDVISUALS.ShapeInputHandler(
                        SCREENSIZE)
                    if size == 0:
                        print("Error. Size can't be 0.")
                    else:
                        match shape:
                            case "Dot":
                                ADDVISUALS.AddDot(gameVisuals, x, y)
                            case "Line":
                                gameVisuals = ADDVISUALS.AddLine(
                                    gameVisuals, size, x, y)
                        GRAPHICS.LowerFrame(LOWER)
                        print(*INTROMESSAGE, sep="")
                        print(*INTROMESSAGEBOTTOM, sep="")
                        GRAPHICS.PlayFrame(gameVisuals)

                        time.sleep(0.02)
            elif(len(errorMesage) > 0):
                GameHandler.ErrorHandler()


class InitiateProgram:

    GAMEHANDLER = GameHandler()
    BORDERMODE, LOWER, SCREENSIZE, PREFIX, SPACING, BORDER = GAMEHANDLER.GraphicsInputHandler()
    GRAPHICS = Graphics(SCREENSIZE, PREFIX, SPACING, BORDER)
    gameVisuals = GRAPHICS.CreateDefaultFrame(BORDERMODE)
    GAMEHANDLER.GameLoop(GRAPHICS, gameVisuals, LOWER, SCREENSIZE)


InitiateProgram()
