#przekazywanie argumentów przez referencję
def show(name):
    print(f'Przed modyfikacją: {name}')
    name[0]='Beata'
    name[1]='Barbara'
    name[2]='Bogdan'
    print(f'Po modyfikacji: {name}')
    print(f'Id obiektu show po modyfikacji:{id(name)}')
    
data=['Anna','Agnieszka','Andzrzej']

print(f'Przed wywołaniem funkcji show: {data}')
print(f'Id obiektu show:{id(data)}')
print()
show(data)
print(f'Po wywołaniu funkcji show:{data}')

#słownik

data1={'imie':'Andrzej','nazwisko':'Nowak'}
print(f'\n Id przed modyfikacją:{id(data1)}')
show(data1)

#Przekazywanie argumentów przez wartość

print('\n')

def show1(city):
    print(f'Przed modyfikacją: {city}')
    city[0]='Beata'
    city[1]='Barbara'
    #city[2]='Bogdan'
    print(f'Po modyfikacji: {city}')
    print(f'Id obiektu show po modyfikacji:{id(city)}')

miasto=['Poznań','Gniezno']
print(f'Przed wywołaniem funkcji show: {miasto}')
print(f'\n Id przed modyfikacją:{id(miasto)}')
show1(list(miasto))
print(f'Po wywołaniu funkcji: {miasto}')

print('\n\n')

def show2(city):
    print(f'Przed modyfikacją: {city}')
    city[0]='Berlin'
    city[1]='Londyn'
    print(f'Po modyfikacji: {city}')
    print(f'Id obiektu show po modyfikacji:{id(city)}')

miasto1={
    0:'Gniezno',
    1:'Poznań'
}

miasto=['Poznań','Gniezno']
print(f'Przed wywołaniem funkcji show: {miasto1}')
print(f'\n Id przed modyfikacją:{id(miasto1)}')
show2(list(miasto1))
print(f'Po wywołaniu funkcji: {miasto1}')
