# Напишите программу, в которой задается
# натуральное число n и выводится лестница из
# n ступенек, i-я ступенька должна состоять из
# чисел от 1 до i без пробелов.

N = 6

for step in range(1, N+1):
    step_string = ""
    for number in range(1, step+1):
        step_string += str(number)
    print(step_string)