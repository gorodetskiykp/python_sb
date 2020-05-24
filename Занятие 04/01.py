# Функция find_min принимает 2 числа var_1 и var_2
# Необходимо произвести их сравнение 
# Наименьшее необходимо присвоить переменной min

def find_min(var_1, var_2):
    min = var_1
    if var_2 < min:
        min = var_2
    return min


if __name__ == '__main__':
    print (find_min(5, 3))

    assert find_min(5, 3) == 3
    assert find_min(5, 5) == 5