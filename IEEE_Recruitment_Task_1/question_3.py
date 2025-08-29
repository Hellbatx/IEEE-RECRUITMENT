#Numpy arrays
import numpy as np                                                               #importing the numpy library

rng= np.random.default_rng()                                                     #makes a random number generator

array= rng.integers(low=1,high=101,size=(5,5))            # generates 10 random integers between 1 and 100(upper limit is exclusive) in a 5,5 matrix            

print(array,"\n")                                #prints the 5,5 matrix


print(f"The minimum of all values in the array is: ",np.min(array),"\n")       #prints the minimum value
print(f"The maximum of all values in the array is: ",np.max(array),"\n")       #prints the maximum value
print(f"The mean of all values in the array is: ",np.mean(array),"\n")         #prints the mean value

normalized_array= (array - np.min(array)) / (np.max(array) - np.min(array))    #normalizes the array values between 0 and 1

print("The normalized array is: ", normalized_array, "\n")                    #prints the normalized array

flattened_array= normalized_array.flatten()                                   #flattens the normalized array into a 1D array

print("THe flattened array (now one dimensional) is: ", flattened_array,"\n")          #prints flattened array 

sorted_1D_array= np.sort(flattened_array)                                       #sorts the array values 

print("The sorted array is: ", sorted_1D_array)                                 #prints the sorted 1D array

