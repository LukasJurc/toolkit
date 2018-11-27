import tkinter as tk

root = tk.Tk()
frame = tk.Frame(root)
frame.pack()
    
# function opens a new window
def create_window1():
    
    class Example(tk.Frame):
        def __init__(self, parent):
            tk.Frame.__init__(self, parent)

        # create a prompt, an input box, an output label,
        # and a button to do the computation
            self.prompt = tk.Label(self, text="Search for a word:", anchor="w")
            self.entry = tk.Entry(self)
            self.submit = tk.Button(self, text="Submit", command = self.calculate)
            self.output = tk.Label(self, text="")

        # lay the widgets out on the screen. 
            self.prompt.pack(side="top", fill="x")
            self.entry.pack(side="top", fill="x", padx=20)
            self.output.pack(side="top", fill="x", expand=True)
            self.submit.pack(side="right")

        def calculate(self):
        # get the value from the input widget, convert
        # it to an int, and do a calculation
            try:
                i = int(self.entry.get())
                result = "%s*2=%s" % (i, i*2)
            except ValueError:
                result = "Please enter digits only"

        # set the output widget to have our result
            self.output.configure(text=result)

# if this is run as a program (versus being imported),
# create a root window and an instance of our example,
# then start the event loop
    
    if __name__ == "__main__":
        root = tk.Tk()
        Example(root).pack(fill="both", expand=True)
    

def create_window2():
    
    class Example(tk.Frame):
            def __init__(self, parent):
                tk.Frame.__init__(self, parent)

        # create a prompt, an input box, an output label,
        # and a button to do the computation
                self.prompt = tk.Label(self, text="Your Course:", anchor="w")
                self.entry = tk.Entry(self)
                self.submit = tk.Button(self, text="Submit", command = self.calculate)
                self.output = tk.Label(self, text="")

        # lay the widgets out on the screen. 
                self.prompt.pack(side="top", fill="x")
                self.entry.pack(side="top", fill="x", padx=20)
                self.output.pack(side="top", fill="x", expand=True)
                self.submit.pack(side="right")
                
                self.prompt = tk.Label(self, text="Your Grade:", anchor="w")
                self.entry = tk.Entry(self)
                self.submit = tk.Button(self, text="Submit", command = self.calculate)
                self.output = tk.Label(self, text="")

        # lay the widgets out on the screen. 
                self.prompt.pack(side="top", fill="x")
                self.entry.pack(side="top", fill="x", padx=20)
                self.output.pack(side="top", fill="x", expand=True)
                self.submit.pack(side="right")

            def calculate(self):
        # get the value from the input widget, convert
        # it to an int, and do a calculation
                try:
                    i = int(self.entry.get())
                    result = "%s*2=%s" % (i, i*2)
                except ValueError:
                    result = "Please enter digits only"

        # set the output widget to have our result
                self.output.configure(text=result)

# if this is run as a program (versus being imported),
# create a root window and an instance of our example,
# then start the event loop
    if __name__ == "__main__":
            root = tk.Tk()
            Example(root).pack(fill="both", expand=True)
    


   
def create_window3():
    window3 = tk.Toplevel(root)
    
def create_window4():
    window4 = tk.Toplevel(root)
    


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