from controller import *
from repository import *
def afis():
    return """
       1.Findet den Distrikt mit der größten, bzw kleinster Bevölkerung 
       2.Findet den Distrikt mit der größten, bzw. kleinsten Anzahl von Einwohner pro Schlafzimmer, sowie den Durchschnittswert 
       3.Findet das durchschnittlichen Alter und den durchschnittlichen Einkommen der Einwohner 
       4.Distrikte gruppiert nach der Spalte ocean_proximity
       5.Erhöht den Preis für alle Häuser am Ozean um 10%
       6.Raport mit allen Distrikten, die sich in bestimmte Intervalle der latitude,longitude und median_house_value befinden
       7.Sortieren nach median_house_value und ocean_proximity
       8.Filtern nach einem Kriterium eine Spalte. Die Spalte und Kriterium werden von der Tastatur eingelesen.
       0.Break
       """
repo=Repository()
haus=Controller(repo)
haus.repo.read('housing.csv')
def main():
    print(afis())
    while True:
        try:
            opt=int(input('Optiune:'))
            if opt==1:
                print(haus.maxim_minim.__doc__)
                haus.maxim_minim()
            if opt==2:
                print(haus.einwohner_pro_schlafzimmer.__doc__)
                haus.einwohner_pro_schlafzimmer()
            if opt==3:
                print(haus.alter.__doc__)
                print(haus.einkommen.__doc__)
                print("Durchschnittliche Alter:")
                print(haus.alter())
                print("Durchschnittliche Einkommen der Einwohner:")
                print(haus.einkommen())
                haus.test_alter_einkommen()
            if opt==4:
                print(haus.ocean.__doc__)
                haus.ocean()
            if opt==5:
                print(haus.repo.preis.__doc__)
                haus.repo.preis()
            if opt==6:
                print(haus.report.__doc__)
                haus.report()
            if opt==0:
                break
            if opt==7:
                print(haus.sort.__doc__)
                haus.sort()
            if opt==8:
                print(haus.filtern.__doc__)
                haus.filtern()
        except ValueError:
            print('Man muss eine Zahl eingeben!')

main()