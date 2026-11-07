###

stops = ["Bengaluru", "Mysuru", "Udupi", "NajanaGudu"]


## slicing -- ":"   ,,, -1 it will take

print(stops[1:3])  ## till 2nd index only from 1 to 2 index it will print
print(stops[1:4])
print(stops[0:4])

## how many elements in present in a list/array--use length or len function
print(len(stops))

print(stops[0:4:3])  #---: 3 third slicing it will jump to 3rd element

######################################

## in operator -- to indentify particular element is there are not in a list

print("########################################")
print()

stops = ["Bengaluru", "Mysuru", "Udupi", "NajanaGudu", 5]

print("Bengaluru" in stops)
print(5 in stops)


#####################

##append function -- to add elements-- adds at the last position, insert is at a particular postition

shopping = ["Rice", "Dal"]
print(shopping)

shopping.append("Milk")
print(shopping)

shopping.insert(0, "Coffee")
print(shopping)

####################

##adding or concatenating
print("############################")
print()

shopping = ["Rice", "Dal"]

shopping = shopping + ["Milk"]

print(shopping)
shopping = ["Milk"] + shopping

print(shopping)

##########
# Overriding or replacing the value or replace

print("############################")
print()

shopping = ["Rice", "Dal"]
print(shopping)
shopping[0] = "Rasam"

print(shopping)

### To remove:

print("############################")
print()

shopping = ["Rice", "Dal"]
#shopping.remove("Rice")

print(shopping)
shopping.remove("Dal")
print(shopping)
