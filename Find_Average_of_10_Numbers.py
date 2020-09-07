#Take 10 numbers from the user and find average value of the entered number using WHILE LOOP
sum=0
limit=10
no=1
while (limit>0):
    userinput=int(input("Enter no %d: "%no))               #Here user will input the numbers for 10 times
    sum=sum+userinput                                      #Algorithm line 7,8,9,10
    limit-=1
    no+=1
avg=sum/10                                                  
print("The Average is %d"%avg)                              #This is the final output