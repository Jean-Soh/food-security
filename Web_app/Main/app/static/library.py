from org.transcrypt.stubs.browser import *
from math import log

def function1():

	value1 = document.getElementsByName("num1")[0].value
	value2 = document.getElementsByName("num2")[0].value

	if value1 == "" or value2 == "":
		window.alert("Your textbox is empty")
		return

	b0 = 45.64998705
	b1 = 11.023
	b2 = 9.646
	x1 = int(value1)
	x2 = int(value2)
	numbers = b0 + b1*(1-log(x1)) + b2*((100-x2)**(1/2))

	document.getElementById("sorted").innerHTML = str(numbers)


def function2():

	value1 = document.getElementsByName("num1")[0].value
	value2 = document.getElementsByName("num2")[0].value
	value3 = document.getElementsByName("num3")[0].value
	value4 = document.getElementsByName("num4")[0].value

	if value1 == "" or value2 == "":
		window.alert("Your textbox is empty")
		return

	b0 = 45.64998705
	b1 = 11.023
	b2 = 9.646
	x1 = int(value1)
	x2 = int(value2)
	numbers1 = b0 + b1*(1-log(x1)) + b2*((100-x2)**(1/2))
	x1 = int(value1) + int(value3)
	x2 = int(value2) + int(value4)
	numbers2 = b0 + b1*(1-log(x1)) + b2*((100-x2)**(1/2))
	numbers = (numbers1/numbers2 - 1) * 100

	document.getElementById("sorted").innerHTML = str(numbers) + "%"
