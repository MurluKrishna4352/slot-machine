import random #importing required modules 
MAX_LINES = 3

def deposit():
    while True: 
        amount = input("enter deposits : ")
        if amount.isdigit():
            amount = int(amount)
            if amount>0:
                break
            else:
                print("amount must be greater than 0.")
        else:
            print("Please enter a number for deposits")
    return amount


def no_of_lines():
    while True: 
        lines = (input("enter number of lines to bet on: "))
        if lines.isdigit():
            lines = int(lines)
            if lines>0:
                break
            else:
                print("number of lines must be greater than 0.")
        else:
            print("Please enter a number of lines")
    return lines



def money_bet():
    while True: 
        money = int(input("enter total money you want to bet: "))
        if money.isdigit():
            lines = int(money)
            if money>0:
                break
            else:
                print("Money to bet must be greatere than 0")
        else:
            print("Please enter a number the money to bet")
    return money


def slot_machine():
    val = {
        'A' : 10,
        'B' : 20,
        'C' : 30
    }



def main():
    bal = deposit() 
    bet_money = money_bet()
    lines = no_of_lines()

main()