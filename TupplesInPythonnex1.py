## tuples -- a kind of array-- But its immutable-- once assigned
##it cant be changed-- Ex: addhar No, pan No.. once its assigned u cant change
##--its Immutabble--tupples
## same way to declare---instead of list [],, here we are using ()-- like functions

##same indexing-- aacessing index also same--with-- []

birthday= (12, "August", 1997)

print(birthday)
print(birthday[0])
print(birthday[1])
print(birthday[2])

print(len(birthday))

###########

birthday= (12, "August", 1997)

print(birthday)
print(birthday[0])
print(birthday[1])
print(birthday[2])

day, month, year = birthday

print(f"Born in {month}/{day}/{year}")

###########

a, b, c = 1, 2, "Hihello"

print(a, b, c)
############################

###########
## -- in case of an array we can change it
birthday= [12, "August", 1997]


birthday[0] = 16
print()
print(birthday)
###########
## -- in case Tupples we can't change it
birthday= (12, "August", 1997)


#birthday[0] = 16
##-- u cant change it(value)-- ERROR: TypeError: 'tuple' object does not support item assignment
#print()
#print(birthday) --

#########

##In tupples u cannot append as well-- append function wont support in tupples

route = ("bengaluru", "Mysuru")

#route.append("Bellary")
## ERROR : AttributeError: 'tuple' object has no attribute 'append'. Did you mean to use a 'list' object?

######################

route = ("bengaluru", "Mysuru")

route = route + ("Chikkbalapura",)
print(route)

##-- ("Chikkbalapura",) =- its completely New tupple
##-- + if u use, its not modifying the tupple-- its just adding 2 diff tupples
##-- without comma it wont work

##

######################

route = ("bengaluru", "Mysuru")

route = ("Chikkbalapura",) + route
print(route)

######################

route = ("bengaluru", "Mysuru")

route =  route + ("Chikkbalapura", "ooty")
print(route)
######################

route = ("bengaluru", "Mandya" ,"Mysuru")

stops = list(route)
#stops = list(route) -- this is correct syntax

print(type(route))
print(type(stops))
stops.insert(1, "Narisipura")
stops.remove("Mysuru")
stops[0] = "Majestic"
print(route)
print(stops)
## list in built function-- to covert into list --from tupples
## u can manipulate-- or modify after u converting into list from tupples


## again to convert back to tupple from list
route = tuple(stops)
#tuple(stops) - correct syntax
print(route)

#################

## most of the cases-- List only we will be using
## addhar no-- in list anyone can change-- it wont throw any error
## once assigned should not be editable-- then go for Tupple..

##########

#Realtime use case:

aadhar_details = ["Santhosh", "12/06/1998", "Bengaluru", (12345,)]
aadhar_details[3][0] = 2666
print(aadhar_details)
##TypeError: 'tuple' object does not support item assignment
##(12345,) -- with comma--- addhar number-- as tupple

## type safety-- tupple -- now cant change aadhra number.. other details
##can be changed