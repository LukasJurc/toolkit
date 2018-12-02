from tkinter import *
import webbrowser

def tools():
    
    def browser_documentation_one():
        webbrowser.open_new(r"https://eu.udacity.com/")
    
    
    def browser_documentation_two():
        webbrowser.open_new(r"https://www.coursera.org/")
    
    
    def browser_documentation_three():
        webbrowser.open_new(r"https://open.hpi.de/?locale=de")
    
    
    def browser_documentation_four():
        webbrowser.open_new(r"https://www.codecademy.com/")
    
    
    def browser_infomaterial_one():
        webbrowser.open_new(r"https://github.com/")
    
    
    def browser_infomaterial_two():
        webbrowser.open_new(r"https://thonny.org/")
        
        
    def browser_infomaterial_three():
        webbrowser.open_new(r"https://atom.io/")
    
    def browser_infomaterial_four():
        webbrowser.open_new(r"https://git-scm.com/")
    
    
    main = Tk()
    main.geometry("300x340")
    main.resizable(0,0)
    main.title("GPB Toolkit - Links")
    main_label = Label(main, text="Tools")
    main_label.pack()
    
    frame_two =  Frame(main)
    frame_two.place(x=20, y=25, width=350, height=510)
 
    #topic one

    topic_one = Label(frame_two, text = "online Course")
    topic_one.place(x=0, y=0, width=250, height=30)

    link_one = Button(frame_two, text="Udacity", fg="blue", cursor="hand2", command = browser_documentation_one)
    link_one.place(x=0, y=30, width=250, height=30)

    link_two = Button(frame_two, text="Coursera", fg="blue", cursor="hand2", command = browser_documentation_two)
    link_two.place(x=0, y=60, width=250, height=30)

    link_three = Button(frame_two, text="Hasso-Plattner-Institut", fg="blue", cursor="hand2", command = browser_documentation_three)
    link_three.place(x=0, y=90, width=250, height=30)

    link_four = Button(frame_two, text="Codecademy", fg="blue", cursor="hand2", command = browser_documentation_four)
    link_four.place(x=0, y=120, width=250, height=30)

    #topic two

    topic_two = Label(frame_two, text = "Werkzeuge")
    topic_two.place(x=0, y=150, width=250, height=30)

    link_one_two = Button(frame_two, text="Github", fg="blue", cursor="hand2", command = browser_infomaterial_one)
    link_one_two.place(x=0, y=180, width=250, height=30)

    link_two_two = Button(frame_two, text="Thonny IDE for Python", fg="blue", cursor="hand2", command = browser_infomaterial_two)
    link_two_two.place(x=0, y=210, width=250, height=30)

    link_three_two = Button(frame_two, text="ATOM IDE", fg="blue", cursor="hand2", command = browser_infomaterial_three)
    link_three_two.place(x=0, y=240, width=250, height=30)

    link_four_two = Button(frame_two, text="git", fg="blue", cursor="hand2", command = browser_infomaterial_four)
    link_four_two.place(x=0, y=270, width=250, height=30)


