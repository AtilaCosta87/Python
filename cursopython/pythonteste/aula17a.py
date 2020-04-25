num = [2, 5, 9, 1]
num[2] = 3
#num[4] = 7 -> não posso aumentar o tamanho da lista, apenas trocar os elementos
num.append(7)
#num.sort() -> ordenar a lista
num.sort(reverse=True)
num.insert(2, 2)

if 5 in num:
    num.remove(5)
else:
    print('Não encontrei o número 4')

#num.pop(2) -> excluir elementos da lista
print(num)
print(f'Essa lista tem {len(num)} elementos')
