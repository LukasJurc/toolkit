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


#fächer = ["fach1", "fach2", "fach3", "fach4", "fach5", "fach6", "fach7", "fach8", "fach9", "fach10"]
#punkte = ["punkte1", "punkte2", "punkte3", "punkte4", "punkte5", "punkte6", "punkte7", "punkte8", "punkte9", "punkte10"]

list_fächer = []
list_punkte = []
start0 = 0

while start0 < int(number_answer):
        fächer = input("Geben sie ein Fach ein: ")
        list_fächer.insert(0,fächer)
        punkte = input("Geben sie ihre Punktzahl ein: ")
        list_punkte.insert(0,int(punkte))
        start0 = start0 +1

# first make a list out of the subjects

#fächer[1] = input("Geben sie ein Fach ein: ")
#punkte[1] = input("Geben sie ihre Punktzahl ein: ")


#return (fächer1)


#def fächer2(Schulfächer):
    #fächer[1:9]
#fächer =
