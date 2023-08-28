#Import necessary library
import tkinter as tk

#create the main application window
root = tk.Tk()

#name the title of the window
root.title("Drone APP")

#set dimensions of the window
root.geometry("400*300")

#add widgets(buttons,labels e.t.c) to the window
label = tk.Label(root, text="welcome to drone control application")
label.pack()

button = tk.Button(root, text="Click to start")
button.pack()

#start the main event loop
root.mainloop


