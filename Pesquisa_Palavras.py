import pandas as pd

texto = 'O problema é que, analisando o histórico dos clientes dos últimos anos, você percebeu que a empresa está' \
        ' com Churn de mais de 26% dos clientes.'
texto2 = 'Laranja, Limão, Melancia, Melão, Maçã, Mamão, Morango, Ameixa, Pera, Mexerica (bergamota), Banana, Abacaxi,'\
        ' Abacate, Uva, Goiaba, Kiwi, Manga, Maracujá, Pêssego'

#print(texto)

def find(search, txt):
    #print('\n')
    print(txt)
    print(f'Texto a ser procurado "{search}", tamanho: {len(search)} caracteres')
    segmento = []
    for i in range(0, len(search)):
        segmento.append(search[i:i+3])
    print(f'Texto foi segmentado: {segmento}\n')

    count = 0
    valores = []
    for i in range(0, len(txt)):
        if txt[i:i+3] in segmento:
            count += 1
            valores.append(txt[i:i+3])
            #print(f'Achei {count} fragmento do texto')
        #print(txt[i:i + 3])
    if count > 2:
        print(valores)
        print(f'Achei {count} coincidencias no texto...')
        print('E muito provavel que o texto esteja dentro....')
    elif count <= 2:
        print(valores)
        print(f'Achei {count} coincidencias no texto...')
    #else:
    #    print(f'Nao achei {count} coincidencias no texto...')


if __name__ == "__main__":
    find('maracuja', texto2.lower())
    pass