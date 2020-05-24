# Напишите программу, в которой задается
# натуральное число n и выводится пирамида из
# n ступенек, i-я ступенька должна состоять из
# чисел от 1 до i и обратно без пробелов.

N = 10

for step in range(1, N+1):
    step_string = ""
    for number in range(1, step+1):
        step_string += str(number)
    for number in range(step-1, 0, -1):
        step_string += str(number)
    print(step_string)


max_step = N * 2 - 1

for step in range(1, N+1):
    step_string = ""
    for number in range(1, step+1):
        step_string += str(number)
    for number in range(step-1, 0, -1):
        step_string += str(number)
    step_empty_side_count = int((max_step - len(step_string)) / 2)
    step_empty_side = " " * step_empty_side_count
    print(step_empty_side + step_string + step_empty_side)