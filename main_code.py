# Obtendo o valor total
renda_mensal = float(input('Qual a sua renda mensal? R$ '))

# Obtendo as percentagens
obter_50_percento = (50 / 100) * renda_mensal
obter_30_percento = (30 / 100) * renda_mensal
obter_20_percento = (20 / 100) * renda_mensal

print("=================================================\nSeus numeros de 50% 30% 20%\n=================================================")

print('Necessidades: R$ {:,.2f}'.format(obter_50_percento))
print('Gastos: R$ {:,.2f}'.format(obter_30_percento))
print('Poupanças: R$ {:,.2f}'.format(obter_20_percento))

print("\n===============================================")
