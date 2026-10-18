def sock_pairs(pairs, cycles):
   
    socks_count = 0
    pairs_rest = 0
   
    for i in range(1, cycles +1):
        if(i % 2 == 0):
            socks_count -= 1


        if(i % 3 == 0):
            socks_count += 1


        if(i % 5 == 0):
            socks_count -= 1


        if(i % 10 == 0):
            socks_count += 2


     
           
    total_socks = (pairs * 2) + socks_count
   
    if(total_socks > 0):
        pairs_rest = total_socks // 2
   
   
    print(pairs_rest)
   
    return pairs_rest
   


#Tests:


sock_pairs(2, 5) #should return 1.
sock_pairs(1, 2) #should return 0.
sock_pairs(5, 11) #should return 4.
sock_pairs(6, 25) #should return 3.
sock_pairs(1, 8) #should return 0.
