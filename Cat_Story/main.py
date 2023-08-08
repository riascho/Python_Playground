import tkinter as tk
from PIL import Image, ImageTk

window = tk.Tk()
window.title("A CAT STORY")
window.geometry("800x600")

pic0 = tk.PhotoImage(file="pictures/Starter.png").subsample(2)
pic1 = tk.PhotoImage(file="pictures/GoToWork.png").subsample(2)
pic1a = tk.PhotoImage(file="pictures/LeaveToy.png").subsample(2)
pic1b = tk.PhotoImage(file="pictures/WontBeLong.png").subsample(2)
pic1end = ImageTk.PhotoImage(Image.open("pictures/UnhappyEnding.jpg"))
pic2 = tk.PhotoImage(file="pictures/FeedTheCat.png").subsample(2)
pic2a = tk.PhotoImage(file="pictures/WrongFood.png").subsample(2)
pic2b = tk.PhotoImage(file="pictures/RightFood.png").subsample(3)
pic2end = ImageTk.PhotoImage(Image.open("pictures/HappyEnding.jpg"))

label0 = tk.Label(text="Your Cat seems pretty unhappy! What to do??")
label1 = tk.Label(text="You think that's a good Idea?")
label1end = tk.Label(text="Oh No! That didn't end well...")
label2 = tk.Label(text="What do you wanna give the cat?")
label2end = tk.Label(text="Aw, someone made the right choice! Happy Cat Happy Life")


def unpack():
    label0.pack_forget()
    button01.pack_forget()
    button02.pack_forget()
    label1.pack_forget()
    label1end.pack_forget()
    label2.pack_forget()
    label2end.pack_forget()
    button11.pack_forget()
    button12.pack_forget()
    button21.pack_forget()
    button22.pack_forget()
    button_continue1.pack_forget()
    button_continue2.pack_forget()
    button_again.pack_forget()

def run1():
  canvas.itemconfig(container, image=pic1)
  unpack()
  label1.pack()
  button11.pack()
  button12.pack()

def run1a():
    canvas.itemconfig(container, image=pic1a)
    unpack()
    label1.pack()
    button_continue1.pack()

def run1b():
    canvas.itemconfig(container, image=pic1b)
    unpack()
    label1.pack()
    button_continue1.pack()

def run1end():
    canvas.itemconfig(container, image=pic1end)
    unpack()
    label1end.pack()
    button_again.pack()

def run2():
    canvas.itemconfig(container, image=pic2)
    unpack()
    label2.pack()
    button21.pack()
    button22.pack()

def run2a():
    canvas.itemconfig(container, image=pic2a)
    unpack()
    label1.pack()
    button_continue1.pack()

def run2b():
    canvas.itemconfig(container, image=pic2b)
    unpack()
    label1.pack()
    button_continue2.pack()

def run2end():
    canvas.itemconfig(container, image=pic2end)
    unpack()
    label2end.pack()
    button_again.pack()

def run0():
    canvas.itemconfig(container, image=pic0)
    unpack()
    label0.pack()
    button01.pack()
    button02.pack()
    return


button01 = tk.Button(text="Option 1: I'm late for work - I need to go!", command=run1)
button02 = tk.Button(text="Option 2: You look hungry. Here, I'll feed you!", command=run2)
button11 = tk.Button(text="Option 1: I will leave you a toy though", command=run1a)
button12 = tk.Button(text="Option 2: I won't be gone too long...", command=run1b)
button21 = tk.Button(text="Option 1: This food kinda needs to go... So here you are!", command=run2a)
button22 = tk.Button(text="Option 2: I'll give you your favorite food!", command=run2b)
button_continue1 = tk.Button(text="let's see what happens..", command=run1end)
button_continue2 = tk.Button(text="let's see what happens..", command=run2end)
button_again = tk.Button(text="Start again?", command=run0)

# MAIN

canvas = tk.Canvas(window, width=600, height=300)
canvas.pack()
container = canvas.create_image(250, 200, image=pic0)

label0.pack()

button01.pack()
button02.pack()

tk.mainloop()

# MAIN