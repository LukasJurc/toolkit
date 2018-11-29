import tkinter as tk

def window_one():
    
    window_one = tk.Tk()
    window_one.geometry("550x600")
    window_one.resizable(0,0)
    window_one.title("GPB Tools")
    
    label_one = tk.Label(window_one, text="Was möchten Sie suchen?")
    label_one.place(x=20, y=5, width=80, height=30)
    
    entry_one = tk.Entry(window_one)
    entry_one.place(x=130, y=5, width=300, height=30)
    
    button_three = tk.Button(window_one, text="Submit")
    button_three.place(x=450, y=5, width=80, height=30)
    
    text_output = tk.Label(window_one, text="")
    text_output.place(x=20, y=45, width=510, height=30)
    
    text_output_two = tk.Label(window_one,text= "ok")
    text_output_two.place(x=20, y=85, width=510, height=500)
    
    window_one.mainloop()
    
def window_two():
    
    window_one = tk.Tk()
    window_one.geometry("550x600")
    window_one.resizable(0,0)
    window_one.title("GPB Tools")
    
    label_one = tk.Label(window_one, text="Was möchten Sie suchen?")
    label_one.place(x=20, y=5, width=80, height=30)
    
    entry_one = tk.Entry(window_one)
    entry_one.place(x=130, y=5, width=300, height=30)
    
    button_three = tk.Button(window_one, text="Submit")
    button_three.place(x=450, y=5, width=80, height=30)
    
    text_output = tk.Label(window_one, text="")
    text_output.place(x=20, y=45, width=510, height=30)
    
    text_output_two = tk.Label(window_one,text= "ok")
    text_output_two.place(x=20, y=85, width=510, height=500)
    
    window_one.mainloop()
    
def window_three():
    bb.window_three()
    
def window_four():
    
    window_one = tk.Tk()
    window_one.geometry("550x600")
    window_one.resizable(0,0)
    window_one.title("GPB Tools")
    
    label_one = tk.Label(window_one, text="Was möchten Sie suchen?")
    label_one.place(x=20, y=5, width=80, height=30)
    
    entry_one = tk.Entry(window_one)
    entry_one.place(x=130, y=5, width=300, height=30)
    
    button_three = tk.Button(window_one, text="Submit")
    button_three.place(x=450, y=5, width=80, height=30)
    
    text_output = tk.Label(window_one, text="")
    text_output.place(x=20, y=45, width=510, height=30)
    
    text_output_two = tk.Label(window_one,text= "ok")
    text_output_two.place(x=20, y=85, width=510, height=500)
    
    window_one.mainloop()
    

def press_button_one():
    window_one()


def press_button_two():
    window_one()


def press_button_three():
    window_one()


def press_button_four():
    window_one()
    

main = tk.Tk()
main.geometry("400x60")
main.resizable(0,0)
main.title("GPB Tools")
main_label = tk.Label(main, text="Choose your programm")
main_label.pack()

button_one = tk.Button(main, text="Suchen", command = press_button_one)
button_one.place(x=20, y=25, width=80, height=30)


button_two = tk.Button(main, text="Notizen", command = press_button_two)
button_two.place(x=110, y=25, width=80, height=30)


button_three = tk.Button(main, text="Durschnitt", command = press_button_three)
button_three.place(x=200, y=25, width=80, height=30)


button_four = tk.Button(main, text="Über uns", command = press_button_four)
button_four.place(x=290, y=25, width=80, height=30)


main.mainloop() 









