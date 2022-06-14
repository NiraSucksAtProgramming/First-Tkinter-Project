from tkinter import *
from time import sleep

root = Tk()
root.geometry("700x400")
root.maxsize(700,400) #This isn't a string, and so it will not use string values like 'X' to define dimensions
root.configure(bg="#5F2900")

number = 0
multiplier = 1


def tapped():
    global number
    global multiplier
    global numberlab

    number += multiplier
    numberlab = Label(root,text=str(number),bg="#5F2900",fg="white",font=("Courier",18))
    numberlab.grid(row=2,column=0,columnspan=2)


def upgradetap():
    global number
    global multiplier
    global upprice
    global numberlab

    if number >= 100:
        numberlab.destroy()
        number -= 100
        multiplier += 1



hello = Label(root,text="Hello World!",bg="#5F2900")
intro = Label(root,text="This is a testing program called Tkinter.",bg="#5F2900",fg="white")
click = Label(root,text="Click this button and the number will appear and rise with every click!",bg="#5F2900",fg="white")


button = Button(root,text="Click Me!",padx=50,pady=50,command=tapped,fg="white",bg="#9C630E")
upgrade = Button(root,text=f"Upgrade\nCost:100",padx=50,pady=20,fg="white",bg="#9C630E",command=upgradetap)
caution = Label(root,text="DISCLAIMER: When upgrading, the number will be\nsubtracted AFTER you click the button again",bg="#5F2900",fg="white")

# label.pack() #Packing it into the window, inefficient and mediocre in comparison to the grid() function.
hello.grid(row=0,column=0) #Row and Column are relative, no row or column can be skipped or ignored in tkinter
intro.grid(row=1,column=0)
click.grid(row=1,column=1)

button.grid(row=2,column=1)
upgrade.grid(row=3,column=0)
caution.grid(row=4,column=0)

root.mainloop()
