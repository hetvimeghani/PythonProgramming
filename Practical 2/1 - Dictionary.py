#D21CE171 - Hetvi Meghani

#Practical - 1
# Write a Python script to check whether a given key already exists in a dictionary.

#Declaration
A = {1:20,2:20,3:30}
b = 1
#Logic
if b in A:
    print("Key is Present")
else:
    print("Key is not present")

#--------------------------------------------------------------------------------------------------------

#Practical - 2
# Write a Python script to merge two Python dictionaries.

#Declaration 
d1 = {1: 100, 2: 200}
d2 = {3: 300, 4: 200}
#Logic
d1.update(d2)
#Print
print(d1)

#--------------------------------------------------------------------------------------------------------

#Practical - 3
# Write a Python program to sum all the items in a dictionary.4

#Declaration
a = {1:5,2:20,3:30}
#Print
print(sum(a.values()))

#--------------------------------------------------------------------------------------------------------

#Practical - 4
# Write a Python script to add a key to a dictionary.
# Sample Dictionary : {0: 10, 1: 20}
# Expected Result : {0: 10, 1: 20, 2: 30}

#Declaration
a = {0:10,1:20}
#Add element in dictionary
a.update({2:30})
#print
print(a)

#--------------------------------------------------------------------------------------------------------

#Practical - 5
# Write a Python script to concatenate the following dictionaries to create a new one.
# Sample Dictionary :
# dic1={1:10, 2:20}
# dic2={3:30, 4:40}
# dic3={5:50,6:60}
# Expected Result : {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}

#Declaration
dic1 = {1:10,2:20}
dic2 = {3:30,4:40}
dic3 = {5:50,6:60}
#Merge dictionaries
dic1.update(dic2)
dic1.update(dic3)
#Print
print(dic1)