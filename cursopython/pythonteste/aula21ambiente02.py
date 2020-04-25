def soma(a=0, b=0, c=0):
    """
    -> Faz a soma de três valores e mostra o resultado na tela.
    :param a: O primeiro valor
    :param b: O seguando valor
    :param c: O terceiro valor
    Função criada por Átila Costa na aula do canal CursoemVideo
    """
    s = a + b + c
    print(f'A soma vale {s}', end='')


#soma(3, 2, 5)
#soma(3, 2)
#soma(3)
#soma()
#soma(3, 3, 5, 8) -> vai dar erro, pois pode receber até 3 parametros
#soma(3, 3, 5)
#soma(b=4, c=2)
soma(c=3, a=2)
