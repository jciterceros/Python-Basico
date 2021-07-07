texto6 = ['banana', 'laranja', 'limao', 'lima', 'melancia', 'melao', 'maca', 'mamao', 'morango', 'amora', 'ameixa', 'pera', 'mexerica (bergamota)']

precissao = 2
search = 'Nichirica'

print(texto6)
print('-' * 50 + 'Pesquisa Segmentanda' + '-' * 150)
search = search.lower()
print(f'Texto a ser procurado "{search}", tamanho: {len(search)} caracteres')

segmento = []
for i in range(0, len(search)):
    segmento.append(search[i:i + precissao])
print(f'Texto foi segmentado[segmentado]: \t{segmento}')

notas = []
coincidencias = []
count = 0

for txt in texto6:
    segmentotxt = []
    for i in range(0, len(txt)): # -1
        segmentotxt.append(txt[i:i + precissao])
    count = 0
    for i in range(0, len(segmento)):
        for j in range(i-1, len(segmentotxt)):
            if str(segmento[i]) == str(segmentotxt[j]):
                coincidencias.append(1)
                count = count + 1
    notas.append(count)
maior = notas[0]
divergencia = 0
for indice in range(1,len(notas)):
    if notas[indice]>maior:
        maior = notas[indice]
    if notas[indice]==maior:
        divergencia = 1
if (maior == 1):
    print(f'Escreva novamente, texto incoerente...')
else:
    print(f'Notas: {notas}')
    print(texto6[notas.index(maior)])
