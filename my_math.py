

def is_it_odd(num):
    if(num % 2 != 0):
        return True

    return False

def print_n_times(text):
    how_many = input("How many times? ")
    if(how_many.isdigit()):
        for num in range(0, int(how_many)):
            print(text)
    else:
        print("Please enter a number only")

def is_it_prime(num):
    is_not_prime = False
    if(num > 1):
        for i in range(2, num):
            if (num % i) == 0:
                is_not_prime = True
                break
    if is_not_prime:
        print(f"Your number: {str(num)} is not prime")
                
    else:
        print(f"Your number: {str(num)} is prime")       

def  user_age(dob, year):
    user_age = int(year) - int(dob)
    return f"You are {str(user_age)} years old"

def calc_tip(total, tip):
    tip_amount = float(total) * (float(tip)/100)
    return f"Tip amount: ${str(tip_amount)}"