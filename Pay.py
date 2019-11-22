'''
Functions related to salaries
author = Megi Beca
'''


# Calculated bonus depending on amount of sales and formats it
# credit to HackerRank.com rank for prompt
def bonuses():
    sales = int(input("Enter the amount of sales you've had this year"))
    if sales >= 100000:
        bonus = 10000
    elif sales >= 75000:
        bonus = 5000
    elif sales >= 50000:
        bonus = 2500
    elif sales >= 25000:
        bonus = 1000
    else:
        bonus = 0
    print("Your bonus is ${:,.2f}".format(bonus))


# Calculates the annual income
def income():
    hours = int(input("How many hour a week do you work?"))
    hourly = int(input("How much do you make per hour?"))
    sum1 = int(hourly * hours * (4 * 13))
    print("You early approximately", sum1, "per yeaar")
