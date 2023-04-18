from functions import print_hi, calc

print_hi()

first_num = int(input("Input first num: "))
second_num = int(input("Input second num: "))
oper = input("Input operation (add, sub, mult, div): ")

print("Result: ", calc(first_num, second_num, oper))