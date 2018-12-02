from tkinter import *
import python_links as pl
import html_links as hl
import css_links as cl
import tools_links as tl

def window_one():
    main = Tk()
    main.geometry("250x170")
    main.resizable(0,0)
    main.title("GPB - Links")
    main_label = Label(main, text="über was willst du lesen?")
    main_label.pack()

    def python_links():
        pl.python()

    def html_links():
        hl.html()

    def css_links():
        cl.css()

    def tools_links():
        tl.tools()


    button_one = Button(main, text="Python", command = python_links)
    button_one.place(x=20, y=25, width=200, height=30)


    button_two = Button(main, text="HTML", command = html_links)
    button_two.place(x=20, y=55, width=200, height=30)


    button_three = Button(main, text="CSS", command = css_links)
    button_three.place(x=20, y=85, width=200, height=30)


    button_four = Button(main, text="Tools", command = tools_links)
    button_four.place(x=20, y=115, width=200, height=30)


    main.mainloop()