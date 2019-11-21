'''
Functions related to paying for things
author = Megi Beca
'''


# Calculates the percent saved off an item then format's the output
def identifying_percent_off():
    original_price = float(input("Enter the original cost of the item: "))
    sale_price = float(input("Enter the sale price: "))
    percent_off = int((original_price - sale_price) / original_price * 100)
    print("Original price: $", format(original_price, ".2f"), sep="")
    print("Sale price: $", format(sale_price, ".2f"), sep="")
    print("Percent off: ", format(percent_off, "d"), "%", sep="")


# Calculates the percent saved off an item then responds with what tear the sale is in
def identifying_savings():
    is_bad = True
    while is_bad:
        try:
            original_price = int(input("Enter the original price of the item: "))
            price = int(input("Enter your price: "))
            is_bad = False
            percent_off = int((original_price - price) / original_price * 100)
            if percent_off >= 70:
                print("You got", percent_off, "percent off, you got a great deal.")
            elif percent_off >= 50:
                print("You got", percent_off, "percent off, you got a deal.")
            else:
                print("You got", percent_off, "percent off, you got an ok deal.")
        except ValueError:
            print("You did not enter a whole number.")


def change():
    user_input = True
    sum = 0
    print("Enter 'x' when you're done entering prices.")
    while user_input:
        #Get the price of the first item
        price = float(input("Enter the price of an item.\n"))
        sum += price
        if price == "x" or price == "X":
            user_input = False
    #Get the payment amount
    payment = float(input("How much did you pay?\n"))

    difference = payment - sum
    # Determine if customer still owes
    if payment < sum:
        print("You still owe ${:,.2f}".format(-difference))

    # or if change is owed
    if payment>sum:
        print("Thank you, your change is ${:,.2f}".format(difference))
    else:
        print("Thank you for shopping with us, and have a great day.")
