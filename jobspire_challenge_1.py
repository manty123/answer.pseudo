import random

def print_name_number(name):
    #Generate a random number between 6 to 15
    rand_number = random.randrange(6, 15)
	#Print the output
    print(name + ' ' + str(rand_number))

#Take input from user 
name = input('Enter any input: ')
#Call the function to print the output
print_name_number(name)

