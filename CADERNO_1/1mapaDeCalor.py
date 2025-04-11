#matiz 6x3 -> 6 linhas e 3 colunas
#1 = sim
#0 = nao

def iniciar():
    usuarios = int(input())
    vitorias = {'superior': 0,
            'esquerda': 0,
            'centro':0,
            'direita': 0,
            'inferior': 0}

    for _ in range(usuarios):
        matriz = criarMatriz()
        resultado = verificarMatriz(matriz)
        vitorias[resultado] += 1
    return max(vitorias, key=vitorias.get)
    

def criarMatriz():
    matriz = []
    while len(matriz) < 6:
        x = list(map(int, input().split()))
        matriz.append(x)
    return matriz

def verificarMatriz(matriz):
    superior = sum(matriz[0])
    inferior = sum(matriz[5])

    centro = sum([matriz[linha][1] for linha in range(0,5)])
    esquerda = sum([matriz[linha][0] for linha in range(0,5)])
    direita = sum([matriz[linha][2] for linha in range(0,5)])

    d = {'superior': superior,
         'inferior': inferior,
         'esquerda': esquerda,
         'direita': direita,
         'centro': centro}

    maior_valor = -1
    regiao = ''
    for key, value in d.items():
        if maior_valor < value:
            maior_valor = value
            regiao = key
    return regiao

print(iniciar())

     



    

    
    
    




