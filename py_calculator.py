'''
ToDo:
-------------
1. Simple interest - completed
2. Compound interest - completed
3. Addition - completed
4. Subtraction - completed
5. Multiplication - completed
6. Division - completed
7. Age calculator - completed
8. Age difference
9. area of a triangle 
10. hours left from now
11. days left from today
12. temperature calculator

'''


import math
from datetime import date 

current_year = date.today().year

def simple(capital, rate, time):
  return capital * (1 + (rate * time))

def compound(capital, rate, time):
  return capital * ((1 + rate) ** time)

def addition(num1, num2):
  return (num1+num2)

def subtract(num1, num2):
  return (num1-num2)

def multiplication(num1, num2):
  return (num1*num2)
  
def divide(num1, num2):
  return (num1/num2)
 
def age_cal(year1,current_year):
  return (current_year-year1)
 
  
print "------------%d----------" %date.today().year  
print "1) Simple Interest"
print "2) Compound interest"
print "3) Addition"
print "4) Subtraction"
print "5) Multiplication"
print "6) Divide"
print "7) Age Calculator"

selection = raw_input("> ").lower()

if selection in ['1', 'simple interest']:
	capital = float(raw_input("Capital: "))
	rate = float(raw_input("Interest rate: ")) / 100
	time = float(raw_input("Time (years): "))
	print simple(capital, rate, time)
elif selection in ['2', 'compound interest']:
	capital = float(raw_input("Capital: "))
	rate = float(raw_input("Interest rate: ")) / 100
	time = float(raw_input("Time (years): "))
	print compound(capital, rate, time)
elif selection in ['3', 'addition']:
	num1 = float(raw_input("first number: "))
	num2 = float(raw_input("second number: "))
	print addition(num1,num2)
elif selection in ['4', 'subtraction']:
	num1 = float(raw_input("first number: "))
	num2 = float(raw_input("second number: "))
	print subtract(num1,num2)
elif selection in ['5','multiplication']:
	num1 = float(raw_input("first number: "))	
	num2 = float(raw_input("second number: "))
	print multiplication(num1,num2)
elif selection in ['6', 'divide']:
	num1 = float(raw_input("first number: "))	
	num2 = float(raw_input("second number: "))
	print divide(num1,num2)
elif selection in ['7', 'age calculator']:
	year1 = int(raw_input("Year of birth: "))
	print age_cal(year1,current_year)
	
else:
  print "You didn't choose a valid interest type"
