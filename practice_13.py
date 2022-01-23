ticket = int(input('Сколько билетов хотите приобрести?\n'))
price = []

for i in range(1, ticket + 1):
    age = int(input(f'Возраст {i} участника?\n'))
    if age < 18:
        price.append(0)
        print(f'стоимость {i} билета',* price[-1:], 'рублей.')
    elif 18 <= age <=25:
        price.append(990)
        print(f'стоимость {i} билета',* price[-1:], 'рублей.')
    elif age > 25:
        price.append(1390)
        print(f'стоимость {i} билета',* price[-1:], 'рублей.')
    print()

if ticket > 3:
    total_amount = int(sum(price) - ((sum(price) / 100) * 10))
    print(f'Общая стоимость {ticket} билетов с учетом cкидки 10 % \n',total_amount, 'рублей.')
else:
    print(f'Общая стоимость {ticket} билетов \n', sum(price),'рублей.')
