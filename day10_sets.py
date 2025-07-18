
#1Q:-what is the output of following code?
my_set = {1,2,3,4,5}
print(len(my_set))

#2Q:- which method is used to add an element  to sets ?
#Ans:- add method is used 
set_1 ={1,2,3,4}
set_1.add(6)
print(set_1)

#3Q and 5Q:-which method is used to find the common elements in both the sets? Task1 set intersection?
sett_1 = {1,2,3,4,5}
sett_2 ={4,5,6,7,8}
sett3 = sett_1.intersection(sett_2)
print(f'the common elements in both the sets are ,{sett3}')

#4Q.Ans:Sets are mutable datatypes.

#6Q:- Find the union of both the sets?
sett_1 = {1,2,3,4,5}
sett_2 ={4,5,6,7,8}
set_3 = sett_1.union(sett_2 )
print(set_3)


#7Q:- find the difference between two sets?
sett_1 = {1,2,3,4,5}
sett_2 ={4,5,6,7,8}
set_difference = sett_1.difference(sett_2)

print(f'the difference between sett1 nad sett2 is:,{set_difference}' )

#8Q:- check the element 3 in set?
my_set ={1,2,3,4,5}
if 3 in my_set:
   print(my_set)
   
#9,10,11,12Q:- create frozen set  perform  union, intersection, difference and symmetric difference in frozen set

my_set ={1,2,3,4,5}
frozen_set1 = frozenset(my_set)
print(frozen_set1)

my_set2= {4,5,6,7,8,9}
frozen_set2 = frozenset(my_set2)
print(frozen_set2)

print(f'frozenset union',frozen_set1.union(frozen_set2))
print(f'frozenset intersection',frozen_set1.intersection(frozen_set2))
print(f'frozenset difference',frozen_set1.difference(frozen_set2))
print(f'frozenset symmetric difference',frozen_set1.symmetric_difference(frozen_set2))
