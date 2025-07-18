#1A:- all () function retrurns true when applied to empty tuple

#2Q:_create a tuple
tuple1 = (1,2,3)
print(type(tuple1))

#3Q:-find length of tuple
tuple1 = (1,2,3)
print(len(tuple1))

#4a:- Tuples are immutable, denoted by () coma separated elements/datatypes

##Coding excercises:-Create a tuple containing your name,favourate color and age
my_tuple =  {'shree', '25', 'white _color'}
print(my_tuple)

#Access the tuple 
# Corrected: Use a tuple instead of a set
days_of_week = ('sunday','monday','tuesday','wednesday','thursday','friday','saturday')

print(days_of_week)

for i in range(len(days_of_week)):
    if i == 2:
        print(f'Holiday is on {days_of_week[i]}')
        
        
# tuple concatenation:
list1 = []
list2 = []

for i in range(1, 6):
    for j in range(1, 5):
        if i % 2 == 0 and i not in list1:
            list1.append(i)
            print(f'Even number added: {i}')
        elif j % 2 != 0 and j not in list2:
            list2.append(j)
            print(f'Odd number added: {j}')

a = tuple(list1)
b = tuple(list2)

print("Tuple a (even numbers):", a)
print("Tuple b (odd numbers):", b)

print("Type of a:", type(a))
print("Type of b:", type(b))

##6Q :- generate a bill for supermarket  purchase


items = [("Apple", 99), ("Banana", 99), ("Milk", 49)]
total = 0
print("item\t Price")
print("-"*25)
for i,j in items:
    print(f"{i}\t{j}")
    total+=j
    print("-"*25)
print(f"Total\t{total}")


    

