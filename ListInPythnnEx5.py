
## copying 1 list to another list

ration = ["Rice", "Dal"]

new_ex_Ration = ration

print(ration)
print(new_ex_Ration)

######################################

## copying 1 list to another list & then appending new element

ration = ["Rice", "Dal"]

new_ex_Ration = ration
new_ex_Ration.append("Milk")  ##it will add to both list
##beacuse of python internally points to same memory address/cell

print(ration)
print(new_ex_Ration)

######################################

## copying 1 list to another list & then appending new element & also to keep
##sperate individual copy without pointing to same memory so that it should
#not reflect changes in both lists--use copy
print("##################")
print()
ration = ["Rice", "Dal"]

#copy_ration = ration
copy_ration= ration.copy()
copy_ration.append("Milk")
print(ration)
print(new_ex_Ration)

####

##to append to a particular position or Index: use insert

print("##################")
print()
ration = ["Rice", "Dal"]


copy_ration= ration.copy()
copy_ration.insert(1, "Ghee")
print(ration)
print(copy_ration)




