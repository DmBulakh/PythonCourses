import tkinter as tk
import os

mainWindow = tk.Tk()
mainWindow.title("Grid demo")
mainWindow.geometry('640x800+8+200')

label = tk.Label(mainWindow, text="Tkinter grid demo")
label.grid(row=0, column=0, columnspan=3)

mainWindow.columnconfigure(0, weight=1)
mainWindow.columnconfigure(1, weight=1)
mainWindow.columnconfigure(2, weight=1)
mainWindow.columnconfigure(3, weight=1)
mainWindow.columnconfigure(4, weight=1)

mainWindow.rowconfigure(0, weight=1)
mainWindow.rowconfigure(1, weight=10)
mainWindow.rowconfigure(2, weight=1)
mainWindow.rowconfigure(3, weight=3)
mainWindow.rowconfigure(4, weight=3)

fileList = tk.Listbox(mainWindow)
fileList.grid(row=1, column=0, sticky='nsew', rowspan=2)
fileList.config(border=2, relief='sunken')

for zone in os.listdir('/Windows/System32'):
    fileList.insert(tk.END, zone)

listScroll = tk.Scrollbar(mainWindow, orient=tk.VERTICAL, command=fileList.yview)
listScroll.grid(row=1, column=1, sticky='nsw', rowspan=2)
fileList['yscrollcommand'] = listScroll.set

optionFrame = tk.LabelFrame(mainWindow, text="File Details ")
optionFrame.grid(row=1, column=2, sticky='ne')

rbValue = tk.IntVar()
rbValue.set(2)

radio1 = tk.Radiobutton(optionFrame, text="Filename", value=1, variable=rbValue)
radio2 = tk.Radiobutton(optionFrame, text="Path", value=2, variable=rbValue)
radio3 = tk.Radiobutton(optionFrame, text="Timestamp", value=3, variable=rbValue)

radio1.grid(row=0, column=0, sticky='w')
radio2.grid(row=1, column=0, sticky='w')
radio3.grid(row=2, column=0, sticky='w')


mainWindow.mainloop()
