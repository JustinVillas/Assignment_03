# Amount_money = int(input("Amount of money that you have? "))
# Price_of_Apple = int(input("What is the price of an apple? "))
# maximum_apples = int(Amount_money / Price_of_Apple)
# Remaining_money = int(Amount_money - (maximum_apples * Price_of_Apple))
# print(f"You can buy {maximum_apples} apples and your change is {Remaining_money} pesos.")

# Task
# Redo the Assignment 2.3 and put fuction in it

def get_money():
    money = int(input("Pare magkano pera mo? "))
    return money


def get_apple_price():
    apple_price = int(float(input("Suki! tumawad ka sa presyo ng mansanas? ")))
    return apple_price


def get_maximum_apples(payment_customer, price_of_apple):
    maximum_apples = int(payment_customer / price_of_apple)
    return maximum_apples


def get_remaining_money(payment_customer, max_apple, price_of_apple):
    remaining_money = int(payment_customer - (max_apple * price_of_apple))
    return remaining_money


def display_output(max_apple, change):
    print(f"You can buy {max_apple} apples and your change is {change} pesos.")


# Steps
# Ask the money of your customer
payment_customer = get_money()
# Give the price of the apples
price_of_apple = get_apple_price()
# Get the maximum apples that consumer can buy
max_apple = get_maximum_apples(payment_customer, price_of_apple)
# Compute the remaining money
change = get_remaining_money(payment_customer, max_apple, price_of_apple)
# Display the maximum apple that consumer can buy and the remaininf money
display_output(max_apple, change)

# Sunday morning what a great day. =)
