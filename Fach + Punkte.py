#Zuerst auf Deutsch

text = "Hallo! In diesem Menü kannst du deine Fächer inklusive Punkte eintragen."

laenge = len(text)
print("*" + "*" * laenge + "*" + "*")
print("*" + text +  "*")
print("*" *2 + "*" * laenge + '*')

fächer = ["fach1", "fach2", "fach3", "fach4", "fach5", "fach6", "fach7", "fach8", "fach9", "fach10"]
punkte = ["punkte1", "punkte2", "punkte3", "punkte4", "punkte5", "punkte6", "punkte7", "punkte8", "punkte9", "punkte10"]


for fächer and punkte in range (0,10):
    input("Geben sie ein Fach ein: ")


#Fächer[0:9] = input("Geben sie ein Fach ein: ")
#Punkte[0:9] = input("Geben sie ihre Punktzahl ein: ")

#Fächer[1] = input("Geben sie ein Fach ein: ")
#Punkte[1] = input("Geben sie ihre Punktzahl ein: ")

#import pickle

#l = [1,2,3,4]

import json
a = [1,2,3]
with open('test.txt', 'w') as f:
    f.write(json.dumps(a))

#Now read the file back into a Python list object
with open('test.txt', 'r') as f:
    a = json.loads(f.read())