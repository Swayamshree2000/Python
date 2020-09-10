#for the print of star
i=1

#spacing
j=2         
while (i>=1):
    a=" "*j+"*"*i+" "*j
    print(a)
    i+=2
    j-=1
    if i>5:
        break;

j=1
i=3
while i>=1:
    a=" "*j+"*"*i+" "*j
    print(a)
    j+=1
    i-=2