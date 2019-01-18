from tkinter import *
import tkinter.simpledialog as dl
import tkinter.messagebox as mb

root = Tk()
w = Label(root,text = '主窗口')
w.pack()

mb.showinfo('Welcome','Welcome Message')
guess = dl.askinteger('Number','Enter a number')

output = 'This is output message!'
mb.showinfo('Output:',output)