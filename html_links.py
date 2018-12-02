from tkinter import *
import webbrowser

def html():
    
    def browser_documentation_one():
        webbrowser.open_new(r"https://www.w3.org/standards/")
    
    
    def browser_documentation_two():
        webbrowser.open_new(r"https://www.w3.org/standards/webdesign/")
    
    
    def browser_documentation_three():
        webbrowser.open_new(r"https://www.w3.org/standards/webofdevices/")
    
    
    def browser_documentation_four():
        webbrowser.open_new(r"https://www.w3.org/standards/webarch/")
    
    
    def browser_infomaterial_one():
        webbrowser.open_new(r"https://www.w3schools.com/html/html_css.asp")
    
    
    def browser_infomaterial_two():
        webbrowser.open_new(r"https://developer.mozilla.org/en-US/docs/Web/HTML")
        
        
    def browser_infomaterial_three():
        webbrowser.open_new(r"http://howtocodeinhtml.com/")
    
    def browser_infomaterial_four():
        webbrowser.open_new(r"https://www.youtube.com/watch?v=RP-DZ2WmKWM&list=PLiHzu4i2Hsb2m7xKZA7aWXve6w8z8Y_ws")
    
    
    main = Tk()
    main.geometry("300x340")
    main.resizable(0,0)
    main.title("GPB Toolkit - Links")
    main_label = Label(main, text="HTML")
    main_label.pack()
    
    frame_two =  Frame(main)
    frame_two.place(x=20, y=25, width=350, height=510)
 
    #topic one

    topic_one = Label(frame_two, text = "offizielle Documentation")
    topic_one.place(x=0, y=0, width=250, height=30)

    link_one = Button(frame_two, text="W3C Standards", fg="blue", cursor="hand2", command = browser_documentation_one)
    link_one.place(x=0, y=30, width=250, height=30)

    link_two = Button(frame_two, text="Web Design and Applications", fg="blue", cursor="hand2", command = browser_documentation_two)
    link_two.place(x=0, y=60, width=250, height=30)

    link_three = Button(frame_two, text="Web of Devices", fg="blue", cursor="hand2", command = browser_documentation_three)
    link_three.place(x=0, y=90, width=250, height=30)

    link_four = Button(frame_two, text="Web Architecture", fg="blue", cursor="hand2", command = browser_documentation_four)
    link_four.place(x=0, y=120, width=250, height=30)

    #topic two

    topic_two = Label(frame_two, text = "Infomaterial")
    topic_two.place(x=0, y=150, width=250, height=30)

    link_one_two = Button(frame_two, text="W3C Schools - HTML", fg="blue", cursor="hand2", command = browser_infomaterial_one)
    link_one_two.place(x=0, y=180, width=250, height=30)

    link_two_two = Button(frame_two, text="MDN Web Docs - HTML", fg="blue", cursor="hand2", command = browser_infomaterial_two)
    link_two_two.place(x=0, y=210, width=250, height=30)

    link_three_two = Button(frame_two, text="Buch: How to Code in HTML and CsS3", fg="blue", cursor="hand2", command = browser_infomaterial_three)
    link_three_two.place(x=0, y=240, width=250, height=30)

    link_four_two = Button(frame_two, text="PanjuTorials Video", fg="blue", cursor="hand2", command = browser_infomaterial_four)
    link_four_two.place(x=0, y=270, width=250, height=30)
