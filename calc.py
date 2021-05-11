
# imports
import my_math
import time

# global vars

# functions
def print_menu():
    print("----------------------")
    print(' Welcome to PyCalc')
    print("----------------------")
    print('1------Sum')
    print('2------Subtract')
    print('3------Multiply')
    print('4------Division')
    print('5------Is it odd?')
    print("6------Is it prime?")
    print('7------Print your text * times')
    print('q -----Quit')
    print("")

# instructions
selected_option = ""
while(selected_option != 'q'):
    print('\n\n\n')
    print_menu()
    selected_option = input('Choose an option: ')
    if(selected_option == 'q'):
        print("Goodbye")
        exit()
    elif(selected_option.isdigit()):
        print('You chose Option: ' + selected_option)
        if(int(selected_option) < 7 & int(selected_option) > 4):
            num1 = float(input("Provide number 1: "))
            return num1
        elif(int(selected_option) < 4 & int(selected_option) > 0):
            num2 = float(input("Provide number 2: "))
        else:
            print("Please enter a number from the list")
    else:
        print("Please enter a number from the list")


    if(selected_option == '1'):
        res = num1 + num2
        print(F'Result: {res}')
    elif (selected_option == '2'):
        res = int(num1) - int(num2)
        print(F'Result: {res}')
    elif (selected_option == '3'):
        res = int(num1) * int(num2)
        print(F'Result: {res}')
    elif (selected_option == '4'):
        res = int(num1) / int(num2)
        print(F'Result: {res}')
    elif (selected_option == '5'):
        if(my_math.is_it_odd(num1)):
            print("Your number is odd")
        else:
            print("Your number is even")
    elif (selected_option == "6"):
        my_math.is_it_prime(num1)
    elif (selected_option == '7'):
        print_text = input("Enter text to print: ")
        print(my_math.print_n_times(print_text))
    
    time.sleep(2)

