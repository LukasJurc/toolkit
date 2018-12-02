from tkinter import *
import random


def window_one():
    list_fail = ["Please again", "Ups, problems", "Houston, we have a problem", "Send us a mail to:xxxxxxx@xxxxx.com"]

    def search(word):
        txt = open("./archives/python.txt")
        try:
            for info in txt:
                output = info.split(";")
                if word.capitalize() == output[1]:
                    return output
        except:
            return "No"

#output
    def show_output(event):
        word = input_text.get()
        answer = search(word)
        if answer == "No":
            answer_one.config(text = random.choice(list_fail))
        else:
            answer_one.config(text=answer[1])
            answer_two.config(text=answer[2])
            answer_three.config(text=answer[3])
            answer_four.config(text=answer[4])
            answer_five.config(text=answer[5])
            answer_six.config(text=answer[6])
            answer_seven.config(text=answer[7])

    window =  Tk()
    window.geometry("550x600")
    
    frame_one =  Frame(window)
    frame_one.place(x=20, y=0, width=550, height=50)

    search_label =  Label(frame_one, text= "Introduce your search: ")
    search_label.place(x=10, y=5, width=150, height=30)

    input_text = Entry(frame_one)
    input_text.bind("<Return>", show_output)
    input_text.place(x=150, y=5, width=150, height=30)

    clear_output = Button(frame_one, text = "Clean Output", command = reset_output)
    clear_output.place(x=350, y=5, width=150, height=30)
    
    frame_two =  Frame(window)
    frame_two.place(x=20, y=50, width=550, height=400)

    answer_one = Label(frame_two)
    answer_one.pack()
    answer_two = Label(frame_two)
    answer_two.pack()
    answer_three = Label(frame_two)
    answer_three.pack()
    answer_four = Label(frame_two)
    answer_four.pack()
    answer_five = Label(frame_two)
    answer_five.pack()
    answer_six = Label(frame_two)
    answer_six.pack()
    answer_seven = Label(frame_two)
    answer_seven.pack()
