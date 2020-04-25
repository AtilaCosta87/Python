frase = str(input('Digite uma Frase: ')).upper().strip()
print('A letras "A" aparece {} vezes na frase.'.format(frase.count('A')))
print('A letra primeira letra "A" apareceu na posição: {}'.format(frase.find('A')+1))
print('A ultima letra "A" apareceu na posição: {}'.format(frase.rfind('A')+1))
