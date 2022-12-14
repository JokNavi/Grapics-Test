from turtle import screensize
import keyboard
import numpy as np
from VisualsModule import *

# GameManager() (class) is used for handeling the different startup modes and input parameters.
# Once done, GameManager() sends his finished parameters to GameLoop(GameManager).
class GameManager():
    def __init__(self) -> None:
        pass

    lower = 15
    prefix = "->" 
    border = "##"
    screensize = 25

    def ProgramParam(self, lower, prefix, border, screensize):
        print("\n#SETTINGS-MENU!")
        print(f"Vertical space inbetween frames: {lower}")
        print(f"Line prefix: {prefix}")
        print(f"Border character: {border}")
        print(f"Screen size: {screensize}")
        print(f"\nPRESS \"y\" TO CHANGE THE SETTINGS, \"Esc\" TO CANCEL")
        while True:
            if keyboard.is_pressed("esc"):
                return lower, prefix, border, screensize
            elif keyboard.is_pressed("y"):
                print("\n#INPUT SETTINGS DOWN BELOW!")
                print("0 - \u221E")
                lower = input("New vertical space inbetween frames: ")
                print("\n1 - \u221E")
                screensize = input("New Screen size: ")
                print("\nSingle character: \"#\", \"A\", \"1\", \"$\", ect..")
                border = input("New border character: ")
                print("\nOne or more characters: \"->\", \"#\", \"-\", ect.., or \"Numbered\"")
                prefix = input("Line prefix: ")
                print("\nSending data.\n")
                return lower, prefix, border, screensize

    def ShapeInputs(self, SCREENSIZE, PREFIX):
        print("\n#ADD-SHAPE-MENU!\n")
        print("- Shapes can be: Dot, Line, Circle")
        print(f"- Size can be: 1 to {SCREENSIZE}")
        print(f"- X Coords can be: 1 to {(SCREENSIZE*3)-len(PREFIX)}\n")
        print("Input your desired shape, size, X and Y down below.")
        print("Use this format: Shape, Size, X, Y")
        SHAPE, SIZE, X, Y = input(">: ").split(",")
        return SHAPE, int(SIZE), int(X), int(Y)

    gameVisuals = np.full([(screensize*3)+2, screensize+2]," ", dtype = "U")
    Graphics = Graphics(lower, prefix, border, screensize)
    Graphics.RefreshBorder(gameVisuals)

#print(GameManager.ProgramParam("no", 10, "->", "#", 10))

# GameLoop() (Function) handles the main game loop. With inputs from GameManager
