from tkinter import *
import webbrowser

# Principal function of the module, to be called from main.py
def python():
    
    # Functions to call the links
    def browser_documentation_one():
        webbrowser.open_new(r"https://bit.ly/2DWDjIL")
    
    
    def browser_documentation_two():
        webbrowser.open_new(r"https://bit.ly/2oV1q3W")
    
    
    def browser_documentation_three():
        webbrowser.open_new(r"https://bit.ly/2DVvMK9")
    
    
    def browser_documentation_four():
        webbrowser.open_new(r"https://bit.ly/1ARqSBt")
    
    
    def browser_infomaterial_one():
        webbrowser.open_new(r"https://bit.ly/2vPbMns")
    
    
    def browser_infomaterial_two():
        webbrowser.open_new(r"https://youtu.be/dyJdLalc7TA")
        
        
    def browser_infomaterial_three():
        webbrowser.open_new(r"https://bit.ly/1GHEdzn")
    
    def browser_infomaterial_four():
        webbrowser.open_new(r"https://bit.ly/2AJBITq")
    
    # Creation of the user interface
    main = Tk()
    main.geometry("300x340")
    main.resizable(0,0)
    main.title("Toolkit - Python Links")
    main_label = Label(main, text="Python")
    main_label.pack()
    
    frame_two =  Frame(main)
    frame_two.place(x=20, y=25, width=350, height=510)
 
    #topic one
    topic_one = Label(frame_two, text = "Offizielle Documentation")
    topic_one.place(x=0, y=0, width=250, height=30)

    link_one = Button(frame_two, text="Python 2", fg="blue",
                      cursor="hand2", command = browser_documentation_one)
    link_one.place(x=0, y=30, width=250, height=30)

    link_two = Button(frame_two, text="Python 3", fg="blue",
                      cursor="hand2", command = browser_documentation_two)
    link_two.place(x=0, y=60, width=250, height=30)

    link_three = Button(frame_two, text="Developer Guide", fg="blue",
                        cursor="hand2", command = browser_documentation_three)
    link_three.place(x=0, y=90, width=250, height=30)

    link_four = Button(frame_two, text="Python Style Guide", fg="blue",
                       cursor="hand2", command = browser_documentation_four)
    link_four.place(x=0, y=120, width=250, height=30)

    #topic two
    topic_two = Label(frame_two, text = "Infomaterial")
    topic_two.place(x=0, y=150, width=250, height=30)

    link_one_two = Button(frame_two, text="FreeCodeCamp Video", fg="blue",
                          cursor="hand2", command = browser_infomaterial_one)
    link_one_two.place(x=0, y=180, width=250, height=30)

    link_two_two = Button(frame_two,
                          text="Tutorial Python in Deutsch", fg="blue",
                          cursor="hand2", command = browser_infomaterial_two)
    link_two_two.place(x=0, y=210, width=250, height=30)

    link_three_two = Button(frame_two,
                            text="Buch: Automate the Boring Stuff with Python",
                            fg="blue", cursor="hand2",
                            command = browser_infomaterial_three)
    link_three_two.place(x=0, y=240, width=250, height=30)

    link_four_two = Button(frame_two, text="Raspberry Foundation Projekten",
                           fg="blue", cursor="hand2",
                           command = browser_infomaterial_four)
    link_four_two.place(x=0, y=270, width=250, height=30)