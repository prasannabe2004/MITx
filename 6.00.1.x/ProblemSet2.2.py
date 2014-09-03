annualInterestRate = 0.18
balance = 3926

bal = balance
pay = 0
while(bal >=0):
    bal = balance
    pay = pay + 0.0001
    for month in range(1, 13):   
        UnpaidBal = bal - pay
        bal = UnpaidBal + UnpaidBal*(annualInterestRate/12.0)    


print("Lowest Payment: %4.2f" % float(pay))
    