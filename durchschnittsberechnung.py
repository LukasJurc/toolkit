# Berechnung der Noten und Punkte Durchschnitt

print("gib dein erstes Fach ein:")      # Eingabe eines Modul
fach1 = input()
while len(fach1)>40 or len(fach1)< 2or fach1.isspace():
    print("Fehlermeldung!!!   Bitte geben sie ein Fach ein(min 2 and max 40)")
    fach1 = input()
print("Gib deine Punkte ein:")          # Eingabe der KlausurPunkte 
punkte1 = int(input())
while int(punkte1) >3 or int(punkte1) <0 or punkte1.isspace():
    print("Fehlermeldung!!!   Bitte geben sie ihre Punkte ein(min 1 and max 3)")
    punkte1 = int(input())

print("gib dein zweites Fach ein:")     # Eingabe eines Modul
fach2 = input()
while len(fach2)>40 or len(fach2)< 2or fach2.isspace():
    print("Fehlermeldung!!!   Bitte geben sie ein Fach ein(min 2 and max 40)")
    fach2 = input()
print("Gib deine Punkte ein:")          # Eingabe der KlausurPunkte 
punkte2 = int(input())
while len(punkte2)>40 or len(punkte2)< 2 or punkte2.isspace():
    print("Fehlermeldung!!!   Bitte geben sie ihre Punkte ein(min 2 and max 40)")
    punkte2 = int(input())

print("gib dein drittes Fach ein:")     # Eingabe eines Modul
fach3 = input()
while len(fach3)>40 or len(fach3)< 2or fach3.isspace():
    print("Fehlermeldung!!!   Bitte geben sie ein Fach ein(min 2 and max 40)")
    fach3 = input()
print("Gib deine Punkte ein:")          # Eingabe der KlausurPunkte
punkte3 = int(input())
while len(punkte3)>40 or len(punkte3)< 2 or punkte3.isspace():
    print("Fehlermeldung!!!   Bitte geben sie ihre Punkte ein(min 2 and max 40)")
    punkte3 = int(input())

print("gib dein viertes Fach ein:")     # Eingabe eines Modul
fach4 = input()
while len(fach4)>40 or len(fach4)< 2or fach4.isspace():
    print("Fehlermeldung!!!   Bitte geben sie ein Fach ein(min 2 and max 40)")
    fach4 = input()
print("Gib deine Punkte ein:")          # Eingabe der KlausurPunkte
punkte4 = int(input())
while len(punkte4)>40 or len(punkte4)< 2 or punkte4.isspace():
    print("Fehlermeldung!!!   Bitte geben sie ihre Punkte ein(min 2 and max 40)")
    punkte4 = int(input())

print("gib dein fünftes Fach ein:")     # Eingabe eines Modul
fach5 = input()
while len(fach5)>40 or len(fach5)< 2or fach5.isspace():
    print("Fehlermeldung!!!   Bitte geben sie ein Fach ein(min 2 and max 40)")
    fach5 = input()
print("Gib deine Punkte ein:")          # Eingabe der KlausurPunkte
punkte5 = int(input())
while len(punkte5)>40 or len(punkte5)< 2 or punkte5.isspace():
    print("Fehlermeldung!!!   Bitte geben sie ihre Punkte ein(min 2 and max 40)")
    punkte5 = int(input())

durchschnitt = (punkte1 + punkte2 + punkte3 + punkte4 + punkte5) / 5  # Durchschnittsberechnung der Klausurpunkte
print("Klausurpunkte Durschnitt:", durchschnitt)










