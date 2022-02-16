from functions import *


if __name__ == "__main__":
    nums_or_validate = nums_or_validate_num()
    if nums_or_validate == "v":
        number = bank_card_input()
        result = validity_test(number)
        print(result)
    else:
        member = put_card_members()
        save_card_nums_to_file(member)
