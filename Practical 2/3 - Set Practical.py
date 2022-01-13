# Set Practical - 1
# Write a Python program to add member(s) in a set and clear a set

set = {10,20,30,40}
set.add(50)
print(set)
set.clear()
print(set)

################# Created By Manav Dadhaniya - D21CE163 #####################

# Set Practical - 2
# Write a Python program to remove an item from a set if it is present in the set.

set = {10,20,30,40}
x=50
c=0
for y in set:
    if x==y:
        print('X is available in set');
        c=1
if c==0:
    print('X is not available in set')

################# Created By Manav Dadhaniya - D21CE163 #####################

# Set Practical - 3
# Write a Python program to create an intersection, Union, difference of sets.

set1 = {0, 2, 4, 6, 8}
set2 = {1, 2, 3, 4, 5}
print("Union :", set1 | set2)
print("Intersection :", set1 & set2)
print("Difference :", set1 - set2)

################# Created By Manav Dadhaniya - D21CE163 #####################

# Set Practical - 4
# Write a Python program to find maximum and the minimum value in a set.

set = {10,20,30,40,50}
print('Manimum Value of Set = ', min(set))
print('Maximum Value of Set = ', max(set))

################# Created By Manav Dadhaniya - D21CE163 #####################

# Set Practical - 5
# Write a Python program to find the most common elements and their counts from list, tuple, dictionary.

# list
list=['Cars', 'Cars', 'Flowers', 'Cars','Cats']
# tuple
tuple = (1,2,3,4,5,1,3,1,1)
# Dictionary
Car = {
     "Brand":"Toyota",
     "Model":"Camry",
     "Year":"2021",
     "Brand":"Toyota"
 }
from collections import Counter
l = Counter(list)
l.most_common(1)

t = Counter(tuple)
t.most_common(1)

d = Counter(Car)
d.most_common(1)
print ("",l.most_common(1))
print ("",t.most_common(1))
print ("",d.most_common(1))

################# Created By Manav Dadhaniya - D21CE163 #####################