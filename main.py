print ("Find whether the entered number is a Duck number or not")
print ("A Duck number has no zeros in front of it")
number = input("Enter any number:")
type(number)
if number[0] == '0':
    print ("Entered number is not a Duck number")
else:
    print ("Entered number is a Duck number")
