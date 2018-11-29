# Start of the function

counter = 3
counter2 = 10

print("Wie viele Fächer wollen sie eintragen?: ")
number_answer = input()

while int(counter)> int(number_answer) or int(counter2)< int(number_answer):
    print("""Der Durchschnitt kann nur mit mindestens 3 Fächern berechnet werden.
Bitte geben sie eine Zahl zwischen 3-10 ein.""")
    number_answer = input()
    
if int(number_answer) <int(counter2) or int(number_answer) > int(counter):
    print("OK, wir machen weiter.")


class school:
    def __init__(grades, desc, excellent, good, okay, well, acceptable, bad):
        grades.desc = descript
        grades.excellent = excellent2
        grades.good = good3
        grades.okay = okay4
        grades.well = well5
        grades.acceptable = acceptable6
        grades.bad = bad7

g1 = school("Sehr gut", "wow")

print(g1.excellent2)

#def gpa_ph(gradesbad):
 #   print(" " + grades.bad)


list_fächer = []
list_punkte = []
#noten = [1, 2, 3, 4, 5, 6]
start0 = 0



while start0 < int(number_answer):
        fächer = input("Geben sie ein Fach ein: ")
        list_fächer.insert(0,fächer)
        punkte = input("Geben sie ihre Punktzahl ein: ")
        list_punkte.insert(0,int(punkte))
        if int(punkte)>= 92 and int(punkte)<= 100:
            print("Note: sehr gut = ", "1")
        elif int(punkte)>= 81: #or int(punkte)<= (91):
            print("Note: gut = ", B)
        elif int(punkte)>= 67:# or int(punkte)>= (67):
            print("Note: befriedigend = ", C)
        elif int(punkte)>= 50: #or int(punkte)>= (50):
            print("Note: ausreichend = ", D)
        elif int(punkte)>= 30: #or int(punkte)>= (30):
            print("Note: mangelhaft = ", E)
        elif int(punkte)>= 0: #or int(punkte)>= (0):
            print("Note: ungenügend =", gpa_ph(gradesbad))
        start0 = start0 +1





# Durchschnittsberechnung
if len(list_punkte) == 3:
    print("Durchschnittspunkte: ", ( list_punkte[0] + list_punkte[1] + list_punkte[2])/3)
    
elif len(list_punkte) == 4:
    print("Durchschnittspunkte: ", (list_punkte[0] + list_punkte[1] + list_punkte[2] + list_punkte[3])/4)

elif len(list_punkte) == 5:
    print("Durchschnittspunkte: ", (list_punkte[0] + list_punkte[1] + list_punkte[2] + list_punkte[3] + list_punkte[4])/5)
    
elif len(list_punkte) == 6:
    print("Durchschnittspunkte: ", (list_punkte[0] + list_punkte[1] + list_punkte[2] + list_punkte[3] + list_punkte[4] + list_punkte[5])/6)

elif len(list_punkte) == 7:
    print("Durchschnittspunkte: ", (list_punkte[0] + list_punkte[1] + list_punkte[2] + list_punkte[3] + list_punkte[4] + list_punkte[5] + list_punkte[6])/7)

elif len(list_punkte) == 8:
    print("Durchschnittspunkte: ", (list_punkte[0] + list_punkte[1] + list_punkte[2] + list_punkte[3] + list_punkte[4] + list_punkte[5] + list_punkte[6] + list_punkte[7])/8)

elif len(list_punkte) == 9:
    print("Durchschnittspunkte: ", (list_punkte[0] + list_punkte[1] + list_punkte[2] + list_punkte[3] + list_punkte[4] + list_punkte[5] + list_punkte[6] + list_punkte[7] + list_punkte[8])/9)

elif len(list_punkte) == 10:
    print("Durchschnittspunkte: ", (list_punkte[0] + list_punkte[1] + list_punkte[2] + list_punkte[3] + list_punkte[4] + list_punkte[5] + list_punkte[6] + list_punkte[7] + list_punkte[8] + list_punkte[9])/10)

# Notendurchschnitt


if len(grades) == 3:
    print("Schnitt: "), (grades.A + grades.B + grades.C / 3)
    #print("Notendurchschnitt", (int(A) + int(B) + int(C)/int(3)))

#durchschnitt(grades):
    #grades.A + grades.B + grades.C / 3)