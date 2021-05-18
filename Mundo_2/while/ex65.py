tot = media = c = maior = menor = 0
resp = "S"

while resp == "S":
    n = int(input("Digite um número: "))
    tot += n
    c += 1
    if c == 1:
        maior = menor = n
    if n >= maior:
        maior = n
    elif n <= menor:
        menor = n
    resp = str(input("Deseja continuar [S/N]: ")).strip().upper()

media = tot / c

print(f"Você digitou {c} números e a média entre eles é {media}")
print(f"O maior número digitado foi {maior} e o menor {menor}")
