# Функция find_null принимает массив чисел mass
# Необходимо произвести подсчет количества чисел массива 
# Результат необходимо присвоить переменной sum

def find_null(mass):
    sum = 0
    for x in mass:
        if x == 0:
           sum += 1 
    return sum


if __name__ == '__main__':
    mass = [1, 0, 0, 0, 0, 1, 2, 3, 3, 4]
    print (find_null(mass))

    assert find_null([1, 0, 0, 0, 0, 1, 2, 3, 3, 4]) == 4
    assert find_null([1, 1, 0, 1, 1, 1, 0, 1, 1, 1]) == 2