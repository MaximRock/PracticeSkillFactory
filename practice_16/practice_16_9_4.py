class Quests:
    def __init__(self, surname, name, city, status):
        self.surname = surname
        self.name = name
        self.city = city
        self.status = status

class Volunteer(Quests):
    def __init__(self, surname, name, city, status, job):
        super().__init__(surname, name, city, status)
        self.job = job

    def corporate(self):
        return f'Участник: {self.surname} {self.name},г.{self.city}, статус: {self.status}'

quests_db = [
    {
    "surname": "Петров",
    "name": "Петр Петрович",
    "city": "Ростов-на-Дону",
    "status": "Наставник",
    "job": "Волонтер",
    },
    {
    "surname": "Абанькин",
    "name": "Вадим Вадимович",
    "city": "Курск",
    "status": "Наставник",
    "job": "Волонтер",
    },
    {
    "surname": "Круглов",
    "name": "Сергей Александрович",
    "city": "Воронеж",
    "status": "Студент",
    "job": "Инженер",
    },
    {
    "surname": "Мишин",
    "name": "Василий Васильевич",
    "city": "Белгород",
    "status": "Ментор",
    "job": "Техник",
    },
    {
    "surname": "Воронин",
    "name": "Иван серогеевич",
    "city": "Томбов",
    "status": "Студент",
    "job": "Волонтер",
    },
]

print()
for quest in quests_db:
    for item in quest:
        if item == 'job' and quest['job'] == 'Волонтер':
            quest_obj = Volunteer(quest['surname'], quest['name'], quest['city'], quest['status'], quest['job'])
            print(quest_obj.corporate())
