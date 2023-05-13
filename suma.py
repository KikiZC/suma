vklad = input("Zadejte vklad: ")
suma = 0
for c in vklad:
    if c.isdigit():
        suma += int(c)
print("Soucet cislic je:", suma)
