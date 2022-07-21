#Creating a Simple Caculator
print("For Addition Press a")
print("For Substraction Press b")
print("For Multiplication Press c")
print("For Division Press d")
input1 = input("What You Want to Do: ")

#Function for Addition
def addition(a,b):
	sum1 = a+b
	print("Sum of Two number is: ",sum1)
	return 

#Function for Substraction
def substraction(a,b):
	if a>b:
		sub = a-b 
	else:
		sub = b-a 
	print("Substraction of Two numbers is: ",sub)
	return

#Function for Multiplication
def multiplication(a,b):
	mult = a*b 
	print("Multiplication of Two Number is: ",mult)
	return 

#Function for Division
def division(a,b):
	if a>b:
		div = a/b 
	else:
		div = b/a
	print("Division of Two Number is: ",div)
	return

#If User Input wrong then this message will show
def wrong():
	print("Wrong Input")
	print("Try Again")
	return

#Taking Two number as input from user
input2 = int(input('Enter First Number: '))
input3 = int(input('Enter Second Number: '))

#Calling our Function on the basis of Condition
if input1 == 'a':
	addition(input2,input3)
elif input1 == 'b':
	substraction(input2,input3)
elif input1 == 'c':
	multiplication(input2,input3)
elif input1 == 'd':
	division(input2,input3)
else:
	wrong()
	exit()


print("Thank you")
