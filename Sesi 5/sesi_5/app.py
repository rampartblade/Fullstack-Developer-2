class Dog(): #pascalcase
    species = 'Anjing'
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def description(self):
        return f"{self.name} is {self.age} years old"

    def speak(self,sound):
        return f"{self.name} says {sound}"

miles = Dog('Miles', 4)

print(miles.name, miles.age, miles.species)
print(miles.description())
print(miles.speak("gonggong"))

### Sesi 6 ###
#1
def my_generator():
    print("Inside my generator")
    yield 'a'
    yield 'b'
    yield 'c'

my_generator()
temp = my_generator()
#print(my_generator())
print(next(temp))
print(next(temp))
print(next(temp))

#2
for char in my_generator():
  print(char)

def counter_generator(low, high):
    while low <= high:
       yield low
       low += 1

for i in counter_generator(5,10):
  print(i, end=' ')

#3
def say_hello(name):
    return f"Hello {name}"

def be_awesome(name):
    return f"Yo {name}, together we are the awesomest!"

def greet_bob(greeter_func):
    return greeter_func("Bob")

print(greet_bob(say_hello))
print(greet_bob(be_awesome))

#4
""" def parent():
    print("Printing from the parent() function")

    def first_child():
        print("Printing from the first_child() function")

    def second_child():
        print("Printing from the second_child() function")

    second_child()
    first_child()
parent() """

#5
def parent(num):
    def first_child():
        return "Hi, I am Emma"

    def second_child():
        return "Call me Liam"

    if num == 1:
        return first_child()
    else:
        return second_child()

print(parent(1))

#6
