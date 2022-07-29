##Names =["Paul", "James", "Prosper", "John"]
##
####print(Names)
##
##
##Input_Name = input("Enter your name: ")
##Input_Age = input("Enter your age: ")
##

#WRITE A PROGRAM THAT ASKS THE USER FOR HIS/HER 
#NAME AND AGE THEN USES A CUSTOM FUNCTION THAT
#TAKES IN THE ENTERED AGE AND RETURNS THE YEAR
#THEY WERE BORN. 
#EXAMPLE : 
#INPUT FOR NAME : PERFECT
#INPUT FOR AGE : 23
#OUTPUT: HELLO, PERFECT. YOU WERE BORN IN THE YEAR 1999




##Input_name = input("Please enter your name: ")
##Input_age = int(input("Please enter your age: "))
##
##print("Hello " + Input_name+ "! you were born in  the year: ", 0-Input_age+2022)
##          
##






##

##for i in range(1,25):
##    count = 0
##    for j in range(1,i-1):
##        if (i%j==0):
##            count=count+1
##        if (count==2):
##            print(i)


##Name = input("Enter your name: ")
##
##Age = int(input("Enter your age: "))
##
##print("Hello " +Name+ ", you were born in the year", 0-Age+2022)
## 

Name = input("Enter your name: ")
Age = int(input("Enter your age: "))

def getYear():

    Year = 2022

    return Year - Age
          

print("Hello " + Name+
      ", you were born in the year", getYear())



































