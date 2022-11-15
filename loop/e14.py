num= 76542
temp=num
sum=0
rem=0
while temp>0:
    rem=temp%10
    sum= (sum*10)+rem
    temp=temp//10
print(sum)
