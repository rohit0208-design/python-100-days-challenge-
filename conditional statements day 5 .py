#finding wheather the following number is 0 or +ve,-Ve
num=int(input("enter the number"))
if num==0:
    print("the number is zero ")
elif num>-1:
    print(" the number is postive ")
else:
    print("the number is negative ")
#finding greatest among the 3 numbers 
num1=int(input(" enter the number "))
num2=int(input("enter the number "))
num3=int(input("enter the number "))
if num1 > num2 & num3:
         print("num 1 is greater ")
elif num2 > num1 & num3:
    print("num2 is greater ")
elif num3 > num1 & num2:
    print("num3 is greater ") 
#finding wheather the following number is factor of 5 or not 
num=int(input(" enter the number "))
if num%5==0:
    print ("number is a factor of 5 ", num)
else:
        print("not a factor of 5")
#finding wheather the following number is a factor of 3 and 5 or not a factor 
num=int(input("enter the number "))
if num%3==0 and num%5==0:
        print ("number is a factor of 3 and 5 ")
elif num%3==0:
    print(" number is a factor of 3")
elif num%5==0:
    print(" number is a factor of 5 ")
elif num%3!=0 or num%5!=0:
    print("not a factor of3 and 5 ")
