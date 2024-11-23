n1 = int(input("Escolhe um número inicial: "))
n2 = int(input("Escolhe um número final: "))
n3 = int(input("Escolhe um incremento: "))
print(f'Os números entre {n1} e {n2} cujo o incremento é {n3} são:')
for x in range(n1, n2 +1, n3):
     print(x , end = ' ')