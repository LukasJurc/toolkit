import tkinter as tk

root = tk.Tk()
frame = tk.Frame(root)
frame.pack()
root.geometry("363x200")
root.resizable(0,0)
root.title("GPB Toolkit")
root.option_add("*background", "lightgrey")

    
# function opens a new window
def create_window1():
    
    class Example(tk.Frame):
        def __init__(self, parent):
            tk.Frame.__init__(self, parent)
            frame.pack()
            root.geometry("800x600")
            root.resizable(0,0)
            root.title("GPB Search")
            root.option_add("*background", "lightgrey")

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
                root.geometry("800x600")
                root.resizable(0,0)
                root.title("GPB Grades")
                root.option_add("*background", "lightgrey")

        #Entry 1, Window 2
        
        # create a prompt, an input box, an output label,
        # and a button to do the computation
                self.prompt = tk.Label(self, text="Your Course:", anchor="w")
                self.entry = tk.Entry(self)
                self.submit = tk.Button(self, text="Submit", command = self.calculate)
                self.output = tk.Label(self, text="")
                

        # lay the widgets out on the screen. 
                self.prompt.place(x=30, y=0, width=300, height=50)
                self.entry.place(x=30, y=60, width=300, height=50)
                self.submit.place(x=30, y=120, width=300, height=50)
                self.output.place(x=30, y=180, width=300, height=50)
                

#Entry 2, Window 2
                self.prompt = tk.Label(self, text="Your Grade:", anchor="w")
                self.entry = tk.Entry(self)
                self.submit = tk.Button(self, text="Submit", command = self.calculate)
                self.output = tk.Label(self, text="")

        # lay the widgets out on the screen. 
                self.prompt.place(x=400, y=0, width=300, height=50)
                self.entry.place(x=400, y=60, width=300, height=50)
                self.submit.place(x=400, y=120, width=300, height=50)
                self.output.place(x=400, y=180, width=300, height=50)

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
