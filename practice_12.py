per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}
deposit = list(map(float, per_cent.values()))
money = int(input('Введите сумму вклада: '))

for i in range(len(deposit)):
    deposit[i] = deposit[i] * money / 100
    deposit[i] = int(deposit[i])
print(deposit)
print('Максимальная сумма, которую вы можете заработать — ', max(deposit))