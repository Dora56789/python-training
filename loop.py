# Írjuk ki 5x egymás után a nevünket (egymás alá)
# print("Dóra\n" * 5)

# i, j, k

for i in range(5):  # Ciklus fej
    print(i)
    print("Dóra")   # Ciklus törzs 
print("End")

# Feladat: Írj egy ciklust, ami kiírja a számokat 1től 100ig egymás alá
# Feladat: Írd ki egymás után a neved 5x, írd elé a sorszámot is
# Feladat: Írj egy ciklust amely 1től 10ig kiírja a számokat és azok négyzetét is egy új sorba

for i in range(1, 101):
    print(i)

for i in range(100):
    print(i + 1)


for j in range(1, 6):
    print (f"{j} Dóra")

for j in range(5):
    print(f"{j+1} Dóra")

for i in range(10):
    j = i + 1
    result = j ** 2
    print(f"A {j} szám négyzete: {result}")


# i felveszi a következő értékeket: 5 <= i > 10
for i in range(5, 10):
    print(i)

# harmadik paraméter a lépés
for i in range(10, 20, 2):
    print(i)

# lépés negatív szám, csökkenti, esetünkben 10-től 1-ig
for i in range(10,0, -1):
    print(i)


    
