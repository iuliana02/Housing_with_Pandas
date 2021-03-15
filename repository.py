import csv
import pandas as pd

class Repository:
    def __init__(self):
        self.liste=[]
        self.dataframe = pd.DataFrame()

    def create_liste(self):
        list=[]
        with open('housing.csv', newline='') as csvfile:
            reader = csv.reader(csvfile, delimiter=',')
            lines = [line for line in reader]
            for line in lines:
                list.append(line)

    def read(self,filename): #citire fisier csv
          self.dataframe = pd.read_csv(filename)

    def preis(self):
        '''Erhöht den Preis für alle Häuser am Ozean um 10%'''

        liste = [r for r in csv.reader(open('housing.csv'), delimiter=',') if r[9] == 'NEAR OCEAN']
        marire = [[r[0], r[1], r[2], r[3], r[4], r[5], r[6], r[7], float(r[8]) + float(r[8]) / 10, r[9]] for r in liste
                  if not (not r[8]) and (r[8][0] > '0' and r[8][0] < '9')]
        afis = [print(r) for r in marire]

