#Take 10 numbers from the user and find average value of the entered number using WHILE LOOP
sum=0
limit=10
number=1

#This WHILE-LOOP statement helps the loop to run 10 times
while (limit>0):

#Here user will input the numbers for 10 times
    userinput=int(input("Enter no %d: "%number))

#Algorithm lines (13,14,15)
    sum=sum+userinput
    limit-=1
    number+=1
                  
#This is the final output.
print("The Average is %d"%(sum/10))