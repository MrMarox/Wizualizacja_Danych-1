import numpy as np
import pandas as pd
import matplotlib as ts
import matplotlib.pyplot as plt

ts = pd.Series(np.random.rand(1000))
ts = ts.cumsum()
#
# ts.plot()
# plt.show()

# dane = {'Kraj': ['Belgia', 'Indie', 'Brazylia'],
#         'Stolica': ['Bruksela', 'Delhi', 'Brasilia'],
#         'Populacja': [41190840, 1303171035, 207847528],
#         'Kontynent':['Europa','Azja','Ameryka Południowa']}
# df = pd.DataFrame(dane)

# grupa = df.groupby('Kontynent').agg({'Populacja':['sum']})
# print(grupa)
# grupa.plot(kind='bar',xlabel= 'Kontynent',ylabel='Populacja w mld',
#            rot=0,title='Populacja dla Kontynentu')
# wykres=grupa.plot.bar()
# wykres.set_xlabel('Kontynent')
# wykres.set_ylabel('Populacja w mld')
# wykres.tick_params(axis='x',labelrotation=0)
# wykres.legend(loc='best')
# wykres.set_title('Populacja na Kontynentach')
# plt.savefig('wykres.png')
# plt.show()

# df = pd.read_csv('dane.csv',header=0, sep=';',decimal='.')
# print(df)
#
# grupa = df.groupby('Imię i nazwisko').agg({'Wartość zamówienia':['sum']})
#
# grupa.plot(kind='pie',subplots=True,autopct='%.2f %%',fontsize=20,
#            figsize=(8,8),colors=['violet','green'])
# plt.legend(loc='upper left')
# plt.show()

# df = pd.DataFrame(ts)
# print(df)
# df['srednia kroczaca']=df.rolling(window=100).mean()
# df.plot()
# plt.legend(['Wartość','Średnia krocząca'])
# plt.show()