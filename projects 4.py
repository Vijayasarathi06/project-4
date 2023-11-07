##Amstrong number
num=int(input("enter the number"))
k=str(num)
length=len(k)
result=0
a=num
while num>0:
    x=num%10
    result=result+x**length
    num=num//10
if a==result:
    print("it is a Amstrong number",result)
else:
    print("false")

##Happy number//Sad number
num=int(input("enter the value of number"))
a=num
while a>0:
    result=0
    x=a%10
    result=result+(x**2)
    a=a//10
a=result
if result==1:
    print("it is a happy number",result)
else:
    print("it is a sad number",result)
##Disarium number
num=int(input("enter the value of number"))
temp=num
x=num
count=0
while temp>0:   
    temp=temp//10
    count=coun  t+1
a=0
while x>0:
    rem=x%10
    a=a+(rem**count)
    x=x//10
    count=count-1
if a==num:
    print("it is a disarium number")
else:
    print("it is not a disarium number")

##factorial number  
num=int(input("enter the value of number"))
factorial=1
for i in range(1,num+1):
    factorial*=i
print(factorial)
   
##Factor number
num=int(input("enter the value of number"))
for i in range(1,num+1):
    if num%i==0:
        print(i)
    
    
    

















