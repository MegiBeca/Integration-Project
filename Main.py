'''
author = Megi Beca
'''

import Sales
import Formatter
import Pay
import time

end = True
while end:
    request = input(
        "Pick a letter:\nA = Identify thhe persecnt yoy saved.\nB = Identify what level of savings you got.\n"
        "C = Identify how much you owe or how much change you are owed.\nD = Format a receipt.\nE = Calculate how "
        "much of a bonus you reseaved this year.\nF = Calculate your yearly income.\n").upper()
    if request == "A":
        Sales.identifying_percent_off()
    elif request == "B":
        Sales.identifying_savings()
    elif request == "C":
        Sales.change()
    elif request == "D":
        Formatter.formatting_receipts()
    elif request == "E":
        Pay.bonuses()
    elif request == "F":
        Pay.income()
    time.sleep(5)
