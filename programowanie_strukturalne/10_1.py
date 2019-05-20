#Pętle zadania

#Podaj wartość początkową i końcową która będzie wypisana w porządku malejący

print("Podaj a: ")
a=int(input())
print("Podaj b: ")
b=int(input())

if b>a:
    pom=a
    a=b
    b=pom

for i in range(a,b-1,-1):
    print(i,end=' ')
print()

print("\n\n")

print("Podaj wysokosc choinki: ")
x=int(input())
print("Podaj szerokosc choinki: ")
y=int(input())

for i in range(0,x):
    for j in range(1,y+1):
        print(j * '*')
print()
print("\n\n")

ilosc=int(input("ilosc wierszy: "))
znak=input("Znak: ")

for i in range(1,ilosc+1):
    print (znak *i)
    i=i+1

print("\n\n")
a=0
b=0
print("Podaj a: ")
a=int(input())
print("Podaj b: ")
b=int(input())
suma=a+b
if suma==0:
    print("Nie można dzielić przez 0 !\n")
else:
    wyrazenie=(a*a+b)/(suma*suma)
    print("Wartość wyrazenia wynosi: ",wyrazenie)


print("\n\n")


###################################

for letter in "CDV - Poznań":
    if letter=='V':
        continue
    print(f'Litera: {letter}',end=" ")

########################################

x=10
while x>0:
    x=x-1
    if x==6:
        continue
    print(f'{x}')
print("Koniec programu")

#Użytkownik podaje hasło, jeśłi poda "okoń" to wyświetli się "Poprawne hasło", użytkownik ma na podanie hasła 3 próby, jeśli przekroczy ilość prób to będzie komunikat, przekroczono ilość prób

prog=3
while prog>0:
    prog=prog-1
    haslo=input("Podaj hasło: ")
    if haslo=="okoń":
        print("Gratulacje-Poprawne hasło")
        prog=-1
    else:
        print("Nieprawidłowe hasło")
    if prog==0:
        print("Przekroczono ilośc dozwolonych prób")

print("\n\n")





