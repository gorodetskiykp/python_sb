# Функция find_equal принимает 3 числа var_1, var_2 и var_3
# Необходимо произвести их сравнение 
# Количество повторяющихся чисел необходимо присвоить переменной count

def find_equal(var_1, var_2, var_3):
    if var_1 == var_2 == var_3:
        count = 3
    elif var_1 == var_2 or var_1 == var_3 or var_2 == var_3:
        count = 2 
    else:
        count = 0
    return count


if __name__ == '__main__':
    print (find_equal(5, -5, 5))

    assert find_equal(5, 3, 1) == 0
    assert find_equal(5, 5, 5) == 3
    assert find_equal(5, -5, 5) == 2