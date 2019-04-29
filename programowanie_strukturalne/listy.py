#programowanie=[listy] (tuple) {słowniki}
programowanie=['Python','C#','PHP','Java','JS']
print(programowanie)
print(type(programowanie))

first=programowanie[0]
print(first)
print(f'Pierwszy język programowania w liście: {first}')

last=programowanie[-1]
print(f'Ostatni język programowania w liście: {last}')

threeElements=programowanie[0:3]
print(threeElements)

#Dodanie nowego elementu na końcu listy
programowanie.append('R')
print(programowanie)

#Zliczanie elementów w liście
ile=programowanie.count('Python')
print(ile)
programowanie.append('Python')
ile=programowanie.count('Python')
print(ile)

iloscElementow=len(programowanie)
print(iloscElementow)


#Połączenie liści
print(programowanie)
inneJezyki=['C','C++']
programowanie.extend(inneJezyki)
print(programowanie)

#wyczyszczenie listy
nowa=programowanie
print(id(programowanie))
print(id(nowa))
print(nowa)
nowa.append("GO")
print(nowa)
print(programowanie)
nowa.clear()
print(nowa)
print(programowanie)