# Write your code here!
print('Hello from my file!')
# Declare variables: No keyword
my_name = 'Nathalie'
my_age = 37
my_boolean = True
my_undefined_value = None
# Find the length of a string
len(my_name)

CITY = 'Berlin'

# Function: 

def greet_user (name):
  greeting = 'Hello ' + name
  print(greeting)
  return greeting

greet_user('Anne')

# Objects in js is a dictionary / (HashMap) in python 
user = {
  'age': 39,
  'hobby': 'running'
}

# Array in js is a list in python

my_hobbies = ['running', 'coding', 'eating' ]

non_change_list = (1,2,3)
# compare numbers
number1 = 10
number2 = 10

if number1 > number2:
  print(str(number1) + ' is bigger than ' + str(number2))
elif number2 > number1:
  print(str(number2) + ' is bigger than ' + str(number1))
else: 
  print('Numbers are the same')  
