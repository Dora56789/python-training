# kérjétek be hogy a felhasználó mikor született - int-é kell konvertálni
# írjátok ki hogy ezek alapján hány éves 
# de ne csak egy számot hanem a következő üzenetet:

#mivel xxxx-ben születtél, ezért yy éves vagy.

# számoljuk ki hány éves age változóba
# írjuk ki  f stringgel a megadott üzenetet


year_of_birth = int(input("Mikor születtél?"))
print(year_of_birth)
age = 2022 - year_of_birth
print(age)

print(f"Mivel {year_of_birth} - ben születtél, ezért {age} éves vagy.")


