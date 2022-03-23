# class ksztalty():
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#         self.opis = 'To jest klasa dla ogolnych ksztaltow'
#
#     def pole(self):
#         return self.x * self.y
#
#     def obwod(self):
#         return self.x * 2 + self.y * 2
#
#     def dodaj_opis(self, text):
#         self.opis = text
#
#     def skala(self, czynnik):
#         self.x = self.x * czynnik
#         self.y = self.y * czynnik
#
#
# class kwadrat(ksztalty):
#     def __init__(self, x):
#         self.x = x
#         self.y = x
# class kwadratL(kwadrat):
#     def obwod(self):
#         return 8 * self.x
#     def pole(self):
#         return 3 * self.x * self.y
# kwadrat=kwadrat(5)
#
# print('Obwod:',kwadrat.obwod())
# print('Pole:',kwadrat.pole())
# kwadrat.dodaj_opis('nasza figura to kwadrat')
# print(kwadrat.opis)
# kwadrat.skala(0.3)
# print(kwadrat.obwod())
# print('')
#
# litera_L = kwadratL(5)
# print('Obwod:',litera_L.obwod())
# print('Pole:',litera_L.pole())
# litera_L.dodaj_opis('nasza figura jest w ksztalcie L ')
# print(litera_L.opis)
# litera_L.skala(0.3)
# print(litera_L.obwod())
# print('')
#
#
# class kwadrat(ksztalty):
#     def __init__(self, x):
#         self.x = x
#         self.y = x
#     def __str__(self):
#      return "kwadrat o boku {}".format(self.x)
# kwadrat=kwadrat(5)
# print(kwadrat)
#
#
#
#

# class Osoba:
#     def __init__(self,imie,nazwisko):
#         self.imie = imie
#         self.nazwisko = nazwisko
#     def przedstaw_sie(self):
#         return '{} {}'.format(self.imie, self.nazwisko)
#
# class Pracownik(Osoba):
#     def __init__(self,imie,nazwisko,pensja):
#         Osoba.__init__(self,imie ,nazwisko)
#         self.pensja = pensja
#     def przedstaw_sie(self):
#         return '{} {} i zarabiam {}zł'.format(self.imie, self.nazwisko, self.pensja)
#
# class Menago(Pracownik):
#     def przedstaw_sie(self):
#      return '{} {} i jestem menago wiec, zarabiam {}zł'.format(self.imie, self.nazwisko , self.pensja)
#
# Heniu = Pracownik('heniek','kowal',2400)
# menago = Menago('Stanisla','Ryba',8000)
#
# print(Heniu.przedstaw_sie())
# print(menago.przedstaw_sie())
#
#
# imie ='koko'
# it= iter(imie)
# print(next(it))
# print(next(it))
# print(next(it))
# print(next(it))

# class Wspak:
#     def __init__(self, data):
#         self.data = data
#         self.index = len(data)
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         if self.index == 0:
#             raise StopIteration
#         self.index = self.index - 1
#         return self.data[self.index]
#
#
# napis = Wspak('robak')
# print(napis.__next__())
# for a in napis:
#     print(a)
