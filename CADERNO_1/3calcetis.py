from itertools import combinations

v, n = str(input()).split()
valor_total = int(v)
numeros_itens = int(n)

valores = []
for _ in range(numeros_itens):
    valores.append(int(input()))

def verificar(valores, valor_total):
    for i in combinations(valores, 3):
        alvo = 200 - valor_total
        if sum(i) == alvo:
            return True
    return False

if verificar(valores, valor_total) == True: 
    print("fretegratis")
else:
    print('fretepago')

    



