

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
    print("IDk yet")