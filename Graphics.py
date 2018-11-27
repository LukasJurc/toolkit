import tkinter as tk
    
# function opens a new window
def create_window1():
    window1 = tk.Toplevel(root)
    tk.Label(window1, text='your text').pack(padx=30, pady=30)
    
    
def create_window2():
    window2 = tk.Frame(root)
    
def create_window3():
    window3 = tk.Toplevel(root)
    
def create_window4():
    window4 = tk.Toplevel(root)
    
root = tk.Tk()
frame = tk.Frame(root)
frame.pack()

slogan = tk.Button(frame,
                   text="Button 1",
                   command=create_window1)
slogan.pack(side=tk.LEFT)

slogan = tk.Button(frame,
                   text="Button 2",
                   command=create_window2)
slogan.pack(side=tk.LEFT)

slogan = tk.Button(frame,
                   text="Button 3",
                   command=create_window3)
slogan.pack(side=tk.LEFT)

slogan = tk.Button(frame,
                   text="Button 4",
                   command=create_window4)
slogan.pack(side=tk.LEFT)

root.mainloop()