#Print multiplication table of 14 from a list in which multiplication table of 12 is stored. (using for loop)

#12's Table
table_12=[12,24,36,48,60,72,84,96,108,120]
table_13=[]

#variable for 14's table
start=14
multiply=1

#for increament of 2 in each loop
a=2

#Algorith using FOR-LOOP
for i in table_12:
    #print("%d X %d = %d"%(start,multiply,(i+a)))
    table_13.append(i+a)
    a+=2
    multiply+=1
print(table_13)