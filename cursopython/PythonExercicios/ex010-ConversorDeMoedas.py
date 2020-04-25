real = float(input('Quanto dinheiro você tem na carteira? R$ '))
dolar = real / 3.68
euro = real / 4.23
print('Com R$ {:.2f} você pode comprar US$ {:.2f} e EUR$ {:.2f}'.format(real, dolar, euro))