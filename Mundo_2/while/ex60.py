n = int(input("Digite um número: "))
c = n
mult = 1

print(c, end=" ")
while c > 1:
    if c == n:
        c = c - 1
        print("x", c, end=" ")
        mult = n * c
    else:
        c = c - 1
        print("x", c, end=" ")
        mult = mult * c
print(" = ", mult)
print(f"Portanto, o fatorial de {n} é {mult}")
