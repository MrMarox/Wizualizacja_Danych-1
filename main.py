import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# zadanie 1
# a=np.arange(1,21,1)
# b=(a^2+(4*a))/(np.sin(a))
# plt.plot(a,b,'o--',label='f(x)')
# plt.xlabel('x')
# plt.ylabel('f(x)')
# plt.title('wykres z zadania 1')
# plt.show()

# zadanie 2
#       dwa wykresy na jednym
# x1=np.arange(-2,2.1,0.1)
# x2=np.arange(-3,3.1,0.1)
# y1=np.tan(x1)*np.sin(x1)
# y2=np.sin(x2)+np.tan(x2)
#
# fig,axs=plt.subplots(2,2)
# axs[0,1].plot(x1,y1,'g--')
# axs[0,1].set_title('pierwszy wykres')
# axs[0, 1].set_xlabel('x')
# axs[0, 1].set_ylabel('wynik funkcji')
# axs[0,1].legend(['tan(x)*sin(x)'])
#
# axs[1,0].plot(x2,y2,linewidth=2)
# axs[1,0].set_title('drugi wykres')
# axs[1,0].set_xlabel('x')
# axs[1,0].set_ylabel('wynik funkcji')
# axs[1,0].legend(['tan(x)+sin(x)'])
# fig.delaxes(axs[0,0])
# fig.delaxes(axs[1,1])
# plt.savefig('zad2.png')
# plt.show()

# zadanie 3
# sns.set()
# df=pd.read_csv('plik do wgrania',header=0,sep=',',decimal='.')
# print(df)
# a=df['text x'].where(df['class']=='Iris-versicolor')
# b=df['text y '].where(df['class']=='Iris-versicolor')
#
# wykres=sns.relplot(data=df,x=a,y=b,hue='class',palette='dark')
#
# plt.show()


# zadanie 4

# df=pd.read_csv('plik do wczytania',header=0,sep=';',decimal='.')
# print(df)
#
# sns.set()
# plot=sns.catplot(data=df,x='fraza x',y='fraza na y',
#                  kind='bar/pie',ci=None,hue='fraza x',
#                  estimator=np.sum,dodge=False,
#                  palette=['cyan','violet','red','green','yellow'],
#                  legend_out=True)
# plot.fig.set_size_inches(10,10)
# plt.xticks(rotation='vertical')
# plot.fig.suptitle('tytul')
# plt.show()