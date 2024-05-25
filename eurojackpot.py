import random

balance = 0

# Visar nuvande balance
def get_balance():
    global balance
    return balance

# Uppdaterar balance
def set_balance(amount):
    global balance
    balance = amount

def display_welcome_message():
    current_balance = get_balance()
    print(f"Välkommen till svenska spel, ditt saldo är {current_balance} kr\n")



def user_choice():
    valid_choices = ["insättning", "eurojackpot"]
    while True:
        user_input = input("Vill du göra en 'INSÄTTNING', eller spela 'EUROJACKPOT': \n>: ").lower()

        if user_input in valid_choices:
            return user_input
        else:
            print("Ogiltigt val. Vänligen välj 'Insättning' eller 'Eurojackpot'")



def deposit():
    current_balance = get_balance()
    while True:
        print("Vilket belopp vill du sätta in? \n")
        deposit_amount = input(">: ")
        if deposit_amount.isdigit():
            deposit_amount = int(deposit_amount)
            if deposit_amount > 0:
                print(f"Vill du sätta in {deposit_amount} kr?\n ")
                answer = input(">: ").lower()
                if answer == "ja":
                    current_balance += deposit_amount
                    set_balance(current_balance)
                    print(f"Your new balance is {current_balance}")
                    break
        else:
            print("Ogiltigt belopp, försök igen.\n")
            continue

def pick_num_by_user():
    lotto_lines = []
    star_num = []
    while True:
        try:
            num_rows = input("Hur många rader vill du spela?\n >: ")
            if num_rows.isdigit():
                num_rows = int(num_rows)
                break
        except ValueError:
            print("Ogiltig inmatning\n")
    regular_nums = 5
    star_nums = 2
    rad = 0

    for lines in range(num_rows):
        current_line = []
        current_star_line = []
        rad += 1
        siffra = 0
        star_number = 0



        print(f"--- Rad {rad} ---")
        for line in range(regular_nums):
            siffra += 1
            line = input(f"Välj siffra nr {siffra}, mellan 1 - 50\n >: ")
            if line in current_line:
                print("Du har redan valt den här siffran\n")
                pick_num()
            elif not line.isdigit():
                print("Ogiltig inmatning\n")
                pick_num()
            elif not 1 <= int(line) <= 50:
                print("Ogiltig inmatning\n")
                pick_num()
            else:
                current_line.append(line)
        star_num.append(current_star_line)

        for line2 in range(star_nums):
            print(f"--- Stjärnsiffra, rad {rad} ---")
            star_number += 1
            line = input(f"Välj stjärnsiffra nr {star_number}, mellan 1 - 10\n >: ")
            if line in current_star_line:
                print("Du har redan valt den här siffran\n")
                pick_num()
            elif not line.isdigit():
                print("Ogiltig inmatning\n")
                pick_num()
            elif not 1 <= int(line) <= 10:
                print("Ogiltig inmatning\n")
                pick_num()
            else:
                current_star_line.append(line)

        lotto_lines.append(current_line)
    return lotto_lines, star_num


regular, star = pick_num_by_user()

def draw_reg_num():
    winning_numbers = []
    for i in range(5):
        winning_numbers.append(random.randint(1, 50))

    return  winning_numbers

def draw_star_num():
    winning_star_numbers = []
    for i in range(2):
        winning_star_numbers.append(random.randint(1, 10))
    return winning_star_numbers

def check_win(user_reg_nums, user_star_nums, win_reg_num, win_star_num):
    reg_num_score = 0
    star_num_score = 1
    for user_reg_num in user_reg_nums:
        reg_num_score = 0
        for i in user_reg_num:
            if i in win_reg_num:
                reg_num_score += 1
    winnings = reg_num_score * 1000

    for i in user_star_nums:
        if i in win_star_num:
            star_num_score += 1


    winnings = 1000*reg_num_score ** star_num_score
    print(f"Du vann {winnings} SEK!")




check_win(regular, star, draw_reg_num(), draw_star_num())







    # Kolla så att det finns pengar





# def run_jackpot():
