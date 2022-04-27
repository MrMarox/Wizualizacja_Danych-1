import numpy as np
import pandas as pd
import matplotlib as ts
import matplotlib.pyplot as plt

df = pd.read_excel('imiona.xlsx')
print(df)

# zad 1

# grupa = df.groupby('Rok').agg({'Liczba':['sum']})
# grupa.plot()
# print(grupa)
# plt.show()

# zad 2

# grupa = df.groupby('Plec').agg({'Liczba':['sum']})
#
# grupa.plot(kind='bar',xlabel= 'Plec',ylabel='mln',
#            rot=0,title='urodziny chlopcow i dziewczynek 2000-2017')
# plt.legend(loc='lower left')
# plt.show()

# zad 3

# df = df[df['Rok']>=2012]
# grupa = df.groupby('Plec').agg({'Liczba':['sum']})
# grupa.plot(kind='pie',subplots=True,autopct='%.2f %%',fontsize=20,
#            figsize=(8,8),colors=['violet','blue'])
# print(grupa)
# plt.show()

# zad 4

# df = pd.read_csv('zamowienia.csv',header=0, sep=';',decimal='.')
# print(df)
# grupa = df.groupby('Sprzedawca').size()
# grupa.plot(kind='bar',xlabel= 'Sprzedawcy',ylabel='ilosc zamowien',
#            rot=0,title='zamowienia sprzedawcow')
# plt.show()
# print(df)

