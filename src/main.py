import sys
import tkinter as tk
from src.rstree import build_rs_tree
from src.gui import RSTreeApp

if __name__ == "__main__":
    rs_tree, object_array = build_rs_tree()
    root = tk.Tk()
    app = RSTreeApp(root, rs_tree)
    root.mainloop()