#star pattern.

n= int(input("Enter the number of rows: "))            # asking for the user input

for i in range(1,n+1):                                 #for loop going from 1 row to n rows (n+1 is excluded).

    spaces= " " * (n-i)                                # spaces progressively decrease
    
    stars= "*" * i                                     # stars progressively increase
    
    print(spaces+stars)                                # printing the final pattern
    
    