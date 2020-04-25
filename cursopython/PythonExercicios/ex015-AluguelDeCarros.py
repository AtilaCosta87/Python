dia = int(input('Quantos dias alugados? '))
km = float(input('Quantos Km rodados? '))
pago = (dia * 60) + (km * 0.15)
print('Total a pagar é de R${:.2f}'.format(pago))
