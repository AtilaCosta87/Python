a = [2, 3, 4, 7]
# b = a -> cria uma ligação entre a e b
b = a[:] # -> cria uma copia de a em b
b[2] = 8
print(f'Lista A: {a}')
print(f'Lista B: {b}')
