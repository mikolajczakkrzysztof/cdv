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



