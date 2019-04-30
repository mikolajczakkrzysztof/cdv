#pętla for

colors=['red','green','blue','magenta']
print(colors)
print(type(colors))

for i in colors:
    print(f'{i}',end=" ")
print('\n')

#wypisz tekst
string='CDV - uczelnia ludzi ciekawych'

for letter in string:
    print(letter,end=" ")

print()
#wypisz liczby z przedziału <1;10>
for i in range(1,11):
    print(i,end=' ')
print()
