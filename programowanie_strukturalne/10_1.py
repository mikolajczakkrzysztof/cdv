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




