def wyswietl(num1,num2):
    print(f'Liczba 1: {num1}')
    print(f'Liczba 2: {num2}')

wyswietl(3,4)

####### *args ############
def wyswietlArgs(num1, *args):
    print(f'\nPierwszy element: {num1}')
    for i in args:
        print(f'następna wartość: {i}')

wyswietlArgs(5,3,13,4,3.5)

#################

imiona =['Anna','Julia','Krzysztof','Jan']
wyswietlArgs(imiona)
wyswietlArgs(*imiona)

############czysczenie ekranu
#import os
#os.system('cls')

############## **kwargs ############

def pracownik(**kwargs):
    for key, val in kwargs.items():
        print(f'klucz: {key}, wartość: {val}')

pracownik1={
    'imie':'Jan',
    'nazwisko':'Nowak',
    'wiek':21,
    'miasto':'Poznań',
    'umowaOprace':True
}

pracownik(**pracownik1)
