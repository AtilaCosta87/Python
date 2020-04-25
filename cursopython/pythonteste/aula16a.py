lanche = ('Hambúrger', 'Suco', 'Pizza', 'Pudim', 'Batata Frita')
# Tuplas são imutáveis
# lanche[1] = 'Refrigerante' <- Não pode ser  feito

# print(len(lanche)) <- Saber o tamanho da tupla

for comida in lanche:
    print(f'Eu vou comer {comida}')

for cont in range(0, len(lanche)):
    print(f'Eu vou comer {lanche[cont]} na posição {cont}')

for pos, comida in enumerate(lanche):
    print(f'Eu vou comer {comida} na posição {pos}')

print('Comi pra caramba!')
