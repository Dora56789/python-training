 # Felhasználói bevitelt tartalmazó feladatok

# input függvény
# paraméter: mit kell kiírni
# visszatérési érték: felhasználó által begépelt érték

name = input("Mi a neved?")
print(name)


# Kiírás : Helló (megadott név) !
# Trainer esetén Hello Trainer!
print("Helló " + name + "!")

# Kérjétek be a felhasználó életkorát !
# Írjátok ki a kétszeresét!

age = int(input("Hány éves vagy?"))
print(type(age))
print(age * 2)

"10" # String literál
10  # int literál

print("10" * 2)
print(10 * 2)

# Konverziós függvény 
print(type(int("10")))