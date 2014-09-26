## Example of computation without and with functional abstraction

## Without functional abstraction

x = float(raw_input('Enter a number: '))
p = int(raw_input('Enter an integer power: '))
##
result = 1
##


## With functional abstraction

def iterativePower(x,p):
    result = 1
    for turn in range(p):
        print ('iteration: ' + str(turn) + ' current result: ' + str(result))
        result = result * x
    return result

print iterativePower(x,p)

        

