from tkinter import *

# Function to be called from gpa_calculator.py
def point_system():
    
    # Creation of the user interface
    table_root =  Tk()
    table_root.geometry("150x200")
    table_root.title("Toolkit - Tabelle")

    tabel_title = Label(table_root, text ="Punktesystem:")
    tabel_title.place(x=-53, y=10, width=240, height=30)

    tabel_one = Label(table_root, text ="100 - 92 = sehr gut")
    tabel_one.place(x=-53, y=40, width=240, height=30)

    tabel_two = Label(table_root, text = "91 - 81 = gut")
    tabel_two.place(x=-67, y=70, width=240, height=30)

    tabel_three = Label(table_root, text ="80 - 67 = befriedigend")
    tabel_three.place(x=-44, y=100, width=240, height=30)

    tabel_four = Label(table_root, text ="66 - 50 = ausreichend")
    tabel_four.place(x=-45, y=130, width=240, height=30)

    tabel_five = Label(table_root, text ="49 - 30 = mangelhaft")
    tabel_five.place(x=-48, y=160, width=240, height=30)

    tabel_six = Label(table_root, text ="29 - 0 = ungenügend")
    tabel_six.place(x=-47, y=190, width=240, height=30)


