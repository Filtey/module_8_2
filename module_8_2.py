def personal_sum(numbers):
    result = 0
    incorrect_data = 0
    try:
        for value in numbers:
            try:
                result += value
            except TypeError:
                print(f'Некорректный тип данных для подсчёта суммы - {value}')
                incorrect_data += 1
    except TypeError:
        print('В numbers записан некорректный тип данных')
        return -1

    return result, incorrect_data


def calculate_average(numbers):
    rez = 0
    summ = personal_sum(numbers)
    if(summ == -1): return
    ccount = 0
    for value in numbers:
        if(type(value) is int):
            ccount += 1
    try:
        rez = summ[0]/ccount
    except ZeroDivisionError:
       pass
    finally:
        return rez

print(f'Результат 1: {calculate_average("1, 2, 3")}') # Строка перебирается, но каждый символ - строковый тип
print(f'Результат 2: {calculate_average([1, "Строка", 3, "Ещё Строка"])}') # Учитываются только 1 и 3
print(f'Результат 3: {calculate_average(567)}') # Передана не коллекция
print(f'Результат 4: {calculate_average([42, 15, 36, 13])}') # Всё должно работать