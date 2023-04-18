from functions import print_hi, calc, check_num

print_hi()

first_num = check_num(input("Input first num: "))
second_num = check_num(input("Input second num: "))
oper = input("Input operation (add, sub, mult, div): ")

print("Result: ", calc(first_num, second_num, oper))

