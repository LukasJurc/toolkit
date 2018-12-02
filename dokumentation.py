from tkinter import *
import webbrowser
import os

def window_four(): 

    def mhello():
        mtext = mEntry.get()
        mlabel2 = Label(mGui, text= mtext)
        mlabel2.pack()
        if mtext == "dinko":
            webbrowser.open_new('https://www.dropbox.com/s/3od07ml3tvvpo4c/The%20Art%20of%20SEO.pdf?dl=0')
        elif mtext == "dinko": 
            webbrowser.open_new('https://www.dropbox.com/s/3od07ml3tvvpo4c/The%20Art%20of%20SEO.pdf?dl=0')
        elif mtext == "stephan":
            webbrowser.open_new('https://www.dropbox.com/s/3od07ml3tvvpo4c/The%20Art%20of%20SEO.pdf?dl=0')
        elif mtext == "furkan":
            webbrowser.open_new('https://www.dropbox.com/s/3od07ml3tvvpo4c/The%20Art%20of%20SEO.pdf?dl=0')
        elif mtext == "lukas":
            webbrowser.open_new('https://www.dropbox.com/s/3od07ml3tvvpo4c/The%20Art%20of%20SEO.pdf?dl=0')
        else:
            return "This person wasn´t in this project!"
    mGui = Tk()

    mGui.geometry('450x500')
    mGui.title('dokumentation')
    #note label
    mlabel = Label(mGui, text='Geben Sie den Namen der Person ein, dessen Dokumentation Sie sehen wollen:')
    mlabel.pack()
    mbutton = Button(mGui, text ='OK',command=mhello,fg="black",bg="light grey")
    mbutton.pack()

    mEntry = Entry(mGui)
    mEntry.pack()

    mGui.mainloop()
