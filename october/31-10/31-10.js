function spookify(boo) {

    boo = boo.replaceAll('-', '~');
    boo = boo.replaceAll(/_/g, '~');

    let spookyBoo = '';
    let count = 0;

    for(let i=0; i < boo.length; i++){
        if(boo[i] != '~'){
            if(count % 2 == 0){
                spookyBoo += boo[i].toUpperCase();
            }else{
                spookyBoo += boo[i].toLowerCase();
            }

            count += 1
        }else{
            spookyBoo += boo[i];
        }
    }

    console.log(spookyBoo)
    return spookyBoo;
}

//Tests
spookify("hello_world") //should return "HeLlO~wOrLd".
spookify("Spooky_Case") //should return "SpOoKy~CaSe".
spookify("TRICK-or-TREAT") //should return "TrIcK~oR~tReAt".
spookify("c_a-n_d-y_-b-o_w_l") //should return "C~a~N~d~Y~~b~O~w~L".
spookify("thE_hAUntEd-hOUsE-Is-fUll_Of_ghOsts") //should return "ThE~hAuNtEd~HoUsE~iS~fUlL~oF~gHoStS".