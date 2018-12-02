
from tkinter import *
#Automated Date input
from datetime import datetime
import os

def window_three():
    #time showing date and time
    today = datetime.now().strftime("%d-%m-%Y um %H %M %S Uhr") 

    def start_notes():
        text_notes = input_notes.get()
        label_text = Label(main_notes, text=str(today)+": " + text_notes)
        label_text.pack()
        #Creates the note folder, no error message, if directory already exists
        os.makedirs("./note/", exist_ok=True)
        # Definition of filename and write path
        fileinput = open("./note/"+ str(today) +".txt", 'w')#
        fileinput.write(text_notes)
        # Closes file
        fileinput.close()
        
    
    main_notes = Tk()

    main_notes.geometry('450x500')
    main_notes.title('Notizen')
    #note label
    label_notes = Label(main_notes, text='Geben Sie Ihre Notizen ein:')
    label_notes.pack()
    mbutton = Button(main_notes, text ='OK',command=start_notes,fg="black",bg="light grey")
    mbutton.pack()

    input_notes = Entry(main_notes)
    input_notes.pack()

    main_notes.mainloop()