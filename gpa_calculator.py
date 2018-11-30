# Start of the function


def input_subjects():
    global number_answer
    counter = 3
    counter2 = 10
    print("Wie viele Fächer wollen sie eintragen?: ")
    number_answer = input()
    while int(counter)> int(number_answer) or int(counter2)< int(number_answer):
        print("""Der Durchschnitt kann nur mit mindestens 3 Fächern berechnet werden.
          Bitte geben sie eine Zahl zwischen 3-10 ein.""")
        number_answer = input()
    
    print("OK, wir machen weiter.")
    points()

# calculating points
def points():
    global list_subjects
    global list_points
    start0 = 0
    while start0 < int(number_answer):
        ssubjects = input("Geben sie ein Fach ein: ")
        list_subjects.insert(0,ssubjects)
        spoints = input("Geben sie ihre Punktzahl ein: ")
        list_points.insert(0,int(spoints))
        if int(spoints)>= 92 and int(spoints)<= 100:
            print("Note: sehr gut =", A)
            list_marks.insert(0, 1)
        elif int(spoints)>= 81 and int(spoints)<= 91:
            print("Note: gut =", B)
            list_marks.insert(0, 2)
        elif int(spoints)>= 67 and int(spoints)<= 80:
            print("Note: befriedigend =", C)
            list_marks.insert(0, 3)
        elif int(spoints)>= 50 and int(spoints)<= 66:
            print("Note: ausreichend =", D)
            list_marks.insert(0, 4)
        elif int(spoints)>= 30 and int(spoints)<= 49:
            print("Note: mangelhaft =", E)
            list_marks.insert(0, 5)
        elif int(spoints)>= 0 and int(spoints)<= 29:
            print("Note: ungenügend =", F)
            list_marks.insert(0, 6)
        start0 = start0 +1
             
    gpa()


# Grade Point Average = GPA / gpa
def gpa():
    global list_subjects
    global list_points
    if len(list_points) == 3:
        x1 = (list_points[0] + list_points[1] + list_points[2])/3
        print("Punktedurchschnitt:", round(x1,2))
    elif len(list_points) == 4:
        x2 = (list_points[0] + list_points[1] + list_points[2] + list_points[3])/4
        print("Durchschnittspunkte:", round(x2,2))
    elif len(list_points) == 5:
        x3 = (list_points[0] + list_points[1] + list_points[2] + list_points[3] + list_points[4])/5
        print("Durchschnittspunkte:", round(x3,2))
    elif len(list_points) == 6:
        x4 = (list_points[0] + list_points[1] + list_points[2] + list_points[3] + list_points[4] + list_points[5])/6
        print("Durchschnittspunkte:", round(x4,2))
    elif len(list_points) == 7:
        x5 = (list_points[0] + list_points[1] + list_points[2] + list_points[3] + list_points[4] + list_points[5] + list_points[6])/7
        print("Durchschnittspunkte:", round(x5,2))
    elif len(list_points) == 8:
        x6 = (list_points[0] + list_points[1] + list_points[2] + list_points[3] + list_points[4] + list_points[5] + list_points[6] + list_points[7])/8
        print("Durchschnittspunkte:", round(x6,2))
    elif len(list_points) == 9:
        x7 = (list_points[0] + list_points[1] + list_points[2] + list_points[3] + list_points[4] + list_points[5] + list_points[6] + list_points[7] + list_points[8])/9
        print("Durchschnittspunkte:", round(x7,2))
    elif len(list_points) == 10:
        x8 = (list_points[0] + list_points[1] + list_points[2] + list_points[3] + list_points[4] + list_points[5] + list_points[6] + list_points[7] + list_points[8] + list_points[9])/10
        print("Durchschnittspunkte:", round(x8,2))

    gpamarks()

# GPA / gpa marks
def gpamarks():
    global list_marks
    if len(list_marks) == 3:
        y1 = (list_marks[0] + list_marks[1] + list_marks[2])/3
        print("Notendurchschnitt:", round(y1,2))
    elif len(list_marks) == 4:
        y2 = (list_marks[0] + list_marks[1] + list_marks[2] + list_marks[3])/4
        print("Notendurchschnitt:", round(y2,2))
    elif len(list_marks) == 5:
        y3 = (list_marks[0] + list_marks[1] + list_marks[2] + list_marks[3] + list_marks[4])/5
        print("Notendurchschnitt:", round(y3,2))
    elif len(list_marks) == 6:
        y4 = (list_marks[0] + list_marks[1] + list_marks[2] + list_marks[3] + list_marks[4] + list_marks[5])/6
        print("Notendurchschnitt:", round(y4,2))



list_subjects = []
list_points = []
list_marks = []


marks =  {
  "excellent": 1,
  "good": 2,
  "okay": 3,
  "well": 4,
  "acceptable": 5,
  "bad": 6
}

A = marks.get("excellent")
B = marks.get("good")
C = marks.get("okay")
D = marks.get("well")
E = marks.get("acceptable")
F = marks.get("bad")


input_subjects()
