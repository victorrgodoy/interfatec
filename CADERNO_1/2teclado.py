def start():
    words = []
    for _ in range(int(input())):
        word = str(input()).upper()
        words.append(word)

    for word in words:
        x = transform(word)
        print(x)
    
def transform(word):
    d = {
        2:'ABC',
        3:'DEF',
        4:'GHI',
        5:'JKL',
        6:'MNO',
        7:'PQRS',
        8:'TUV',
        9:'WXYZ'
    }   

    x = ''
    for i in word:
        for key, value in d.items():
            for j in value:
                if i == j:
                    x += str(key)
    return x          
        
start()

