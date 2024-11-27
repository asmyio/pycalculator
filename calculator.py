# you have to crete a flow:

# this was maybe user input group la
# user will input a number
# user will input another number
# user will choose what calculation they want

# tis was mabe... uh... calculation hroup la
# if the user selects +, the two numbers will add
# if the user selects -, the two numbers will be deducted
# what if I have dum dum user? I say 'sorry, cannot'
# ask the user again :D
# then reupdate the value inside the function


# this was I want it to be... output?
# I want the results to be displayed, what is it? and done.

# so... first user input, then the input is taken to another box
# then that box, uh, show me?

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