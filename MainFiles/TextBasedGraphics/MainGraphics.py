import keyboard
import time


class Graphics:
    def __init__(self, screenSize, prefix, spacing, border):
        self.yscreenSize = screenSize
        self.xScreenSize = screenSize*3
        self.prefix = prefix
        self.spacing = spacing
        self.border = border

    def CreateDefaultFrame(self):
        # Creates a single line as a list, takes self.prefix and self.spacing as input
        def CreateALine():
            line = [self.spacing for _ in range(self.xScreenSize)]
            line.insert(0, "->")
            line.append(self.border)
            return line

        # Create gameVisual list and add a border, no matter if it's empty or not
        borderLine = [self.border for _ in range(
            self.xScreenSize+len(self.prefix)+1)]
        gameVisuals = [CreateALine() for _ in range(self.yscreenSize)]
        gameVisuals.insert(0, borderLine)
        gameVisuals.append(borderLine)
        return gameVisuals

    def RunGame(self, gameVisuals):
        for lineCounter in range(len(gameVisuals)):
            print(*gameVisuals[lineCounter], sep="")

    def LowerFrame(self, lower):
        lowerList = [" " for _ in range(lower)]
        print(*lowerList, sep="\n")


class GameHandler:

    def GraphicsInputHandler(self):
        lower = 30
        
        screenSize = 25
        prefix = "->"
        spacing = " "
        border = "#"       
        return lower, screenSize, prefix, spacing, border

    def GameLoop(self, GRAPHICS, gameVisuals, lower):
        GRAPHICS.RunGame(gameVisuals)
        while True:
            time.sleep(0.05)
            if keyboard.is_pressed("esc"):
                return
            if keyboard.is_pressed("space"):
                GRAPHICS.LowerFrame(lower)  
                GRAPHICS.RunGame(gameVisuals)
                time.sleep(0.02)


class InitiateProgram:
    GAMEHANDLER = GameHandler()

    
    lower, screenSize, prefix, spacing, border = GAMEHANDLER.GraphicsInputHandler()
    GRAPHICS = Graphics(screenSize, prefix, spacing, border)

    gameVisuals = GRAPHICS.CreateDefaultFrame()
    GAMEHANDLER.GameLoop(GRAPHICS, gameVisuals, lower)


InitiateProgram()
