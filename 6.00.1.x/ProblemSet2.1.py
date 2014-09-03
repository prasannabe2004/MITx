balance = 5000 
annualInterestRate = 0.18
monthlyPaymentRate = 0.02

TotalPaid = 0

for month in range(1, 13):   
    payment = balance * monthlyPaymentRate
    UnpaidBal = balance - payment
    
    print "Month: ", month    
    print "Minimum monthly payment: %4.2f" % payment
     
    balance = UnpaidBal + UnpaidBal*(annualInterestRate/12.0)   
    print "Unpaid balance: %4.2f" % balance 
    TotalPaid = TotalPaid + payment
    

print "Total paid: %4.2f" % TotalPaid
print "Remaining balance: %4.2f" % balance