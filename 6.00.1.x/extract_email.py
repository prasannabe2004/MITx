#######
# Given a string, extract the email address from string
# If there is no email address, print an appropriate error message
# Other specifications:
# - assume only string contains no more than one address
# - no special characters other than @ and . will be given
# - email address will be denoted between spaces
# - for example: hello a@b this@example.where this@.is.fun will print this@example.where
#######

def IsValidEmail(str):
    index1 = str.find("@")
    index2 = str.find(".")
    print index1,index2
    if str.startswith('@') or \
    (str.count('@') > 1) or \
    str.startswith('.') or \
    (str.count('.') < 1) or \
    index1<0 or \
    index2<0 or \
    index1>index2 or \
    abs(index1-index2) <= 1:
        return False 
    else:
        return True

def main():
        userinput = raw_input("Enter the text here with valid email!!! I will find that for you:")
    	for i in userinput.split(" "):
    	   if IsValidEmail(i) != False:
    	       print i," is the email id you are looking for"
    	   else:
    	       print "No valid email Id found"

main()