while start0 < int(number_answer):
        fächer = input("Geben sie ein Fach ein: ")
        list_fächer.insert(0,fächer)
        punkte = input("Geben sie ihre Punktzahl ein: ")
        list_punkte.insert(0,int(punkte))
        if int(punkte)>=(92):
            print("sehr gut")
        elif int(punkte)>= (81): #or int(punkte)<= (91):
            print("gut")
        elif int(punkte)>= (67):# or int(punkte)>= (67):
            print("befriedigend")
        elif int(punkte)>= (50): #or int(punkte)>= (50):
            print("ausreichend")
        elif int(punkte)>= (30): #or int(punkte)>= (30):
            print("mangelhaft")
        elif int(punkte)>= (0): #or int(punkte)>= (0):
            print("ungenügend")
        start0 = start0 +1