c = 0
tot = 0

n = int(input("Digite um número [quando quiser parar, digite 999]: "))

while n != 999:
    tot += n
    c += 1
    n = int(input("Digite um número [quando quiser parar, digite 999]: "))

print(f"Você digitou {c} números e a soma entre eles é de {tot}")
