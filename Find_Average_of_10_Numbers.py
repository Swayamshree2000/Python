#Take 10 numbers from the user and find average value of the entered number using WHILE LOOP .
sum=0
limit=10
no=1
while (limit>0):
#Here user will input the numbers for 10 times .
    userinput=int(input("Enter no %d: "%no))
#Algorithm lines (12,13,14,15)
    sum=sum+userinput
    limit-=1
    no+=1
avg=sum/10
#This is the final output
print("The Average is %d"%avg)
print("The Average is %d"%avg
