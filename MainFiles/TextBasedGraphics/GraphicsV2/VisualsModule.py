# Graphics() (class) is used for anyhing to do with graphics related, also governs the default settings __init__().
# Graphics() is called from GameManager() and GameLoop(GameManager) for running the graphics created with the Screen(Graphics) sub-class.
class Graphics():
    def __init__(self, LOWER, PREFIX, BORDER, SCREENSIZE):
        self.LOWER = LOWER
        self.PREFIX = PREFIX
        self.BORDER = BORDER
        self.SCREENSIZE = SCREENSIZE
        self.XSCREENSIZE = (SCREENSIZE*3)+2
        self.YSCREENSIZE = SCREENSIZE+2


# Screen(Graphics) (sub-class) is used for creating the default screen components such as the ScreenBorder() and DefaultScreen() functions.
class Screen(Graphics):
    def __init__(self, LOWER, PREFIX, BORDER, SCREENSIZE):
        super().__init__(LOWER, PREFIX, BORDER, SCREENSIZE)

    def LowerFrame(self):
        lowerList = [" " for _ in range(self.LOWER)]
        print(*lowerList, sep="\n")

    def PrintScreen(self, gameVisuals):
        for key, value in gameVisuals.items():
            print(*value, sep="")

    def DefaultScreen(self):
        emptyLine = [" " for _ in range(self.XSCREENSIZE)]
        screenHeightGen = ((self.YSCREENSIZE-1)-i for i in range(self.YSCREENSIZE))
        gameVisuals = {n: list(emptyLine) for n in screenHeightGen}
        return gameVisuals

    def RefreshBorder(self, gameVisuals):
        if self.PREFIX == "Numbered":
            for key, value in gameVisuals.items():
                for i in range(len(str(key))):
                    value[i] = str(key)[i]
                value[self.XSCREENSIZE-1] = self.BORDER
        else:
            for key, value in gameVisuals.items():
                for count, char in enumerate([*self.PREFIX]):
                    value[count] = char
                value[self.XSCREENSIZE-1] = self.BORDER

        gameVisuals[self.YSCREENSIZE-1] = gameVisuals[0] = [self.BORDER for _ in range(self.XSCREENSIZE)]
        return gameVisuals


# AddShapes(Graphics) (sub-class) creates the different shapes in the governing gameVisuals Variable.
# AddShapes(Graphics) gets his input parameters from GameManager().
