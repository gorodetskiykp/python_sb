# Функция find_min принимает 3 числа var_1, var_2 и var_3
# Необходимо произвести их сравнение 
# Наименьшее необходимо присвоить переменной min

def find_min(var_1, var_2, var_3):
    min = var_1
    if var_2 < min:
        min = var_2
    if var_3 < min:
        min = var_3
    return min


if __name__ == '__main__':
    print (find_min(5, 3, 1))

    assert find_min(5, 3, 1) == 1
    assert find_min(5, 5, 5) == 5
    assert find_min(5, -5, 50) == -5