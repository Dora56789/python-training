# Ciklusok egymásba ágyazása 
for i in range(3):
    for j in range(5, 10):
            print(f"{i} - {j}")

# Írjátok ki a 10 x 10-es szorzótáblát

for i in range(1, 11):
    for j in range(1, 11):
        print(f"{i} * {j} = {i * j}")

# Írjuk ki a szorzótáblát négyzet alakban
line = ""   # üres string, 0 karaktert tartalmazó string, 0 hosszú string
for i in range(1, 11):
    line += str(i) + " "
print(line)

for i in range(1, 11):
    line = ""
    for j in range(1, 11):
        result= i * j
        if result < 10:
            line += " "
        line += str(i * j) + " "
    print(line)

# Ciklusban lehet elágazás is 