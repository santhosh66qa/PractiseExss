
## type should be int and return should be int ->
##putting restrictions-- but not fully,  type restrictions

def add_numbers(a: int, b: int) -> int:
    return a + b

result =add_numbers(10, 20)
print("The sum of the two numbers is:", result)
print("UPDATED")


###########################
##string concatenation

print("###############################################")
print()

a = "Santhosh"
b= "sam"

print(a+b)  ##string concatenation  

#####################################

print("###############################################")
print()

##impt:  passing 1 complete function as an argument to another function:

def add(a,b):
    return a+b

def sub(a,b):
    return a-b

sum = add(2, 4)
difference = sub(sum, 2)

print(difference)

#####################################

print("###############################################")
print()

##impt:  

def add(a,b):
    return a+b

def sub(a,b):
    return a-b

difference = sub(add(2, 4), 2)

print(difference)

#####################################

print("###############################################without any variables###########")
print()

##impt:  

def add(a,b):
    return a+b

def sub(a,b):
    return a-b

print(sub(add(2, 4), 2))

#####################################
# Type function-- to what type it is

print("#########################################################")
print()

print(type(1))

#####################################
# Type function-- to what type it is  ## by default it is string type --- input function

print("##################################################")
print()

#a = input("Enter affssgg")
#print(type(a))

#####################################
# Type function-- to what type it is  -- to restrict the type of data int ()

print("##################################################")
# print()

# a = int(input("Enter :"))
# print(type(a))

#####################################
# Type function-- to what type it is  -- to restrict the type of data int ()

print("##################################################")
print()

print(type("☺️"))

