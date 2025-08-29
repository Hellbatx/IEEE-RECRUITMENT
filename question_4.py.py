import numpy as np                                                               #importing the numpy library

rng= np.random.default_rng()                                                     #makes a random number generator

array= rng.integers(low=1,high=101,size=(5,5))

print(array,"\n")                                #prints 10 random integers between 1 and 100(upper limit is exclusive) in a 5,5 matrix

mid_array= array[1:4,1:4]                        #slices the 5,5 array to extract only 3,3. range is 1:4 because upper limit is excluded.

print("New 3,3 array is: \n",mid_array,"\n")                                #prints the 3,3 array.

first_row= mid_array[0,:]                       #extracts the first row the array. 0 means 1st row(index) and : means all the columns.

last_column= mid_array[:,2]                     #extracts the last column of the array. : means all the rows and 2 means 3rd column.

dot_product= np.dot(first_row,last_column)      #finds the dot product of the first row and last column.

print("First row: ",first_row,"\n")                  #prints the first row

print("Last column: ",last_column,"\n")                  #prints the last column

print("Dot product of first row and last column is:  ",dot_product,"\n")    #prints the dot product of the first row and last column
