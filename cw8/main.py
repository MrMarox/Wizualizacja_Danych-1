import numpy as np
import pandas as pd

# s = pd.Series([1,3,5.5,np.nan,'a'])
# print(s)

# s1 = pd.Series([10,12,8,14], index = ['a','b','c','d'])
# print(s1)
#
# dane ={'Kraj':['Belgia','Indie', 'Brazylia'],
#        'Stolica':['Bruksela','Delhi','Brasilia'],
#        'Populacja':[1119084,1303171035,207847528]}
# df = pd.DataFrame(dane)
# print(df)
#
# daty = pd.date_range('20220420',periods=5)
# df = pd.DataFrame(np.random.randn(5,4),index=daty, columns=list('ABCD'))
# print(df)
#
# iris_df = pd.read_csv('iris.csv',header=0,sep=',',decimal='.')
#
# print(iris_df)
#
# iris_df.to_csv('nowy.csv',index=False)
#
# xlsx=pd.ExcelFile('')
# df = pd.read_excel(xlsx,header=0)
#
# df.to_excel('nowy.xlsx',sheet_name='Arkusz_1',index=False)


# print(s1.a)
# print(df.iloc[[0]])
# print(df.loc[[0],['Kraj']])
# print(df.at[0,'Kraj'])
# print('Kraj:'+df.Kraj)

# print(df.sample(1))
# print(df.sample(10,replace=True))
#
# print(s1[(s1>12)])
#
# print(df[df.Populacja > 1200000000])

# szukaj = ['Belgia','Brasilia']
# print(df.isin(szukaj))

# df.loc[3]=['Polska','Warszawa',2000000]
# print(df)
#
#
#
# print(df.sort_values(by='Kraj'))
#
#

