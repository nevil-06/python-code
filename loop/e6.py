num =75869
count=0
rem=0
temp=num
while temp>0:
    rem = num%10
    count+=1
    temp=temp//10
print(count)