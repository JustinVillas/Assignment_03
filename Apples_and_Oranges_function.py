# Task
# Redo Assigntment no. 02 and put function with it

def get_number_of_apples():
    no_apples = int(input("Suki! How many apples do you want to buy? "))
    return no_apples


def get_number_of_oranges():
    no_oranges = int(input("Suki! How many oranges do you want to buy? "))
    return no_oranges


def get_total_amount(apples, oranges):
    return 20 * apples + 25 * oranges


def display_output(payment):
    print(f"The total amount is {payment}.")


# steps
# Ask the number of apples that consumers want to buy
apples = get_number_of_apples()
# Ask the number of oranges that consumers want to buy
oranges = get_number_of_oranges()
# Compute the total amount
payment = get_total_amount(apples, oranges)
# Display the total amount
display_output(payment)

# doing great Justin =)
