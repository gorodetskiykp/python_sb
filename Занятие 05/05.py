# Напишите программу, в которой задается
# натуральное число n и выводится ромб из n*2-1
# ступенек, i-я ступенька должна состоять из чисел
# от 1 до i и обратно без пробелов.

N = 9

for step in range(1, N+1):
    step_string = ""
    for number in range(1, step+1):
        step_string += str(number)
    for number in range(step-1, 0, -1):
        step_string += str(number)
    print(step_string)

for step in range(N-1, 0, -1):
    step_string = ""
    for number in range(1, step+1):
        step_string += str(number)
    for number in range(step-1, 0, -1):
        step_string += str(number)
    print(step_string)