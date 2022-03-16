#
#
# lista=[]
# for x in range(0,10):
#     lista.append(x**2)
# print(lista)
#
#
# lista = [x**2 for x in range(0,10)]
# print(lista)
#
# lista2=[]
# for x in range(0,6):
#     lista2.append(3**x)
# print(lista2)
#
# lista2=[3**x for x in range(0, 6)]
# print(lista2)
#
# lista3=[]
# for x in lista:
#     if x % 2 != 0:
#         lista3.append(x)
# print(lista3)
#
# lista3=[x for x in lista3 if x % 2 != 0]
# print(lista3)
#
#
#
# lista=[]
# for a in [1, 2, 3]:
#     for b in [4, 5, 6]:
#         lista.append((a, b))
# print(lista)
#
# lista2 = [(a, b) for a in [1, 2, 3] for b in [4, 5, 6]]
# print(lista)


# slownik = {'PZU':'Państwowy zakład ubezpieczeń',
#            'ZUS':'Zakład ubezpieczeń społecznych',
#             'PKO':'Państwowa kasa oszczędności'}
# slownik_odwrocony = {}
# print(slownik)
#
# for key,value in slownik.items():
#     slownik_odwrocony[value] = key
# print(slownik_odwrocony)
#
# slownik2 = {value: key for key, value in slownik.items()}
# print(slownik2)

import math


# def row_kwad(a, b, c):
#     delta = b ** 2 - 4 * a * c
#     if delta < 0:
#         print('brak rozwiazań')
#         return -1
#     elif delta == 0:
#         print('jedno rozwiazanie')
#         x = (-b) / (2 * a)
#         return x
#     else:
#         print('ma dwa rozwiazania')
#         x1 = ((-b) - math.sqrt(delta)) / (2 * a)
#         x2 = ((-b) + math.sqrt(delta)) / (2 * a)
#         return x1, x2
#
#
# print(row_kwad(6, 1, 3))
# print(row_kwad(1, 2, 1))
# print(row_kwad(1, 4, 1))


# def parz(a):
#     if a % 2 == 0:
#         return 'parzysta'
#     else:
#         return 'nieparzysta'
#
#
# print(parz(4))
# print(parz(3))


# def dlugosc_odc(x1=1, y1=2, x2=3, y2=4):
#     return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
#
#
# # domyslne
# print(dlugosc_odc())
#
# # argumenty pozycyjne
# print(dlugosc_odc(4, 5, 6, 9))
#
# # dwa pierwsze argumenty , kolejne dwa wpisywane wartosci
# print(dlugosc_odc(1, 1, y2=8, x2=7))
# # manipulacja argumentami x1=liczba, x2=liczba, y2=liczba, y1=liczba,


# def ciag(*liczba):
#     if len(liczba) == 0:
#         return 0
#     else:
#         suma = 0
#         for i in liczba:
#             suma += i
#         return suma
#
#
# print(ciag())
# print(ciag(1, 2, 3, 4, 5, 6, 7, 8))

# def co_lubie(** rzeczy):
#     for cos in rzeczy:
#         print('lubie')
#         print(cos)
#         print('co lubie')
#         print(rzeczy[cos])
#
# co_lubie(gry =['planszowe','komputerowe'])
