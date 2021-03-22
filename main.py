#Mission : Identify is number is greater than or less than 10
number = int(input("Type a number :"))

if (number > 10):
  print ("The number " + str(number) +" is greater than 10.")

elif (number < 10):
  print ("The number " + str(number) + " less than 10.")

else:
  print ("The number " + str(number) + " is equal to 10.")