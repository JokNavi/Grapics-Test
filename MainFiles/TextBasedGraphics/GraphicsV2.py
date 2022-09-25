# Graphics() (class) is used for anyhing to do with graphics related, also governs the default settings __init__().
# Graphics() is called from GameManager() and GameLoop(GameManager) for running the graphics created with the Screen(Graphics) sub-class.


class Graphics():
    def __init__(self, SCREENSIZE):
        self.SCREENSIZE = SCREENSIZE
        self.XSCREENSIZE = (SCREENSIZE*3)+1
        self.YSCREENSIZE = SCREENSIZE+1

# Screen(Graphics) (sub-class) is used for creating the default screen components such as the ScreenBorder() and DefaultScreen() functions.
class Screen(Graphics):
    def __init__(self, LOWER, PREFIX, BORDER, SCREENSIZE):
        super().__init__(SCREENSIZE)
        self.LOWER = LOWER
        self.PREFIX = PREFIX
        self.BORDER = BORDER

    def LowerFrame(self):
        lowerList = [" " for _ in range(self.LOWER)]
        print(*lowerList, sep="\n")

    def PrintScreen(self, gameVisuals):
        for key, value in gameVisuals.items():
            print(*value, sep="")

    def DefaultScreen(self):
        emptyLine = [" " for _ in range(self.XSCREENSIZE)]
        screenHeighteGen = ((self.YSCREENSIZE-1)-i for i in range(self.YSCREENSIZE))
        gameVisuals = {n: emptyLine for n in screenHeighteGen}
        return gameVisuals

    def RefreshBorder(self, gameVisuals):
        for key, value in gameVisuals.items():
            for count, char in enumerate([*self.PREFIX]):
                value[count] = char
            value[self.XSCREENSIZE-1] = self.BORDER
        gameVisuals[self.YSCREENSIZE-1] = gameVisuals[0] = [self.BORDER for _ in range(self.XSCREENSIZE)]
        return


SCREEN = Screen(10, "->", "#", 25)
gameVisuals = SCREEN.DefaultScreen()
SCREEN.RefreshBorder(gameVisuals)
SCREEN.PrintScreen(gameVisuals)


# Shapes(Graphics) (sub-class) is used for handeling shape inputs refering them to his own sub-class; AddShapes(Shapes).

# AddShapes(Shapes) (sub-class) creates the different shapes in the governing gameVisuals Variable.
# AddShapes(Shapes) gets his input parameters from Shapes(Graphics).

# GameManager() (class) is used for handeling the different startup modes and input parameters.
# Once done, GameManager() sends his finished parameters to GameLoop(GameManager).

# GameLoop() (Function) handles the main game loop. With inputs from GameManager
