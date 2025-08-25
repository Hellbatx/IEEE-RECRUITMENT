#Task 1: Building an inverted star pattern.

n= int(input("Enter the number of rows: "))

for i in range(0,n-1):

    spaces= " "
    spaces+= i
    stars= "*"
    stars+= n-i
    
    print(spaces+stars)
    