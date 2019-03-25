print("CDV")
print(2)

#potęga
potega=2 ** 10
print(potega)

#pobieranie danych z klawiatury
imie=input()
#konkatenacja
print("Twoje imię podane z klawiatury: "+imie)

nazwisko=input()
print("Twoje imię: "+imie+",Twoje nazwisko: "+nazwisko)

dlugosc=len(nazwisko)
print(type(dlugosc))
print("Długość nazwiska: ",dlugosc)

dlugosc=str(dlugosc)
print(type(dlugosc))
print("Długość nazwiska: "+dlugosc)

#Użytkownik podaje z klawiatury swój wiek, wyświetl dane w formacie:Twój wiek:.... lat.
print("\nPodaj ilość lat:", end="")
wiek=input()
print(type(wiek))
print("Twój wiek: "+wiek+" lat")

nazwisko='Kowalski'

pierwszyZnak=nazwisko[0]
print(pierwszyZnak) #K

ostatniZnak=nazwisko[len(nazwisko)-1]
print(ostatniZnak) #i
ostatniZnak=nazwisko[-1]
print(ostatniZnak) #i

#konwersja
x="S"
print(type(x))#string

#x=int(x)
print(type(x))#int

text="Jan"*2
print(text)
print(type(text)) #string

y=6
print(type(y)) #integer
y=y/2
print(type(y))
print(y) #3.0

wiek=21
print("Twój wiek: ",wiek)
wiek=str(wiek)
print("Twój wiek: "+wiek)

nazwisko="Jankowski"
print(nazwisko[0]) #J
print(nazwisko[0:3])#Jan
print(nazwisko[-2])#k
print(nazwisko[-2:])#ki
print(nazwisko[:-2])#Jankows
print(nazwisko[:-2:2])#Jnos
print(nazwisko[::2])#Jnos

print()
