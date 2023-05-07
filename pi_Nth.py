#Find pi to the Nth Digit

import math

#Creating a base input for the user
user_answer = 'yes'
user = input("Would you like to round pi the Nth digit: ")

#Set a condition if the user doesnt answer
while user.lower() != user_answer: 
   user = input("Would you like to round pi the Nth digit: ")

if user.lower() == 'no':
    print('Hope you have a great day')

elif user.lower() == 'yes':
  #Setting variable input for the user to ask 
  pi = int(input("How many spaces, of pi do you want to see?: "))

#Creating a codition for if variable is greater than set number
while pi > 50:
	print("The number you type was too high. Please type something lower than 50")
	precision = int(raw_input("How many spaces, of pi do you want to see?: "))
else:
	print('%.*f' % (pi, math.pi))