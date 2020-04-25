medida = float(input('Uma distância em metros: '))
km = medida * 0.001
hm = medida * 0.01
dam = medida * 0.1
dm = medida * 10
cm = medida * 100
mm = medida * 1000
print('A média de {} m corresponde a: '.format(medida))
print('{} km'.format(km))
print('{} hm'.format(hm))
print('{:.1f} dam'.format(dam))
print('{:.0f} dm'.format(dm))
print('{:.0f} cm'.format(cm))
print('{:.0f} mm'.format(mm))
