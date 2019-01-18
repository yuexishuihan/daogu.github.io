from tkinter import *
import tkinter.simpledialog as dl
import tkinter.messagebox as mb

root = Tk()
w = Label(root,text = '猜数字')
w.pack()

mb.showinfo('Welcome','欢迎来到猜数字')
number = 67
while True:
    guess = dl.askinteger('Number','请输入一个数字')
    if guess == number:
        output = '回答正确'
        mb.showinfo('输出:',output)
        break
    elif guess < number:
        output = '数字太小'
        mb.showinfo('提示:',output)
    else:
        output = '数字太大'
        mb.showinfo('提示:',output)


# output = 'This is output message!'
# mb.showinfo('Output:',output)