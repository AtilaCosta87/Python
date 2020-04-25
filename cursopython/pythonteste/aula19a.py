pessoas = {'Nome': 'Átila', 'Sexo': 'M', 'Idade': 31}
#print(pessoas)
#print(f'O {pessoas["Nome"]} tem {pessoas["Idade"]} anos.')
#print(pessoas.keys())
#print(pessoas.values())
#print(pessoas.items())

#for k in pessoas.keys():
#    print(k)

#for k in pessoas.values():
#    print(k)

#del pessoas['Sexo']
#pessoas['Nome'] = 'Vilmar'
pessoas['Peso'] = 98.5

for k, v in pessoas.items():
    print(f'{k} = {v}')
