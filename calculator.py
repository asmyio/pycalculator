def user_input():
    first_number = int(input('hi user, input 1st number pls? \n'))
    second_number = int(input('hi user, input 2nd number pls? \n'))
    choice = input('sooo.. you want add or minus?\n')
    return first_number, second_number, choice

def calculation(num1, num2, option):
    x = 0
    while(x == 0):
        if(option == '+'):
            result = num1 + num2
            break
        elif(option == '-'):
            result = num1 - num2
            break
        else:
            print('sorry cannot, pls try again')
            num1, num2, option = user_input()
    return result

def calc_output(calc_value):
    print(f'The calculation result is: {calc_value}')

def main():
    first_num, sec_num, opsen = user_input()
    number_returned = calculation(first_num, sec_num, opsen)
    calc_output(number_returned)

if __name__ == '__main__':
    main()