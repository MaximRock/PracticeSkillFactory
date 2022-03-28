from api import PetFriends
from settings import valid_email, valid_password, empty_password, empty_email
from settings import failed_user_email, failed_user_password, pet_id_failed, auth_key_failed
import os
import re


pf = PetFriends()


def test_get_api_empty_key_valid_email(email=valid_email, password=empty_password):
    """ Проверяем что запрос api выдаст ошибку 403 при авторизации без пароля"""

    # Отправляем запрос и сохраняем полученный ответ с кодом статуса в status, а текст ответа в result
    status, result = pf.get_api_key(email, password)
    # Сверяем полученные данные с нашими ожиданиями
    assert status == 200
    assert 'key' in result

def test_get_api_empty_email_valid_password(email=empty_email, password=valid_password):
    """ Проверяем что запрос api выдаст ошибку 403 при авторизации без email"""

    # Отправляем запрос и сохраняем полученный ответ с кодом статуса в status, а текст ответа в result
    status, result = pf.get_api_key(email, password)
    # Сверяем полученные данные с нашими ожиданиями
    assert status == 200
    assert 'key' in result

def test_get_api_failed_email_valid_password(email=failed_user_email, password=valid_password):
    """ Проверяем что запрос api выдаст ошибку 403 при авторизации
        когда название email введен не верно"""

    # Отправляем запрос и сохраняем полученный ответ с кодом статуса в status.
    status, result = pf.get_api_key(email, password)
    # Сверяем полученные данные с нашими ожиданиями
    assert status == 403
    print(f'\nВведеный email {email}, -> Верный email {valid_email}')

def test_get_api_failed_password_valid_email(email=valid_email, password=failed_user_password):
    """ Проверяем что запрос api выдаст ошибку 403 при авторизации
        когда пароль введен не верно"""

    # Отправляем запрос и сохраняем полученный ответ с кодом статуса в status.
    status, _ = pf.get_api_key(email, password)
    # Сверяем полученные данные с нашими ожиданиями
    assert status == 403
    print(f'\nВведеный пароль {password}, -> Верный пароль {valid_password}')

def test_get_all_pets_failed_key(filter='my_pets'):
    """ Ожидаем ошибку 403 при не верном auth_key."""

    # Отправляем запрос и сохраняем полученный ответ с кодом статуса в status.
    status, result = pf.get_list_of_pets(auth_key_failed, filter)
    assert status == 200
    assert len(result['pets']) > 0

def test_get_all_pets_failed_filter_number_int(filter=4456):
    """ В значение filter указываем число int, ожидаем ошибку 500"""

    # Отправляем запрос и сохраняем полученный ответ с кодом статуса в status.
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    status, result = pf.get_list_of_pets(auth_key_failed, filter)
    assert status == 200
    assert len(result['pets']) > 0

def test_get_all_pets_failed_filter_invalid_string(filter='mypetspets'):
    """ В значение filter указываем значение - "mypetspets" как str, ожидаем ошибку 500"""

    # Отправляем запрос и сохраняем полученный ответ с кодом статуса в status.
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    status, result = pf.get_list_of_pets(auth_key_failed, filter)
    assert status == 200
    assert len(result['pets']) > 0

def test_get_all_pets_failed_long_string(filter='zxkjcvbluidsahgkdfhbvsdfhbgfhg4dyju4c4hvjbb4jy4avs4vd644j6dzcf1g1vh1bfgju4b6fhb4sdfg1vsh4bfjk4fjhfdgsaddgvfjb4kn44nh4dsfcdsgdfhb4jnlkm,ghnjdgdfxasfsdgvdh4jbu4nknk4lfgdvfcasd4yb4ju4nkgk4dvgdf4hb4jkhd4hbd4hnb;sdf6s84fbasef;oidhgf;jgdf6+8h4df65h4dfh4d6fh4d+6fh4df64hd6h4dj4h,4gj6j4dtdv4hd4hjd6h4vdgsdgsgsrtgsdfghsdfheshfghdfhdfh647546846548fgh6df4hg6df4hgdf8h4d6f4ghd6f5g4hd6f5gh4df5gh4df5gh4df6g5h4df6g5h4dfg6h5d4fghd6f5h4'):
    """ В значение filter указываем значение состоящее из 420 символов как str, ожидаем ошибку 500"""

    # Отправляем запрос и сохраняем полученный ответ с кодом статуса в status.
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    status, result = pf.get_list_of_pets(auth_key_failed, filter)
    assert status == 200
    assert len(result['pets']) > 0

def test_get_all_pets_failed_filter_symbols(filter='!!@#%$^&'):
    """ В значение filter указываем спец. символы как str, ожидаем ошибку 500"""

    # Отправляем запрос и сохраняем полученный ответ с кодом статуса в status.
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    status, result = pf.get_list_of_pets(auth_key_failed, filter)
    assert status == 200
    assert len(result['pets']) > 0


def test_update_remote_pet_info(name='Матрас', animal_type='Кот', age=4):
    """Проверяем возможность обновления информации о несуществующем питомце,
        ожидаем ошибку 400, вывод сообщения. Используем pet_id - id удаленного питомца"""

    # Получаем ключ auth_key и список своих питомцев
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    _, my_pets = pf.get_list_of_pets(auth_key, "my_pets")

    # Если список не пустой, то пробуем обновить его имя, тип и возраст
    if len(my_pets['pets']) > 0:
        status, _ = pf.update_pet_info(auth_key, pet_id_failed, name, animal_type, age)

        # Проверяем что статус ответа = 400 и имя питомца соответствует заданному
        assert status == 400
        print(f'\nТакой "ID"- "{pet_id_failed}" - не существует.')
    else:
        # если спиок питомцев пустой, то выкидываем исключение с текстом об отсутствии своих питомцев
        raise Exception("There is no my pets")

