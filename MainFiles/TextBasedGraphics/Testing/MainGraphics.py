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
        #Creates a single line as a list, takes self.prefix and self.spacing as input
        def CreateALine():
            line = []
            line.extend(self.prefix)
            for _ in range(self.xScreenSize):
                line.extend(self.spacing)
            line.extend(self.border)
            return line

        #Create gameVisual list and add a border, no matter if it's empty or not
        gameVisuals = []
        borderLine = []
        for _ in range(self.xScreenSize+len(self.prefix)+1):
            borderLine.append(self.border)

        gameVisuals.append(borderLine)
        for _ in range(self.yscreenSize):
            gameVisuals.append(CreateALine())
        gameVisuals.append(borderLine)
        return gameVisuals

    def RunGame(self, gameVisuals):
        for lineCounter in range(len(gameVisuals)):
            print(*gameVisuals[lineCounter], sep = "")

    def LowerFrame(self, lower):
        LowerList = []
        for _ in range(lower):
            LowerList.append(" ")
        print(*  LowerList, sep ="\n")

class GameHandler:
    def InputHandler():
        screenSize = 25
        prefix = "->"
        spacing = " "
        border = "#"
        return screenSize, prefix, spacing, border

    def GameLoop(GRAPHICS, gameVisuals):
        GRAPHICS.RunGame(gameVisuals)
        while True:
                time.sleep(0.05)
                if keyboard.is_pressed("esc"):
                    return
                if keyboard.is_pressed("space"):
                    GRAPHICS.LowerFrame(30)
                    GRAPHICS.RunGame(gameVisuals) 
                    time.sleep(0.02)

    screenSize, prefix, spacing, border = InputHandler()
    GRAPHICS = Graphics(screenSize, prefix, spacing, border)
    gameVisuals = GRAPHICS.CreateDefaultFrame()
    GameLoop(GRAPHICS, gameVisuals)
    