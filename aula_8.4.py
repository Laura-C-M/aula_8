n1 = int(input("Escolhe um número inicial: "))
n2 = int(input("Escolhe um número final: "))
print(f'Os números que entre {n1} e {n2} são:')
for x in range(n1, n2 +1, 6):
     print(x , end = ' ')