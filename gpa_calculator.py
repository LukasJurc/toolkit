from tkinter import *
import table as t

def window_two():
    
    def input_subjects(event):
        fächer = input_amount.get()
        list_points = fächer.split()
        if len(list_points) < 3 or len(list_points) > 10:
            error_message.config(text ="3 bis 10! Nochmal eingeben")
        else:
            return gpa(list_points)


    def gpa(list_points):
        try:
            points =[]
            for num in list_points:
                points.insert(0,int(num)) 
            if len(points) == 3:      
                points_one = (points[0] + points[1] + points[2])/3
                if points_one < 100:
                    points_answer.config(text = round(points_one,2))
                else:
                    points_answer.config(text = "Fehler")
            elif len(points) == 4:
                points_two = (points[0] + points[1] + points[2]
                              + points[3])/4
                if points_two < 100:
                    points_answer.config(text = round(points_two,2))
                else:
                    points_answer.config(text = "Fehler")
            elif len(points) == 5:
                points_three = (points[0] + points[1] + points[2]
                                + points[3] + points[4])/5
                if points_three < 100:
                    points_answer.config(text = round(points_three,2))
                else:
                    points_answer.config(text = "Fehler")
            elif len(points) == 6:
                points_four = (points[0] + points[1] + points[2]
                               + points[3] + points[4] + points[5])/6
                if points_four < 100:
                    points_answer.config(text = round(points_four,2))
                else:
                    points_answer.config(text = "Fehler")
            elif len(points) == 7:
                points_five = (points[0] + points[1] + points[2]
                               + points[3] + points[4]+ points[5]
                               + points[6])/7
                if points_five < 100:
                    points_answer.config(text = round(points_five,2))
                else:
                    points_answer.config(text = "Fehler")
            elif len(points) == 8:
                points_six = (points[0] + points[1] + points[2]
                              + points[3] + points[4] + points[5] + points[6]
                              + points[7])/8
                if points_six < 100:
                    points_answer.config(text = round(points_six,2))
                else:
                    points_answer.config(text = "Fehler")
            elif len(points) == 9:
                points_seven = (points[0] + points[1] + points[2]
                                + points[3] + points[4] + points[5] + points[6]
                                + points[7] + points[8])/9
                if points_seven < 100:
                    points_answer.config(text = round(points_seven,2))
                else:
                    points_answer.config(text = "Fehler")
            elif len(points) == 10:
                points_eight = (points[0] + points[1] + points[2]
                                + points[3] + points[4] + points[5] + points[6]
                                + points[7] + points[8] + points[9])/10
                if points_eight < 100:
                    points_answer.config(text = round(points_eight,2))
                else:
                    points_answer.config(text = "Fehler")     
            return prueba(points)
        except:
            error_message.config(text ="Nur Zahlen, bitte.")

    def prueba(points):
        marks = []
        for spoints in points:
            if spoints > 100:
                error_message.config(text ="Bis 100 Punkte")
                break
            elif spoints>= 92 and spoints<= 100:
                marks.insert(0, 1)
            elif spoints >= 81 and spoints<= 91:
                marks.insert(0, 2)
            elif spoints >= 67 and spoints<= 80:
                marks.insert(0, 3)
            elif spoints >= 50 and spoints<= 66:
                marks.insert(0, 4)
            elif spoints>= 30 and spoints<= 49:
                marks.insert(0, 5)
            elif spoints >= 0 and spoints<= 29:
                marks.insert(0, 6)
        if len(marks) == len(points):
            return gpamarks(marks)
    
    def gpamarks(marks):
        if len(marks) == 3:
            mark_one = (marks[0] + marks[1] + marks[2])/3
            marks_answer.config(text = round(mark_one,2))
        elif len(marks) == 4:
            mark_two = (marks[0] + marks[1] + marks[2] + marks[3])/4
            marks_answer.config(text = round(mark_two,2))
        elif len(marks) == 5:
            mark_three = (marks[0] + marks[1] + marks[2] + marks[3]
                          + marks[4])/5
            marks_answer.config(text = round(mark_three,2))
        elif len(marks) == 6:
            mark_four = (marks[0] + marks[1] + marks[2] + marks[3]
                         + marks[4] + marks[5])/6
            marks_answer.config(text = round(mark_four,2))
        elif len(marks) == 7:
            mark_five = (marks[0] + marks[1] + marks[2] + marks[3]
                         + marks[4] + marks[5] + marks[6])/7
            marks_answer.config(text = round(mark_five,2))        
        elif len(marks) == 8:
            mark_six = (marks[0] + marks[1] + marks[2] + marks[3]
                        + marks[4] + marks[5] + marks[6] + marks[7])/8
            marks_answer.config(text = round(mark_six,2))
        
        elif len(marks) == 9:
            mark_seven = (marks[0] + marks[1] + marks[2] + marks[3]
                          + marks[4] + marks[5] + marks[6] + marks[7]
                          + marks[8])/9
            marks_answer.config(text = round(mark_seven,2))
        
        elif len(marks) == 10:
            mark_eight = (marks[0] + marks[1] + marks[2] + marks[3]
                          + marks[4] + marks[5] + marks[6] + marks[7]
                          + marks[8] + marks[9])/10
            marks_answer.config(text = round(mark_eight,2))
    
    def reset():
        error_message.config(text = "Punktanzahl mit leertaste trennen.")
        points_answer.config(text = "")
        marks_answer.config(text = "")
        input_amount.config(text = "")
    
    def table_call():
        t.point_system()
  
    window =  Tk()
    window.geometry("540x120")
    window.title("Toolkit - GPA Calculator")
    
    frame_one =  Frame(window)
    frame_one.place(x=20, y=0, width=550, height=50)

    label_amount = Label(frame_one, text= "Punkte eingeben: ")
    label_amount.place(x=-20, y=5, width=150, height=30)

    input_amount = Entry(frame_one)
    input_amount.bind("<Return>",input_subjects)
    input_amount.place(x=120, y=5, width= 170, height=30)
    
    error_message = Label(frame_one,
                          text = "Punktanzahl mit Leertaste trennen.")
    error_message.place(x=300, y=5, width=200, height=30)
    
    frame_two =  Frame(window)
    frame_two.place(x=0, y=40, width=550, height=150)

    points_label = Label(frame_two, text ="Punktedurschnitt:")
    points_label.place(x=-47, y=0, width=250, height=30)
    
    points_answer = Label(frame_two)
    points_answer.place(x=137, y=0, width=50, height=30)
    
    marks_label = Label(frame_two, text ="Notendurschnitt:")
    marks_label.place(x=-53, y=30, width=250, height=30)
    
    marks_answer = Label(frame_two)
    marks_answer.place(x=137, y=30, width=50, height=30)
    
    button_one = Button(frame_two, text="Punkttabelle", command = table_call)
    button_one.place(x=310, y=25, width=100, height=30)
    
    button_one = Button(frame_two, text="Zurrückstellen", command = reset)
    button_one.place(x=420, y=25, width=100, height=30)