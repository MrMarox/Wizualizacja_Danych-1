# import math
# a=4
# b=4
# if(a==b):
#      print("zgadza sie ")
# else :
#     print("nie sa")
#
# a=6
# b=8
# if a>b :
#     print('liczba a wieksza od b' )
# elif a<b :
#     print('liczba a mniejsza od b ')
# else :
#     print('sa rowne')


# a = input('wpisz liczbe: ')
# print(a)
# print(type(a))


# a =int(a)
# print(type(a))
# a = input('wpisz 1 liczbe: ')
# b = input('wpisz 2 liczbe: ')
# c = input('wpisz 3 liczbe: ')
# d = input('wpisz 4 liczbe: ')
# a= int(a)
# b= int(b)
# c= int(c)
# d= int(d)
# if(a>b)& (c>d):
#     print(' a jest wieksza od  b i c jest wieksza od d')
# else:
#     print('a jest mniejsza od b lub c jest mniejsza od d ')


# a=input('liczba:')
# a = int(a)
# for s in range(0, a+1, 1):
#     print(s)


# lista = ['a', 5, 6, 5, 6]
# for s in lista:
#     print(s)


# a=0
# while a<11:
#
#     print(a)
#     a+=1

# lista = [4, 6, 9, 7, 2, 3]
# liczba = input('podaj liczbe = ')
# licznik = 0
#
# while licznik <len(lista):
#     if int(liczba) - lista[licznik] == 0:
#         print('liczba ' + str(liczba) + '-' + str(lista[licznik]) + '=0')
#         break
#     else:
#         licznik += 1
# else:
#     print('zadna z wartosci nie dala odpowiedniego wyniku')


# lista1 = [4, 6, 8, 3, 9, 2]
# lista2 = [4, 7, 5, 3]
# suma = []
# for a in lista1:
#     for b in lista2:
#         wynik = a+b
#         suma.append(wynik)
#         print(suma)


# a = input('liczba a = ')
# b =input('liczba b = ')
# try:
#     a = int(a)
#     b = int (b)
#     wynik = a/b
#     print(wynik)
# except ZeroDivisionError:
#     print('nie mozna przez 0')
#
# except ValueError:
#     print('nie wczytano liczba calkowita ')


# lista = ['a', 5, 5.5]
# slownik = {5: 1, 'a': 'b', 5.5: 9.5}
# a = lista[0]
# print(slownik[a])
# # append,insert, extend, pop, remove, del, sort, reverse
# lista.pop(0)
# print(lista)
