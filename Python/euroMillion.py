# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import random
from Tkinter import *

root = Tk()

root.title("Simple GUI")
root.geometry("200x100")

root.mainloop()

ran5 = sorted(random.sample(range(1,50), 5))
ran2 = sorted(random.sample(range(1, 12), 2))
print ran5
print ran2

euroMillion = ran5 + ran2

print euroMillion