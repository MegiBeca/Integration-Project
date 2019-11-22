'''
data get sent here to be formatted
author = Megi Beca
'''
import locale

locale.setlocale(locale.LC_ALL, '')


# Receipt formatter
def formatting_receipts():
    user_input = True
    list = []
    list2 = []
    sum = 0
    while user_input:
        item = input("Enter an item:")
        price = float(input("Enter the price:"))
        end = input("Enter 'x' if you're done")
        list.append(item)
        list2.append(price)
        sum += price
        if end == "x" or end == "X":
            user_input = False
    print("Amount          Tax          Sum          Item")
    for x in range(len(list)):
        tax = float(list2[x] * 0.075)
        tax_sum = list2[x] + tax
        print(locale.currency(list2[x]), "        ", locale.currency(tax), "        ", locale.currency(tax_sum),
              "       ", list[x])
    print("Total:    ", sum)


'{:f}'.format(3.141592653589793)
