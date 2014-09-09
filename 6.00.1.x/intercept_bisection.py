# Given a linear function with a positive slope that 
# intercepts the x axis between 0 and 100, find the 
# point where it intercepts without solving for x. 
# Use bisection search. 
# In other words, find 'a' such that f(a) = 0 to some certainty 'epsilon'.

low = 0
high = 100
epsilon = 0.0001
guess = 0
mid = (low+high)/2.0

def f(x):
    return -5+2.77*x

print abs(f(mid))

while (abs(f(mid)) > epsilon):
    print guess,mid
    guess = guess +1
    if f(mid) > 0:
        high = mid
    elif f(mid) < 0:
        low = mid;
    mid = (low+high)/2.0
    
print "a = ",mid, " with ",guess, " guesses ", 5/2.77

