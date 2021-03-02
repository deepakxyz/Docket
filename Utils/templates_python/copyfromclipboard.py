import tkinter as tk

def getClipboardText():
    root = tk.Tk()
    root.withdraw()
    try:
        clipboard =  root.clipboard_get()
        return clipboard
    except:
        clipboard = ''
        return clipboard


    