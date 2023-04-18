from constants import HELLO, ADD, SUB, MULT, DIV

def print_hi():
    print(HELLO)

def calc(first_num, second_num, str):
    if str == ADD:
        return first_num + second_num
    elif str == SUB:
        return first_num - second_num
    elif str == MULT:
        return first_num * second_num
    elif str == DIV and second_num:
        return first_num / second_num
    else:
        return "error("
    