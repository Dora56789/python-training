from urllib import robotparser


if True:
    print("Ez mindig lefut")

if False:
    print("Ez sosem fut le")

if 5 > 10:
    print("Vajon lefut-e")

n = 10
n % 2 == 0 # Páros 
n % 2 == 1 # Páratlan

# Kérj be afelhasználótól egy számot. Ha az páros írd ki hogy páros
# Ha páratlan, írd ki hogy páratlan

number = int(input ("Írj be egy számot."))
result = number % 2
if result == 0:
    print("páros")
if result == 1:
    print("páratlan")
