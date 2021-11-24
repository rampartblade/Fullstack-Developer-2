#Contoh 1
def changeme(mylist):
    '''This changes a passed list into this function'''
    mylist = mylist+[1,2,3,4]
    print("\nValues inside the function : ", mylist)
    return mylist

mylist = [10, 20, 30]
print("\n Values inside outside the function - before : ", mylist)
mylist = changeme(mylist)
print("\n Values inside outside the function - after : ", mylist)

#Contoh 2
def person_car(total_data, **kwargs):
    '''create function to print who owns a car'''
    print('Total data', total_data)
    for key,value in kwargs.items():
        print('Person : ', key)
        print('Car    : ',value)
        print('')

person_car(3,jimmy='Chevrolet', frank='Ford', tina='Honda')
person_car(3)

#contoh 3
def sum(arg1, arg2):
    return arg1 + arg2

total = sum(10,20)
print('result function : ',total)

#contoh 4
# Function definition is here
sum = lambda arg1, arg2: arg1 + arg2

# That lambda function will be equal to :
# def sum(arg1, arg2):
#     return arg1+arg2

# Now you can call sum as a function
print("Value of total : ", sum( 10, 20 ))
print("Value of total : ", sum( 20, 20 ))

#contoh 5
total = 0

def sum(arg1, arg2):
    return arg1+arg2

print("Outside the function global total - before", total)
total = sum(10,20)
print("Outside the function global total - after", total)

#contoh 6
# Example of docstring in a function

def sum_number(num1, num2):
  '''
  This function is used to sum of 2 variables.
  :param num1: Input number 1 | int or float
  :param num2: Input number 2 | int or float
  
  :return: num3: Sum of number | int or float
  '''

  num3 = num1 + num2
  return num3

print(sum_number.__doc__)
print(__doc__)

### Module ###

#cara 1 import person
""" import person
print(person.name)
 """
#cara 2 import person
import sys
""" sys.path.append(r'/Users/ardhiraka/Desktop/H8Py')
print(sys.path) """
#import mod
#mod.__file__

