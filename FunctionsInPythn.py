
'''first_number = 10
second_number = 20

third_number = 50
fourth_number = 20

first_sum = first_number + second_number
second_sum = third_number + fourth_number

print(first_sum)
print(second_sum)
'''
#################################################################

## here same operation addition 2 (1 operation) but 2 times i'm calling it or doing it
##so better to use function to avoid code repetition and make it reusable-- write once & use it multiple times

##Indentation in ver imp in Python means-> adding spaces at the beginning of a line of code to define a block of code.
#Unlike Java, Python uses indentation to identify code blocks instead of curly braces {}.

#creating a function :

def add_numbers(num1, num2):
    return num1 + num2


# To call the function: -- after returning the value from the function, we can store it in a variable or print it directly.

sum = add_numbers(10, 20)
print("The sum of the two numbers is:", sum)

#######################################################################################

print("###############################################")
print()
def add_num(a, b):
    print(a+b)

add_num(20,30)

#######################################################################################

print("###############################################")
print()

def funct1(a, b, c):
    print(a+b+c)

funct1(10, 20, 30)


#######################################################################################

print("###############################################")
print()
def funct1(a, b, c):
    print(a+b)

funct1(10, 20, 30)

##meaningfull function name is important to understand what the function is doing.-- ex: add function but ur 
##implementing multiplication in it-- so better to use meaningful function name to avoid confusion.

print("###############################################")
print()

def add_num(a, b, c):
    print(a, b, c)

add_num(10, "Santhosh", 3.21)

print("###############################################")
print()

def add_num(a, b, c):
    c = "This is changed to string Now"
    print(a, b, c)

add_num(10, "Santhosh", 3.21)