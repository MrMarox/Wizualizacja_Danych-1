import numpy as np
print('---------------')
# zad 1

a = np.arange(4, 20, 4)
print(a)

print('---------------')
# zad 2

b= np.array([2.4,5.2,7.3])
print(b.dtype)
print(b)
c = b.astype('int32')
print(c.dtype)
print(c)

print('---------------')

#zad 3

def tablicaNWymiarowa(n):
    m=np.zeros((pow(2,n),pow(2,n)))
    return m
print(tablicaNWymiarowa(3))

print('---------------')
#zad 4

def generuj(liczba, rozmiarTablicy):
    wynik=np.logspace(1,rozmiarTablicy,num=rozmiarTablicy,base=liczba, dtype="int32")
    return wynik
print(generuj(3,4))
print('---------------')
#zad 5

def wektor(dlugoscWektora):
    a=np.arange(dlugoscWektora)
    odwrocony=a[::-1]
    macierz=np.diag([a for a in odwrocony],2)
    return macierz
print(wektor(5))
print('---------------')
#zad 6

wykreslanka=np.array([["s","l","o","w","o","t","o","k"],["x","d","f","ó","j","a","e","p"],["p","o","r","ł","z","n","d","k"]])
print(wykreslanka)
print('---------------')
#zad 7

def macierz(n):
    x=np.zeros((n,n))
    for i in range(0,n):
        for j in range(0,n):
            if(j>i):
                x[i,j]=abs(2*(j-i+1))
            else:
                x[i,j]=abs(2*(i-j+1))

    return x
print(macierz(3))
print('---------------')
