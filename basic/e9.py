num=121

temp=num
sum=0
while temp>0:
    rem=temp%10
    sum=(sum*10)+rem
    temp=temp//10

if num==sum:
    print("number is palindrom")
else:
    print("not palindrome")