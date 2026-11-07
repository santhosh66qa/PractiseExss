## List in python are just like arrays in other programmming language

##[]-- list is reperesented as this--- list of multiple data types can be holded in a single var--list
##-- collection of differennt data types---list/array--- can hold mutiple data's/data types

fruits = ["apple", "banana", "cherry"]
print(fruits)
print(fruits[0])
print(fruits[1])
print(fruits[2])

########################################

print("###########################################")
print()

fruits_animals_numbers = ["apple", "banana", "cherry", "dog", "Lion", 4, 5.2]
print(fruits_animals_numbers)
print(fruits_animals_numbers[0])
print(fruits_animals_numbers[1])
print(fruits_animals_numbers[2])
print(fruits_animals_numbers[3])
print(fruits_animals_numbers[4])
print(fruits_animals_numbers[5])
print(fruits_animals_numbers[6])
print(type(fruits_animals_numbers[2]))

########################################

print("###########################################")
print()

fruits_animals_numbers = ["apple", "banana", "cherry", "dog", "Lion", 4, 5.2]
print(type(fruits_animals_numbers))

#####

print("###########################################")
print()

numbers = [1,2,3,4] 
print(numbers[1] + numbers[3])

########################################

print("###########################################")
print()

fruits_animals_numbers = ["apple", "banana", "cherry", "dog", "Lion", 4, 5.2]
print(fruits_animals_numbers[0] + fruits_animals_numbers[2])


########################################

## Impt: List index out of range exception:

print("###########################################")
print()

fruits_animals_numbers = ["apple", "banana", "cherry", "dog", "Lion", 4, 5.2]
#print(fruits_animals_numbers[0] + fruits_animals_numbers[7])

##
########################################

## Impt: List index out of range exception:

print("####################### Nested List ################")
print()

fruits_animals_numbers = ["apple", "banana", "cherry", "dog", "Lion", ["Santhosh", "Hi"]]
print(fruits_animals_numbers[5])



##

## 1st that index[], then in that its in which index[]
##2d list/array

print()

fruits_animals_numbers = ["apple", "banana", "cherry", "dog", "Lion", ["Santhosh", "Hi"]]
print(fruits_animals_numbers[5][0])

##

## 1st that index[], then in that its in which index[]
##2d list/array

print()

fruits_animals_numbers = ["apple", "banana", "cherry", "dog", "Lion", ["Santhosh", "Hi"]]
print(fruits_animals_numbers[5][1])

##


print()

fruits_animals_numbers = ["apple", "banana", "cherry", "dog", "Lion", ["Santhosh", "Hi"]]
print(fruits_animals_numbers[0] + fruits_animals_numbers[5][1])
print(fruits_animals_numbers[0] , fruits_animals_numbers[5][1])