from org.transcrypt.stubs.browser import *

def sortnumber1():
	'''	This function is used in Exercise 1.
		The function is called when the sort button is clicked.

		You need to do the following:
		- get the list of numbers from the "generate" HTML id, use document.getElementById(id).innerHTML
		- create a list of integers from the string of numbers
		- call your sort function, either bubble sort or insertion sort
		- create a string of the sorted numbers and store it in array_str
	'''
	# The following line get the value of the text input called "numbers"
	value1 = document.getElementsByName("num1")[0].value
	value2 = document.getElementsByName("num2")[0].value
	value3 = document.getElementsByName("num3")[0].value

	# Throw alert and stop if nothing in the text input
	if value1 == "":
		window.alert("Your textbox is empty")
		return

	# Your code should start from here
	# store the final string to the variable array_str
	b0 = 5
	b1 = 2
	numbers = int(value1) + int(value2) + int(value3)

	document.getElementById("sorted").innerHTML = str(numbers)


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
	value = document.getElementsByName("numbers")[0].value

	# Throw alert and stop if nothing in the text input
	if value == "":
		window.alert("Your textbox is empty")
		return

	# Your code should start from here
	# store the final string to the variable array_str
	b0 = 5
	b1 = 2
	numbers = b0 + b1*int(value)

	document.getElementById("sorted").innerHTML = str(numbers)
