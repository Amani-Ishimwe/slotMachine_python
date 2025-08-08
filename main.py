import random

MAX_LINES = 3
MAX_BET = 100
MIN_BET = 1

ROWS = 3
COLS = 3

symbol_count = {
    "A": 2,
    "B": 4, 
    "C": 6,
    "D": 8,
}

symbol_value = {
    "A": 5,
    "B": 4, 
    "C": 3,
    "D": 2,
}

#function to check winnings
def check_winnings(columns, lines, bet, values):
    winnings = 0
    winning_lines = []
    for line in range(lines):
        symbol = columns[0][line]
        for column in columns:
            symbol_to_check = column[line]
            if symbol != symbol_to_check:
                break
        else:
            winnings += values[symbol] * bet
            winning_lines.append(line + 1)

    return winnings, winning_lines

#function to spin
def get_slot_machine_spin(rows, cols, symbols):
    all_symbols =[]
    for symbol, symbol_count in symbols.items():
        for _ in range(symbol_count):
            all_symbols.append(symbol)

    columns = []
    for _ in range(cols):
        column = []
        current_symbols = all_symbols[:]
        for _ in range(rows):
            value  = random.choice(all_symbols)
            current_symbols.remove(value)
            column.append(value)
        columns.append(column)
    return columns

#function to print the output
def print_slot_machine(columns):
    for row in range(len(columns[0])):
        for i, column in enumerate(columns):
            if i != len(columns) - 1:
                print(column[row], end=" | ")
            else:
                print(column[row], end="")
        print()

#function to deposit
def deposit():
    while True:
        amount = input("What Would You Like To Deposit? $")
        if amount.isdigit():
            amount = int(amount)
            if amount>0:
                break
            else:
                print("The amount must be greater than 0.")
        else:
            print("Please enter a valid number.")
    return amount      

#function to determine the number of lines
def get_number_of_lines():
    while True:
        lines = input("Enter the number of lines to bet on (1-3): ")
        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= MAX_LINES:
                break
            else:
                print(f"Number of lines must be between 1 and {MAX_LINES}.")
        else:
            print("Please enter a valid number.")
    return lines


#function to bet
def get_bet():
    while True:
        bet = input("What is your bet per line? $")
        if bet.isdigit():
            bet = int(bet)
            if MIN_BET <= bet <= MAX_BET:
                break
            else:
                print(f"Bet must be between ${MIN_BET} and ${MAX_BET}.")
        else:
            print("Please enter a valid number.")
    return bet

def spin(balance):
    lines = get_number_of_lines()
    
    while True:
        bet = get_bet()
        total_bet = bet * lines

        if total_bet > balance:
            print(f"You cannot bet ${total_bet}. Your balance is ${balance}.")
        else:
            break

    print(f"You are betting ${bet} on {lines} lines. Total bet is ${total_bet}.")
    slots = get_slot_machine_spin(ROWS, COLS, symbol_count)
    print_slot_machine(slots)
    winnings, winning_lines = check_winnings(slots, lines, bet, symbol_value)
    print(f"You won ${winnings}!")
    print("You won on lines:", *winning_lines)
    return winnings - total_bet


#main function
def main():
    balance = deposit()
    while True:
        print(f"Your current balance is ${balance}.")
        answer = input("Press Enter to spin (or type 'q' to quit): ")
        if answer.lower() == 'q':
            break
        balance += spin(balance)
        print(f"Your new balance is ${balance}.")
main()