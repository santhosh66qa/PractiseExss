## 2D Array/List-- means array whithin another array-- [] 1 array, [] 2nd arry,etc..

marks = [[11,22], [23, 56], [53, 77]]

print(marks)
print(marks[0])
print(marks[0][1])
print(marks[1][1])

##-- 1st 0, 1, 2 --indexes --outer
##--then u need to traverse--ex: to get 56  1st think of
##[23, 56]--index--which is 1 -- so directly start with marks[1]
##then again think --56 is in 1 index--i.e., 0, 1(23, 56)

#################################################################

##-- 3D array-- 3 Dimensional Array

marks = [[11, [13, 16]], [23, 56], [53, 77]]

print(marks[0][1][1])

###-- 1st 0, 1, 2 --indexes --outer-- [11, [13, 16]] --this is 0
   ## [23, 56] -- this is 1
   ## [53, 77] -- this is 2
##--then u need to traverse--ex: to get 16  1st think of
##[11, [13, 16]]--index--which is 0 -- so start with marks[0]
##the again to traverse to 16-- 0 1 --2 indexes-- 11 is 0 and [13, 16] is at 1
## so now [0][1]
##again-- [13, 16]--- 0(13) , 1(16) == so now-- [0][1][1]

####################################################################################

###-- in AI-- vectors--- 3 dimentional Vectors--- these also represented like
##this 3 d arrdy only.. one of the way to reperesent is 3d array




