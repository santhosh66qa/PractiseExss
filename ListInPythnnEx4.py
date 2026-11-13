
##pop -- ex: in a buscuit packet or container-- if u pop-- then 1st buiscuit will comes out
##basically last index/lastly inserted will comes out first..
## in python-- pop removes the last element

shopping = ["Rice", "Dal"]

print(shopping)

remove_item = shopping.pop()

print(remove_item)
print(shopping)

remove_item = shopping.pop()

print(remove_item)
print(shopping)

###

print("####################")
print()
list_numbers= [29, 28, 35, 66]
list_numbers.pop(2)  ## based on index it will pop
print("Pop list numbers")
print(list_numbers)

###-- List is mutable-- means we can add/delete we can change/modify---it will allow me
##to change or modify

##- Immutable-- means which we cannot change once assigned-- real time ex: AAdhar number-- we cant change
##- once aadhar num is created --it remains permenantly, But phone number, address can be changed(these details
## are mutable)
## voter id, pan number-- Immutable

##
#remove:
print("#########################")
print()
numbers = [1, 30, 50, 66, 77]
numbers.remove(30)
print(numbers)

##############

marks = [22, 33, 43, 55]
print("******** Inbuilt functions *************")
print(sum(marks), min(marks), max(marks))

route = ("bengaluru", "Mysuru")




##############

marks = [22, 32, 43, 55, 55, 66, 32]
print("******** To find how many time its repeated *************")
print(marks.count(32))
print(marks.count(21))
print(marks.count(0))

##############

marks = ["Hi", "Hello", "Hi"]
print("******** To find how many time its repeated *************")
print(marks.count("Hi"))
print(marks.count("Hello"))

##############

marks = [123, 34, 65, 45, 1887, 100]
print("******** For sorting elements, only for that particular Instance *************")
print(sorted(marks))  ## only at this line it will sort next line if u try to print entire array it wont be sorted
print(marks)
##only for numbers , can use for strings-- sorted
#######


##########

marks = [123, 34, 65, 45, 1887, 100]
print("******** For sorting elements reversly means big to small *************")
print()
marks.sort(reverse=True)
print(marks)
##########

marks = ["g", "x", "c"]
print("******** For sorting elements reversly means big to small *************")
print()
marks.sort()
print(marks)
marks.sort(reverse=True)
print(marks)
##########

marks = ["ghrer", "abfrs", "daaa"]
print("******** For sorting elements reversly means big to small *************")
print()
marks.sort()
print(marks)
marks.sort(reverse=True)
print(marks)
print("#######################")
marks.reverse()
print(marks)


