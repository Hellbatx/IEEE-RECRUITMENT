# Finding the intersection of two lists which have common elements. 

import numpy as np

List_1= [3, 4, 5, 1, 4, 6, 1, 7, 7]
List_2= [5, 8, 2, 9, 9, 4, 6, 3]

# We are going to use set() becuase a set can only have unique elements.

Set_1= set(List_1)                # here we convert list to set to remove any repeated elements.
Set_2= set(List_2)

intersection= np.array(list(Set_1 & Set_2))    #here we find the common elements of both sets using & operator, and convert it into a list.

print("List 1 is: ", List_1,"\n")
print("List 2 is: ", List_2,"\n")
print("intersection of lists is: ", intersection)
