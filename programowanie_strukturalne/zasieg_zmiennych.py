#zasieg zmiennych, zmienne lokalne i globalneabs

#precyzja liczby(zaokrąglenie do 3 miejsc po przecinku)

x="{0:.3f}".format(5)
print(x)

def plnToChf(value):
    kursChf=3.7536
    iloscChf=value / kursChf
    iloscChf="{0:.0f}".format(iloscChf)
    print(f'Ilosc CHF: {iloscChf}')

plnToChf(100)

Ile=input("Podaj ile masz złotówek: ")
Ile=float(Ile)
def zwrot(wartosc):
    kursEuro=4.28755406
    iloscEuro=Ile/kursEuro
    iloscEuro="{0:.0f}".format(iloscEuro)
    print(f'Ilosc Euro:{iloscEuro}')
zwrot(Ile)

#zmienna globalna

kursUSD=3.8281908
print(f'id usd: {id(kursUSD)}')


pln=input('Podaj kwotę PLN jaką chcesz wymienić na USD: ')
pln=float(pln)
def zwrotUSD(wartosc):
    #kursUSD=3.8281908
    iloscUSD=pln/kursUSD
    iloscUSD="{0:.0f}".format(iloscUSD)
    return iloscUSD


print(f'\nId dolara: {id(kursUSD)}')
print(f'\nKurs dolara: {kursUSD}')
usd=zwrotUSD(pln)
print(f'Ilość {pln}PLN={usd}USD')
print(f'Kurs USD:{kursUSD}')


###########################################################################################
zmiennaGlobalna=10
print(f'\n Wartość zmiennaGlolobalna: {zmiennaGlobalna}')
print(f'\n ID zmiennaGlobalna: {id(zmiennaGlobalna)}')

def spr():
    global zmiennaGlobalna
    zmiennaGlobalna=20
    print(f'\nWartość zmiennaGlolobalna: {zmiennaGlobalna}')
    print(f'\n ID zmiennaGlobalna: {id(zmiennaGlobalna)}')

spr()
print(f'\nWartość zmiennaGlolobalna: {zmiennaGlobalna}')





