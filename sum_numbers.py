# Add össze az első tíz egész számot


j=7
# j = j + 3 # 10 lesz
j += 3 # növeljük a j változó értékét 3-al


sum = 0
for i in range(1, 11):
    sum += i
print(sum)