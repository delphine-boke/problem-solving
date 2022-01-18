# write a program that takes an input from a user and checks whether 
# its odd or even


number = int(input("enter a number: "))
#if number is divisible by 2, it's even otherwise its odd
if (number % 2) == 0:
   print("{0} is an even number".format(number))
else:
   print("{0} is an odd number".format(number))

