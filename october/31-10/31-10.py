def spookify(boo):

    boo = boo.replace('-' , '~')
    boo = boo.replace('_', '~')
    spooki_boo = ''
    
    count = 0
    for i in range(len(boo)):
        if boo[i] != '~':
            
            if count % 2 == 0:
                spooki_boo += boo[i].upper()
            else:
                spooki_boo += boo[i].lower()
            
            count += 1
        else:
            spooki_boo += boo[i]
    
    print(spooki_boo)
    
    return spooki_boo



spookify("hello_world") #should return "HeLlO~wOrLd".
spookify("Spooky_Case") #should return "SpOoKy~CaSe".
spookify("TRICK-or-TREAT") #should return "TrIcK~oR~tReAt".
spookify("c_a-n_d-y_-b-o_w_l") #should return "C~a~N~d~Y~~b~O~w~L".
spookify("thE_hAUntEd-hOUsE-Is-fUll_Of_ghOsts") #should return "ThE~hAuNtEd~HoUsE~iS~fUlL~oF~gHoStS".