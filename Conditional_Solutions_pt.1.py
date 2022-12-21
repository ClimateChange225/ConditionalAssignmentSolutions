'''
n=int(input("Enter a number: "))
if n>0:
    print("The number is positive")
elif n<0:
    print("The number is negative")
else:
    print("The number is negative")
'''
'''
n=int(input("Enter a number: "))
if n%2==0:
    print("The number is even")
else:
    print("The number is odd")
'''
'''
a1=int(input("Enter the age of person 1: "))
a2=int(input("Enter the age of person 2: "))
if a1>a2:
    print("Person 1's age is greater")
elif a1<a2:
    print("Person 2's age is greater")
else:
    print("Age of person 1 and person 2 are equal")
'''
'''
yr=int(input("Enter a year: "))
if yr%4==0 and yr%100!=0 or yr%400==0:
    print("The year is a leap year")
else:
    print("The year is not a leap year")
'''
'''
age=int(input("Enter your age: "))
if age>=18:
    print("You are an adult")
else:
    print("You are not an adult")
'''
'''
age=int(input("Enter your age: "))
if age>=60:
    print("You are a senior citizen")
else:
    print("You are not a senior citizen")
'''
'''
#Question 7-12
its=int(input("Enter the number of numbers: "))
l1=[]
for i in range(1,its+1):
    elem=int(input("Enter a number: "))
    l1.append(elem)
l1.sort
print("Greatest number is:", l1[-1])
print("Smallest number is:", l1[0])
'''
'''
n=int(input("Enter a number: "))
if n%5==0 and n%11==0:
    print("The number is divisible by 5 and 11")
elif n%5!=0 and n%11==0:
    print("The number is divisible by 11 but not 5")
elif n%5==0 and n%11!=0:
    print("The number is divisible by 5 but not by 11")
else:
    print("The number isn't divisible by 5 and 11")
'''
'''
n=int(input("Enter the numbeber name you want to be displayed(0-9): "))
dic1={0:"Zero", 1:"One", 2:"Two", 3:"Three", 4:"Four", 5:"Five", 6:"Six", 7:"Seven", 8:"Eight", 9:"Nine"}
print(dic1[n])
'''
'''
n=str(input("Enter a letter: "))
if n.lower().strip()=="a" or n.lower().strip()=="e" or n.lower().strip()=="i" or n.lower().strip()=="o" or n.lower().strip()=="u":
    print("The letter is a vowel")
else:
    print("The letter isn't a vowel")
'''
'''
print("Enter the number corresponding to the menu option: ")
opt=int(input("1. Area of circle\n2. Area of square\n3. Area of rectangle\n"))
if opt==1:
    r=int(input("Enter radius: "))
    print("The area of the circle is:", 3.14*r*r)
elif opt==2:
    s=int(input("Enter the side: "))
    print("Area of the square is:", s*s)
elif opt==3:
    l=int(input("Enter length: "))
    b=int(input("Enter breadth: "))
    print("Area of rectangle is:", l*b)
'''
'''
math=int(input("Enter marks for math: "))
sci=int(input("Enter marks for sci: "))
eng=int(input("Enter marks for eng: "))
total=int(input("Enter the total out of which the marks were calculated: "))
if math/total*100>=80 and sci/total*100>=80 and eng/total*100>=80:
    print("Your stream is pure science")
elif math/total*100>=60 and sci/total*100>=80 and eng/total*100>=80:
    print("Your stream is bio. science")
else:
    print("Your stream is commerce")
'''
'''
sale=int(input("Enter the value of sales occurring: "))
if sale>=10_001:
    print("Discount is:", 0.1*sale, "\nAmount payable is:", sale-0.1*sale)
elif sale>5_000:
    print("Discount is:", 0.08*sale, "\nAmount payable is:", sale-0.08*sale)
else:
    print("Discount is:", 0.05*sale, "\nAmount payable is:", sale-0.05*sale)
'''
'''
income=float(input("Enter your income: "))
if income>20_001:
    print("Tax:", 0.2*income, "\nSurcharge:", 0.13*income, "\nUsable Income:", income-((0.2*income)+(0.13*income)))
elif income<15_000:
    print("Tax:", 0.18*income, "\nSurcharge:", 0.11*income, "\nUsable Income:", income-((0.18*income)+(0.11*income)))
else:
    print("Tax:", 0.15*income, "\nSurcharge:", 0.07*income, "\nUsable Income:", income-((0.15*income)+(0.07*income)))
'''
'''
n=int(input("Enter your percentage: "))
print("Your division is: ", end="")
if n>=60:
    print("First")
elif n>50:
    print("Second")
elif n>40:
    print("Third")
else:
    print("Failed")
'''
'''
dist=int(input("Enter distance travelled: "))
if dist>40:
    print("Your fare is:", 20*10+20*7+(dist-40)*6)
elif dist>20:
    print("Your fare is:", 20*10+(dist-20)*7)
else:
    print("Your fare is:", dist*10)
'''
'''
n=int(input("Enter the number of days by which the deadline was missed: "))
if n>10:
    print("Fee chargable is:", (5*0.4)+(5*0.65)+((n-10)*0.8))
elif n>5:
    print("Fee chargable is:", (5*0.4)+((n-5)*0.65))
else:
    print("Fee chargable is:", n*0.4)
'''
'''
n=int(input("Enter the number of days: "))
if n>300:
    print("Your electricity bill is: ", (100*1)+(200*2)+((n-300)*4))
elif n>200:
    print("Your electricity bill is:", (100*1)((n-100)*2))
else:
    print("Your electricity bill is:", 100*n)
'''