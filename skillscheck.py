import random

def income_tax_calculator():
    print("You have selected the Income Tax Calculator")
    while True:
        try:
            income = float(input("How much did you make this year: "))
            break
        except ValueError:
            print("Please enter a valid amount.")

    tax_amount = income * 0.04
    print("Expect to pay", tax_amount, "in taxes this year")

def create_employee_account():
    print("You have selected the Employee Account Creation program")
    first_name = input("What is the employee's first name? ")
    last_name = input("What is the employee's last name? ")

    username = first_name[:3] + last_name[:4]

    word_bank = ["orange", "building", "apple", "elephant", "sunshine"]
    random_word = random.choice(word_bank)
    random_number = random.randint(10, 100)

    password = random_word + str(random_number)

    print("Generated username:", username)
    print("Generated password:", password)

while True:
    print("Welcome to Tom Nook's store management program 2024 Miranda Miller for Nook Industries")
    print("Select one of the following options:")
    print("[A] Income Tax Calculator")
    print("[B] Create an Employee Account")
    print("[C] End this Program")

    option = input("Please type in A, B, or C: ")

    if option.upper() == "A":
        income_tax_calculator()
    elif option.upper() == "B":
        create_employee_account()
    elif option.upper() == "C":
        print("Closing the program...")
        break
    else:
        print("Invalid option. Please try again.")
