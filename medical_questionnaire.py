# Создайте программу “Медицинская анкета”, где вы запросите у пользователя следующие данные: имя, фамилия, возраст и
# вес. Выведите результат согласно которому:
# Пациент в хорошем состоянии, если ему до 30 лет и вес от 50 и до 120 кг,
# Пациенту требуется заняться собой, если ему более 30 и вес меньше 50 или больше 120 кг
# Пациенту требуется врачебный осмотр, если ему более 40 и вес менее 50 или больше 120 кг.
name, s_name = input('Имя: '), input('Фамилия: ')
age, weight = int(input('Возраст: ')), int(input('Вес: '))
print('{} {}, возраст {}, вес {} - '.format(name, s_name, age, weight), end='')
if age <= 30 and 50 < weight < 120:
    print('хорошее состояние.')
elif age >= 40 and (weight <= 50 or weight >= 120):
    print('следует обратится к врачу!')
elif age > 30 and (weight <= 50 or weight >= 120):
    print('следует заняться собой.')
elif age <= 30 and weight <= 50:
    print('стоит больше есть!')
elif age <= 30 and weight >= 120:
    print('стоит меньше есть!')
elif age > 30 and 50 < weight < 120:
    print('стоит делать зарядку по утрам.')
