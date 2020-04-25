larg = float(input('Largura da parede: '))
alt = float(input('Altura de parede: '))
area = larg * alt
tinta = area / 2
print('Sua parede tem a dimensão de {} x {} e a área é de {}m².'.format(larg, alt, area))
print('Para pintar essa parede, você precisará de {}l de tinta.'.format(tinta))