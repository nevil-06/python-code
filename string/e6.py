str1 = "P@#yn26at^&i5ve"
count1=0
count2=0
count3=0
for i in str1:
    if i.isalpha():
        count1+=1
    elif i.isnumeric():
        count2+=1
    else:
        count3+=1

print("alpahbest are",count1,"numbers are",count2,"symbols are",count3)