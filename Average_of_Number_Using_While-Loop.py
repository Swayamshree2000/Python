#Take 10 numbers from the user and find average value of the entered number using WHILE LOOP .
sum=0
limit=10
#while (limit>0):
for i in range(limit):
    print(limit)
    limit-=1
=======
no=1
while (limit>0):
    userinput=int(input("Enter no %d: "%no))
    sum=sum+userinput
    limit-=1
    no+=1
avg=sum/10
print("The Average is %d"%avg)