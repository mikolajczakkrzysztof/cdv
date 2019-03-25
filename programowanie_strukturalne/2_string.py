text="Anna, paweł, JulIA"

lista=text.split(", ")
print(text)
print(lista)
print(type(lista))

imie1=lista[0]
print(imie1)

print("Twoje imię:", imie1)
imieDuze=imie1.upper()
print(imieDuze)

imieMale=imie1.lower()
print(imieMale)
print(imie1)

#sprawdzanie zawartości
print("Podaj swoje nazwisko: ",end="")
nazwisko=input()
zawartosc=nazwisko.isalpha()
print(zawartosc)

#sprawdzic dlaczego przy liczbach jest false

nazwisko=""
print(nazwisko.isalpha())

text1="\nJulia\n"
text2="Nowak"
print(text1+text2)

text1=text1.rstrip()
print(text1+" "+text2)

#wyświetlanie łańcucha znaków

#Wszystkie wersje Pythona
text="%s, Java i %s" % ("PHP","Python")
print(text)

#nowsze wersje Python >2,6v
text="{1}, Java i {0}".format("PHP","Python")
print(text)

#help(text.replace)

new=text.replace("PHP","C#")
print(new)

#wypisanie danych
rok=2019
miesiac="marzec"
dzien=25
print("Data: ",end="")
print(dzien,miesiac,rok)


print("Data: ",end="")
print(dzien,miesiac,rok, sep="-")


