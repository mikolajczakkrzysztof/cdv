def witaj():
    print('Witaj ',end='')
    print('Janusz')
witaj()
def wyswietlWiek(wiek):
    print(f'Twój wiek: {wiek}')
    
wyswietlWiek(20)

def iloczyn(a,b):
    il=a*b
    print(f'iloczyn wynosi: {il}')
print("Podaj 1 liczbe")
liczba1=input()
print("Podaj 2 liczbe")
liczba2=input()
liczba1=int(liczba1)
liczba2=int(liczba2)
iloczyn(liczba1,liczba2)

def iloraz(x,y):
    return x/y

print('Iloraz wynosi:')
iloraz(x=80,y=10)