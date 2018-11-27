# Datumsabfrage

print("Geben Sie ein Datum ein (TT.MM.JJJJ):")
x = input()

z = x[6] + x[7] + x[8] + x[9] + x[3] + x[4] + x[0] + x[1]

# Definition des Dateinamens

filename = z+".txt"

f = open(filename, "r")

# Ausgabe des Dateiinhalts

print(f.read())
