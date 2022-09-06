from ast import Add
from audioop import add


names =  ["Joe" , "Jack" , "Jane"]

# végigiterálunk a names változó elemein
for name in names:
    print(name)

#enumerate függvényt kell használni, ha az indexhez hozzá szeretnénk férni
for i, name in enumerate(names):
    print(i)
    print(name)

counter = 10
for name in names:
    print (counter)
    print(name)
    counter +=1

# Írd ki az első három hónap nevét egymás alá
# 2. Írd ki hogy "Az év egyik hónapja január" az első három hónappal
# 3. Hozz létre egy listát  3, 7, 9, 13 számokkal. Add össze a listában lévő számokat


numbers = [3, 7, 9, 13]
sum = 0
for number in numbers:
    sum  += number
    print(sum)

months = ["Január" , "Február" , "Március"]
for month in months:
    print (month)

months = ["Január" , "Február" , "Március"]
for month in months:
    print("Az év egyik hónapja a " + month)


numbers = [3, 7, 9, 13]
sum = 0
for number in numbers:
    print(number)
    sum += number
print(sum)

numbers = [3, 7, 9, 13]
sum = 0 # 0
number = 3
sum += number # 0 + 3 = 3
number = 7
sum += number # 3 + 7 = 10
number = 9
sum += number # 10 + 9 = 19
number = 13
sum += number # 19 + 13 = 32
print(sum)



