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
8. Age difference - completed
9. area of a triangle - completed
10. hours left from now
11. days left from today
12. temperature calculator

blog: 
how to get current date and time in python
how to get current date and time in ruby
how to get current date and time in javascript
find time left(difference) between two time values in python
find time left(difference) between two time values in ruby


'''


import math
import datetime
from datetime import date 


current_year = date.today().year

t1 = datetime.strftime('01:12','%H:%M')
t2 = datetime.strftime('18:59','%H:%M')
print t1
print t2 - t1


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
  
def age_diff(year1, year2):
  return (year1 - year2)
  
def area_triangle(base,length):
  return ((base*length)/2)






print "------------%d----------" %date.today().year 

print "1) Simple Interest"
print "2) Compound interest"
print "3) Addition"
print "4) Subtraction"
print "5) Multiplication"
print "6) Divide"
print "7) Age Calculator"
print "8) Age Difference"
print "9) Area of a triangle"

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
elif 
