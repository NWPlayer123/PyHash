from sys import argv
from hashlib import md5
from tkinter import Tk, Entry

try:
    with open(argv[1], "rb") as f:
        hashed = md5(f.read())
        hashed = hashed.hexdigest().upper()
        root = Tk()
        root.title("Hash")
        root.resizable(0, 0)
        e = Entry(root, width=35)
        e.pack()
        e.insert(0, hashed)
        e.configure(state="readonly")
        root.mainloop()
except:
        root = Tk()
        root.title("Hash")
        root.resizable(0, 0)
        e = Entry(root, width=35)
        e.pack()
        e.insert(0, "No input file")
        e.configure(state="readonly")
        root.mainloop()
