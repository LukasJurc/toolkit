import tkinter as tk
import blubb as bb
    
    
#commit
def press_button_three():
    bb.window_three()



    

main = tk.Tk()
main.geometry("400x60")
main.resizable(0,0)
main.title("GPB Tools")
main_label = tk.Label(main, text="Choose your programm")
main_label.pack()

button_one = tk.Button(main, text="Suchen")
button_one.place(x=20, y=25, width=80, height=30)


button_two = tk.Button(main, text="Notizen")
button_two.place(x=110, y=25, width=80, height=30)

#commit machen
button_three = tk.Button(main, text="Notizen", command = press_button_three)
button_three.place(x=200, y=25, width=80, height=30)


button_four = tk.Button(main, text="Über uns")
button_four.place(x=290, y=25, width=80, height=30)


main.mainloop() 









