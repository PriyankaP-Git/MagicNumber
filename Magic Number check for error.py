def ask_number(nb_min, nb_max):
    number_int = 0
    while number_int == 0:
        number_str = input(f"What is the Magic Number (between {nb_min} and {nb_max}) ? ")
        try:
            number_int = int(number_str)
        except:
            print("Error: You must enter Number")
    return number_int

Min_Number = 1
Max_Number = 10
Magic_Number = 5

number = 0
while not number == Magic_Number:
    number = ask_number(Min_Number, Max_Number)
    if number > Magic_Number:
        print("Number is greater than Magic Number")
    elif number < Magic_Number:
        print("Number is less than Magic Number")
    else:
        print("You Won")