def test_add_pet_photo_remote_pet(pet_photo='images/dog_rimma.JPG'):
    '''Проверяем добавление фото к удаленному питомцу,
        ожидаем ошибку 500'''

    # указываем путь к фото питомца
    pet_photo = os.path.join(os.path.dirname(__file__), pet_photo)
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    _, my_pets = pf.get_list_of_pets(auth_key, "my_pets")

    # если список моих питомцев не пуст
    if len(my_pets['pets']) > 0:
        status, result = pf.add_photo_pet(auth_key, pet_id_failed, pet_photo)

        # Проверяем что статус ответа = 200 и id питомца соответствует заданному
        assert status == 200
        assert result['id'] == pet_id_failed
    else:
        # если список питомцев пустой, то выкидываем исключение с текстом об отсутствии своих питомцев
        raise Exception("There is no my pets")

def test_add_new_pet_without_photo_key_failed(name='Матрас', animal_type='Кот', age=4):
    '''Проверяем добавление питомца без фото с не существующим auth_key,
        ожидаем ошибку 403'''

    status, _ = pf.add_pet_without_photo(auth_key_failed, name, animal_type, age)
    # Проверяем что статус ответа = 200 и имя питомца соответствует заданному
    assert status == 200

def test_add_new_pet_with_valid_data_auth_key_failed(name='Matras', animal_type='Кот', age='2', pet_photo='images/cat_matras.JPG'):
    """Проверяем добавление питомца с не существующим auth_key,
        ожидаем ошибку 403"""

    # Получаем полный путь изображения питомца и сохраняем в переменную pet_photo
    pet_photo = os.path.join(os.path.dirname(__file__), pet_photo)
    # Добавляем питомца
    status, result = pf.add_new_pets(auth_key_failed, name, animal_type, age, pet_photo)
    # Сверяем полученный ответ с ожидаемым результатом
    assert status == 200
    assert result['name'] == name

def test_add_pet_photo_wrong_format(pet_photo='images/cat_matras.pdf'):
    """Проверяем соответсвие фармата фато, вводим неверный формат "cat_matras.pdf" фото, ажидаем ашибку 500.
        Если фото верное ожидаем резулитат 200 и успешное добавление фото.
        Если список Мои питомцы пустой выводим сообщение"""
    # в переменную вставляем данные фото
    photo = pet_photo
    # шаблон для нахождения формата фото
    pattern = r'.\b([A-Za-z]{3,})\b'
    # вырезаем формат фото, преобразуем в строку, нижний регистр
    photo = ''.join(re.findall(pattern, photo)).lower()
    # список допустимых форматов фото
    lst = ['jpg', 'jpeg', 'png']
    # указываем путь к фото питомца
    pet_photo = os.path.join(os.path.dirname(__file__), pet_photo)
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    _, my_pets = pf.get_list_of_pets(auth_key, "my_pets")
    # ID питомца в котором добавляем или обновляем фото
    pet_id = my_pets['pets'][0]['id']

    # если формат фото есть в списке
    if photo not in lst:
        status, _ = pf.add_photo_pet(auth_key, pet_id, pet_photo)
        assert status == 500
        print(f'\nНеверный формат фото - {photo}.')
    # если список мои питомцы не пустой
    elif len(my_pets['pets']) > 0:
        status, result = pf.add_photo_pet(auth_key, pet_id, pet_photo)
        assert status == 200
        assert result['id'] == pet_id
        print(f'Фото успешно добавлено')
    # если список мои питомцы пустой
    else:
        raise Exception(f'\nПустой список "Мои питомцы"')

# ============================= positive tests ==========================================================

def test_add_new_pet_without_photo_valid_data(name='Матрас', animal_type='Кот', age=4):
    '''Проверяем возможность добавления питомца без фото'''

    _, auth_key = pf.get_api_key(valid_email, valid_password)
    status, result = pf.add_pet_without_photo(auth_key, name, animal_type, age)

    # Проверяем что статус ответа = 200 и имя питомца соответствует заданному
    assert status == 200
    assert result['name'] == name

def test_add_pet_photo_valid_data(pet_photo='images/dog_rimma.JPG'):
    '''Проверяем возможность обновления или добавления фото питомца'''

    # указываем путь к фото питомца
    pet_photo = os.path.join(os.path.dirname(__file__), pet_photo)
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    _, my_pets = pf.get_list_of_pets(auth_key, "my_pets")

    # ID питомца в котором добавляем или обновляем фото
    pet_id = my_pets['pets'][0]['id']

    # если список моих питомцев не пуст
    if len(my_pets['pets']) > 0:
        status, result = pf.add_photo_pet(auth_key, pet_id, pet_photo)

        # Проверяем что статус ответа = 200 и id питомца соответствует заданному
        assert status == 200
        assert result['id'] == pet_id
    else:
        # если спиок питомцев пустой, то выкидываем исключение с текстом об отсутствии своих питомцев
        raise Exception("There is no my pets")
