class Wallet:
    def __init__(self, name_id, name, money):
        self.customer_id = name_id
        self.customer = name
        self.balance = money

db_wallet = [
    {
    "customer_id": 123,
    "customer": "Иванов Иван Иванович",
    "balance": 100,
    },
    {
    "customer_id": 124,
    "customer": "Петров Петр Петрович",
    "balance": 25000,
    },
    {
    "customer_id": 125,
    "customer": "Чугунов Илья Олегович",
    "balance": 1000,
    }
]

for wallet in db_wallet:
    db_obj = Wallet(name_id=wallet.get('customer_id'),
                    name=wallet.get('customer'),
                    money=wallet.get('balance'))

    print(f'Клиент: {db_obj.customer}, баланс: {db_obj.balance} руб.')
