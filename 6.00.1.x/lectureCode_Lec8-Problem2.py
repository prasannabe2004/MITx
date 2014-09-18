def FancyDivide(numbers,index):
    try:
        denom = numbers[index]
        for i in range(len(numbers)):
            numbers[i] /= denom
    except IndexError, e:
        print "-1"
    else:
        print "1"
    finally:
        print "0"

#FancyDivide([0, 2, 4], 1)
#FancyDivide([0, 2, 4], 4)
FancyDivide([0, 2, 4], 0)

def FancyDivide2(numbers, index):
    try:
        denom = numbers[index]
        for i in range(len(numbers)):
            numbers[i] /= denom
    except IndexError, e:
        FancyDivide2(numbers, len(numbers) - 1)
    except ZeroDivisionError, e:
        print "-2"
    else:
        print "1"
    finally:
        print "0"

#FancyDivide2([0, 2, 4], 1)
#FancyDivide2([0, 2, 4], 4)
#FancyDivide2([0, 2, 4], 0)

def FancyDivide3(numbers, index):
    try:
        try:
            denom = numbers[index]
            for i in range(len(numbers)):
                numbers[i] /= denom
        except IndexError, e:
            FancyDivide3(numbers, len(numbers) - 1)
        else:
            print "1"
        finally:
            print "0"
    except ZeroDivisionError, e:
        print "-2"

#FancyDivide3([0, 2, 4], 1)
#FancyDivide3([0, 2, 4], 4)
#FancyDivide3([0, 2, 4], 0)

def FancyDivide4(list_of_numbers, index):
    try:
        try:
            raise Exception("0")
        finally:
            denom = list_of_numbers[index]
            for i in range(len(list_of_numbers)):
                list_of_numbers[i] /= denom
    except Exception, e:
        print e

FancyDivide4([0, 2, 4], 0)


def FancyDivide5(list_of_numbers, index):
    try:
        try:
            denom = list_of_numbers[index]
            for i in range(len(list_of_numbers)):
                list_of_numbers[i] /= denom
        finally:
            raise Exception("0")
    except Exception, e:
        print e

#FancyDivide5([0, 2, 4], 0)