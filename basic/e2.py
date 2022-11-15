for i in range(10):
    sum=0
    curr_num = i
    if(curr_num==0):
        prev_num = curr_num
    else:
        prev_num = i-1
    sum =prev_num+curr_num
    print("previous number ",(prev_num)," and current number", (curr_num) ,"and sum is :",(sum))

    #done