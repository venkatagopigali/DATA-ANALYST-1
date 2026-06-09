def prime_count(a,b):
    p_c=0
    for i in range(a,b+1):
        # print(i)
        c=0
        for j in range(1,i+1):
            if i%j==0:
                c+=1
        if c==2:
            p_c+=1
    print(p_c)



