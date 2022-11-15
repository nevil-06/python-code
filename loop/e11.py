prime_list = []
for i in range(25,50):
    if i ==0 or i==1:
        continue
    else:
        for j in range(2,int(i/2)+1):
            if i%j==0:
                break
            else:
                prime_list.append(i)   


for i in range(len(prime_list)+1):
    print(prime_list[i])
         