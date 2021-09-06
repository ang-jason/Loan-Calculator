##from org.transcrypt.stubs.browser import *
import random

array = []

def gen_random_int(number, seed):

	result = None
	result=list(range(number))
	#print(result)
	
	random.seed(seed)
	random.shuffle(result)
	return result

def generate():
	global array

	number = 10
	seed = 200

	# call gen_random_int() with the given number and seed
	# store it to the global variable array
	array = None
	
	array = gen_random_int(number, seed)
	
	array_str = None
	str_comma=""
	# convert the items into one single string 
	# the number should be separated by a comma
	# and a full stop should end the string.

	array_str=str_comma.join(str(array))

	print(array_str)


	# This line is to placed the string into the HTML
	# under div section with the id called "generate"	
	##document.getElementById("generate").innerHTML = array_str

def bubble_sort(array):
    ###
    ### YOUR CODE HERE
    ###
    ##print((2*len(array))-1)
    ##for y in range((2*len(array))-1):
        ##print("y=",y)
    y=0
    while (y<(2*len(array))+1):
        for i in range(len(array)-1):

            if array[i]>array[i+1]:
                array[i], array[i+1] = array[i+1], array[i]
                #print(array[i],array[i+1])
                #print(array)

        y=y+1
        
def sortnumber1():
	'''	This function is used in Exercise 1.
		The function is called when the sort button is clicked.

		You need to do the following:
		- get the list of numbers from the global variable array and 
			copy it to a new list
		- call your sort function, either bubble sort or insertion sort
		- create a string of the sorted numbers and store it in array_str
	'''
	bubble_sort(array)

	array_str = None
	str_comma=""
	# convert the items into one single string 
	# the number should be separated by a comma
	# and a full stop should end the string.

	array_str=str_comma.join(str(array))

	print(array_str)
	
	##document.getElementById("sorted").innerHTML = array_str

def sortnumber2():
	'''	This function is used in Exercise 2.
		The function is called when the sort button is clicked.

		You need to do the following:
		- Get the numbers from a string variable "value".
		- Split the string using comma as the separator and convert them to 
			a list of numbers
		- call your sort function, either bubble sort or insertion sort
		- create a string of the sorted numbers and store it in array_str
	'''
	# The following line get the value of the text input called "numbers"
	# value = document.getElementsByName("numbers")[0].value

	value = input("Enter your value: ")

	# Throw alert and stop if nothing in the text input
	if value == "":
		window.alert("Your textbox is empty")
		return

	# Your code should start from here
	# store the final string to the variable array_str
	arr = value.split(',')
	print(arr)
	
	bubble_sort(arr)
	print(arr)


	array_str = None
	str_comma=""
	# convert the items into one single string 
	# the number should be separated by a comma
	# and a full stop should end the string.

	array_str=str_comma.join(str(arr))

	print(array_str)

	#document.getElementById("sorted").innerHTML = array_str


generate()

sortnumber1()

sortnumber2()