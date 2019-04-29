#przekazywanie argumentów przez referencję
def show(name):
    print(f'Przed modyfikacją: {name}')
    name[0]='Beata'
    name[1]='Barbara'
    name[2]='Bogdan'
    print(f'Pro modyfikacji: {name}')
    
data=['Anna','Agnieszka','Andzrzej']

show(data)
