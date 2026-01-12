#nested if 
n= int(input())
if n%2==0:
    if n>-1:
        print("number is postive and even")
else:
    print("number is negative even") 
#checking wheather the following number in the list is even or odd 
lst=[2,1,4,5,6,78,9,5,4,32,23,34,45]
for num in lst:
    if num%2==0:
        print("num is even")
else:
    print("num is odd")
print("program is done") 
#checking wheather the following number in the list is +ve or -ve           
lst=[2,1,-9,-3,2,3,-7]
for num in lst:
    if num >= 0:
        print(num, "is positive")
    else:
        print(num, "is negative")
print("program is done")

# printing odd numbers between the 1 to 20
for num in range(1,20,2):
    print(num,"-")

            
