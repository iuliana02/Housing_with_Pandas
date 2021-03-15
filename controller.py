import csv
import pandas as pd
#from repository import *

class Controller:
    def __init__(self, repo):
        self.repo = repo

    def maxim_minim(self): #populatia maxima, minima
        """Findet den Distrikt mit der größten, bzw kleinster Bevölkerung"""
        maxi = self.repo.dataframe['population'].max() #fac functia max pe toata coloana de population
        id1=self.repo.dataframe.index[self.repo.dataframe['population']==maxi].tolist()[0] #gasesc index-ul liniei cu populatia maxima si il salvez intr-o lista
        print('maximum:',self.repo.dataframe.iloc[[id1]]) #printez maximul si linia respectiva
        mini=self.repo.dataframe['population'].min()
        id2=self.repo.dataframe.index[self.repo.dataframe['population']==mini].tolist()[0]
        print('minimum:',self.repo.dataframe.iloc[[id2]])

    def einwohner_pro_schlafzimmer(self):
        """Findet den Distrikt mit der größten, bzw. kleinsten Anzahl von Einwohner pro Schlafzimmer, sowie den Durchschnittswert"""
        mini=99999
        maxi=0
        csv=pd.read_csv('housing.csv')
        df = pd.DataFrame(csv,columns=['population','total_bedrooms']) #coloanele pe care trebuie sa le impart
        df['Result']=df['population']/df['total_bedrooms'] #creez o coloana noua (Result) in care impart population la total_bedrooms
        for i in range(1,len(df['Result'])):
            if df['Result'][i] < mini:
                mini=df['Result'][i]
            if df['Result'][i]> maxi:
                maxi=df['Result'][i]
        print('Minim:',mini)
        print('Maxim:',maxi)
        s = df['Result'].sum()
        l = len(df['Result'])
        durchschnitt = s/l
        print('Durchschnitt:',durchschnitt)

    def alter (self):
        """Findet das durchschnittlichen Alter """
        csv = pd.read_csv('housing.csv') #citesc fisierul
        df1=pd.DataFrame(csv,columns=['housing_median_age']) #iau doar coloana housing_median_age
        s_a=df1['housing_median_age'].sum() #suma pe coloana housing_median_age
        l_a=len(df1['housing_median_age']) #lungimea coloanei(cate randuri are)
        d1=s_a/l_a #durchschnitt-->suma/lungime
        return d1
    def einkommen(self):
        """Findet den durchschnittlichen Einkommen der Einwohner"""
        csv = pd.read_csv('housing.csv')  # citesc fisierul
        df2 = pd.DataFrame(csv, columns=['median_income'])
        s_i = df2['median_income'].sum()
        l_i = len(df2['median_income'])
        d2 = s_i / l_i
        return d2

    def test_alter_einkommen(self):
        assert self.alter()==28.639486434108527
        assert self.einkommen()==388.4320909156977

    def ocean(self):
        '''Die Spalte ocean_proximity ist ein kategorischer Attribut. Auf dieser Spalte
    erscheinen nämlich nur 5 verschiedene Werte. Identifiziert diese und die Anzahl von
    Distrikte aus jeder Kategorie
    '''
        print(self.repo.dataframe['ocean_proximity'].value_counts())


    def report(self):
        """ Report erstellen: sie erhalten von den Kunden ein Intervall für latitude, longitude und median_house_value. Erstellt in einer anderen Textdatei ein Report
        mit allen Distrikten, die diesen Kriterien entsprechen. Gebt eine Fehlermeldung an falls es keine Distrikte gibt die de angegebenen Kriterien entsprechen.
        Die Werte sollen durch ein Leerzeichen getrennt werden"""
        long_mic = float(input('Small longitude:'))
        long_mare = float(input('Big longitude:'))
        lat_mic = float(input('Small latitude:'))
        lat_mare = float(input('Big latitude:'))
        preis_mic = float(input('Kleinstes Preis:'))
        preis_mare = float(input('Grosstes Preis:'))
        try:
            if long_mic>long_mare:
                raise TypeError('long_mic<long_mare')
            if lat_mic>lat_mare:
                raise TypeError('lat_mic<lat_mare')
            if preis_mic>preis_mare:
                raise TypeError('preis_mic<preis_mare')
            with open ('report.txt','w') as f: #deschid fisierul creat de mine si scriu
                [f.write(str(row)+'\n') for row in csv.reader(open('housing.csv'),delimiter=',') if (row[1][1]>'0' and row [1][1]<'9') and (float(row[0])>long_mic and float(row[0])<long_mare) and (float(row[1])>lat_mic and float(row[1])<lat_mare) and (float(row[8])>preis_mic and float(row[8])<preis_mare)]
        except TypeError:
            print("Man muss bei jeder Kategorie die erste Zahl grosser und die zweite Zahl kleiner sein.")


        #de la lab6
    def sort(self):
        """Sorting nach median_house_value und ocean_proximity"""
        sort=self.repo.dataframe.sort_values(by=['median_house_value','ocean_proximity'])
        sort.to_csv('sort.txt',sep=',',index=False,header=False)

    def filtern(self):
        """Filtern nach einem Kriterium eine Spalte. Die Spalte und Kriterium werden von der
        Tastatur eingelesen."""
        df = pd.read_csv('housing.csv')
        ja = input('Wollen sie eine string oder eine float Spalte filtern?')
        col=input('Coloana:')
        if ja=='string':
            krit=input('Kriterium')
            filt=df[df[col]==krit]
            filt.to_csv('filter.txt',sep=',',index=False,header=False)
        else:
            if ja=='float':
                vorz=input('Grosser oder kleiner?(>/<)')
                if vorz =='>':
                    krit=float(input('Kriterium'))
                    filt1 = df[df[col] > krit]
                    filt1.to_csv('filter.txt',sep=',',index=False,header=False)
                else:
                    if vorz=='<':
                        krit = float(input('Kriterium'))
                        filt2 = df[df[col] < krit]
                        filt2.to_csv('filter.txt',sep=',',index=False,header=False)
