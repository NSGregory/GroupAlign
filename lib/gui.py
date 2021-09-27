from tkinter import Tk
from tkinter.filedialog import askopenfilename

"""Gui related functions for the GroupAlign project"""


class selectFile:
    """Contains methods for selecting the filename using a GUI.  Currently relies only on tkinter (3.x).  Will not work
    well with 2.x or earlier."""

    def __init__(self):
        self.name = None

    def byGui():
        Tk().withdraw()
        return askopenfilename()

if __name__ == '__main__':
    file = selectFile.byGui()
    #file.byGui()
    print(file)