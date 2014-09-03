balance = 999999
annualInterestRate = 0.18

bal = balance


epsilon = 0.01
numGuesses = 0

monthlyInterestRate = (annualInterestRate) / 12
lower = balance / 12
upper = (balance * (1 + monthlyInterestRate)**12) / 12

pay = (upper + lower)/2.0

while abs(0-bal) >= epsilon:
    bal = balance
    numGuesses += 1
    for month in range(1, 13):
        UnpaidBal = bal - pay
        bal = UnpaidBal * ( 1 + (annualInterestRate/12.0) )
    
    if bal >= 0:
        lower = pay
    else:
        upper = pay
    pay = (upper + lower)/2.0

print("Lowest Payment: %4.2f" % pay)


