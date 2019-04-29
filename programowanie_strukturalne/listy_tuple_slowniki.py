#listy
programowanie=['PHP','Python',"Java"]
print(type(programowanie))
programowanie.append('C#')
programowanie.append('PHP')
print(programowanie)
ile=programowanie.count('PHP')
print('PHP jest: ',ile)

#tuple
imiona=('Julia','Anna','Tomek')
print(type(imiona))
print(imiona)
firstName=imiona[0]
print(firstName)

#słownik
osoba={'imie':'Janusz','Nazwisko':'Nowak','Miasto':'Poznań','Wiek':21,'umowaOprace':True}
print(type(osoba))
print(osoba)
print(osoba['Miasto'])
print(osoba.get('xyz','Brak klucza'))

print(osoba.keys())


