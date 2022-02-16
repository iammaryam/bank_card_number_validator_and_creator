from random import randint


def nums_or_validate_num():
    user_answer = "False"
    while user_answer not in ["v", "m"]:
        user_answer = input("Do you want to validate a card number or members of valid card numbers?"
                            " say validate with 'v', members with 'm':\n")
        return user_answer


def bank_card_input():
    bank_card_num = 'False'
    while bank_card_num.isdigit() == False or len(bank_card_num) != 16:
        bank_card_num = input("please inter bank card number(this should be 16 numbers):")
        if bank_card_num.isdigit() == False or len(bank_card_num) != 16:
            print("Please inter all of 16 numbers and in the form of digit !!")
    return bank_card_num


def put_card_members():
    while True:
        try:
            card_members = input("please say us how many card number you want:(for example 50):\t")
        except TypeError:
            print("Please inter a number as same as '50' !!")
        else:
            break
    return int(card_members)


def put_first_six_or_not():
    answer = "False"
    while answer not in ["yes", "no"]:
        answer = input("Do you want to write 6 first digits to determine this card numbers"
                       " should be for which one of Iran banks ? 'yes' or 'no' : ")
    return answer


def first_digits():
    six_digits = "False"
    while six_digits.isdigit() != True or len(six_digits) != 6:
        six_digits = input("Please inter 6 digits correctly: ")
    return six_digits


def create_random_card_number(first_digit="nothing"):
    if first_digit == "nothing":
        y = ""
        for num in range(16):
            integer = randint(0, 9)
            y = y + str(integer)
        return y
    else:
        y = first_digit
        for num in range(10):
            integer = randint(0, 9)
            y = y + str(integer)
        return y


def validity_test(number):
    nums_list = list(number)
    x = 0
    for num in nums_list[::2]:
        if int(num) * 2 > 9:
            num = (int(num) * 2) - 9
            x = x + num
        else:
            num = (int(num) * 2)
            x = x + num

    for num in nums_list[1::2]:
        if int(num) * 1 > 9:
            num = (int(num) * 1) - 9
            x = x + num
        else:
            num = (int(num) * 1)
            x = x + num

    if x % 10 == 0:
        return "This bank card number is valid"

    else:
        return "This bank card number isn't valid"


def save_card_nums_to_file(num_member):
    num_list = []
    f = open("nums.txt", "w")
    if put_first_six_or_not() == "yes":
        six_digit = first_digits()
        while len(num_list) != num_member:
            rnd_num = create_random_card_number(six_digit)
            valid_num = validity_test(rnd_num)
            if valid_num == "This bank card number is valid":
                num_list.append(rnd_num)
    else:
        while len(num_list) != num_member:
            rnd_num = create_random_card_number()
            valid_num = validity_test(rnd_num)
            if valid_num == "This bank card number is valid":
                num_list.append(rnd_num)
    print(" Ok !! card numbers are saved in a file with 'nums.txt' name .")
    f.write(str(num_list))
