low = 0
high = 100

print "Please think of a number between 0 and 100!"


while True:
    mid = abs((low+high)/2)
    print "Is your secrete number ", mid, "?"
    user = raw_input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly. ")

    if user == "h":
        high = mid
    elif user == "l":
        low = mid
    elif user == "c":
        print "Game over. Your secret number was: ", mid
        break
    else:
        print "Please check you input"
