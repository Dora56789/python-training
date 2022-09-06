base = int(input("Please enter the base of the triangle"))
height = int(input("Please enter the height of the triangle"))
area = (base * height / 2)
print(f"The area of the triangle is {area}")

# Az int függvény lepegőpontos számok esetén levágja a tizedesjegyeket

print(int(10))
print(int(10.5))