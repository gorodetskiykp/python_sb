# Функция find_sum принимает массив чисел mass
# Необходимо произвести сумму чисел массива 
# Результат необходимо присвоить переменной sum

def find_sum(mass):
    sum = 0
    for x in mass:
        sum += x
    return sum


if __name__ == '__main__':
    mass = [1, 0, 0, 0, 0, 1, 2, 3, 3, 4]
    print (find_sum(mass))

    assert find_sum([1, 0, 0, 0, 0, 1, 2, 3, 3, 4]) == 14
    assert find_sum([1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 10