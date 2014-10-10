def prepare_meal(number):
    current_meal = ""
    if (number % 5 == 0):
        if (number % 3 != 0):
            return "eggs"
        current_meal = "and eggs"
    while (number % 3 == 0):
        current_meal = "spam " + current_meal
        number /= 3
    return current_meal

def main():
    print (prepare_meal(45))

if __name__== '__main__':
    main()
