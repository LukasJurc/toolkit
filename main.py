import tkinter as tk
import webbrowser
import notes as n
import links_library as ll
import gpa_calculator as avg
    
def press_button_one():    
    ll.window_one()


def press_button_two():
    avg.window_two()


def press_button_three():
    n.window_three()


def press_button_four():
    webbrowser.open(r'https://github.com/LukasJurc/toolkit')
    

main = tk.Tk()
main.geometry("400x60")
main.resizable(0,0)
main.title("GPB Tools")
main_label = tk.Label(main, text="Choose your programm")
main_label.pack()

button_one = tk.Button(main, text="Linkbibliothek", command = press_button_one)
button_one.place(x=20, y=25, width=80, height=30)


button_two = tk.Button(main, text="Durchschnitt", command = press_button_two)
button_two.place(x=110, y=25, width=80, height=30)


button_three = tk.Button(main, text="Notizen", command = press_button_three)
button_three.place(x=200, y=25, width=80, height=30)


button_four = tk.Button(main, text="Über uns", command = press_button_four)
button_four.place(x=290, y=25, width=80, height=30)


main.mainloop() 









