from tkinter import *
import webbrowser

def css():
    
    def browser_documentation_one():
        webbrowser.open_new(r"https://www.w3.org/standards/techs/css#stds")
    
    
    def browser_documentation_two():
        webbrowser.open_new(r"https://www.w3.org/TR/2000/REC-DOM-Level-2-Style-20001113/")
    
    
    def browser_documentation_three():
        webbrowser.open_new(r"https://www.w3.org/TR/2012/REC-css3-mediaqueries-20120619/")
    
    
    def browser_documentation_four():
        webbrowser.open_new(r"https://www.w3.org/TR/2013/REC-css-style-attr-20131107/")
    
    
    def browser_infomaterial_one():
        webbrowser.open_new(r"https://developer.mozilla.org/en-US/docs/Web/CSS")
    
    
    def browser_infomaterial_two():
        webbrowser.open_new(r"https://www.w3schools.com/css/default.asp")
        
        
    def browser_infomaterial_three():
        webbrowser.open_new(r"https://www.youtube.com/watch?v=yBFE7Kcpb2k&list=PL5jhqWqcHcSLY1L3plznN7cXr4zteVbXL")
    
    def browser_infomaterial_four():
        webbrowser.open_new(r"https://www.youtube.com/watch?v=QqmCs2UTS8s&list=PLP9IO4UYNF0XQNx1OinMm84lyGzWSWDms")
    
    
    main = Tk()
    main.geometry("300x340")
    main.resizable(0,0)
    main.title("GPB Toolkit - Links")
    main_label = Label(main, text="CSS")
    main_label.pack()
    
    frame_two =  Frame(main)
    frame_two.place(x=20, y=25, width=350, height=510)
 
    #topic one

    topic_one = Label(frame_two, text = "offizielle Documentation")
    topic_one.place(x=0, y=0, width=250, height=30)

    link_one = Button(frame_two, text="CSS Current Status", fg="blue", cursor="hand2", command = browser_documentation_one)
    link_one.place(x=0, y=30, width=250, height=30)

    link_two = Button(frame_two, text="DOM- Level 2 Style Specification", fg="blue", cursor="hand2", command = browser_documentation_two)
    link_two.place(x=0, y=60, width=250, height=30)

    link_three = Button(frame_two, text="Media Queries", fg="blue", cursor="hand2", command = browser_documentation_three)
    link_three.place(x=0, y=90, width=250, height=30)

    link_four = Button(frame_two, text="CSS Style Attributes", fg="blue", cursor="hand2", command = browser_documentation_four)
    link_four.place(x=0, y=120, width=250, height=30)

    #topic two

    topic_two = Label(frame_two, text = "Infomaterial")
    topic_two.place(x=0, y=150, width=250, height=30)

    link_one_two = Button(frame_two, text="MDN Web Docs - CSS", fg="blue", cursor="hand2", command = browser_infomaterial_one)
    link_one_two.place(x=0, y=180, width=250, height=30)

    link_two_two = Button(frame_two, text="W3C School - CSS", fg="blue", cursor="hand2", command = browser_infomaterial_two)
    link_two_two.place(x=0, y=210, width=250, height=30)

    link_three_two = Button(frame_two, text="Video: techPunkt Tutorial", fg="blue", cursor="hand2", command = browser_infomaterial_three)
    link_three_two.place(x=0, y=240, width=250, height=30)

    link_four_two = Button(frame_two, text="Video: W3C CSS Tutorial", fg="blue", cursor="hand2", command = browser_infomaterial_four)
    link_four_two.place(x=0, y=270, width=250, height=30)

