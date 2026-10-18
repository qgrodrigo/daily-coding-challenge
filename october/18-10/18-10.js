function sockPairs(pairs, cycles) {

    let countSocks = 0;
    let totalSocks = 0;
    let totalPairs = 0;

    for(let i= 1; i < cycles +1 ; i++){
        
        if(i % 2 == 0){
            countSocks -= 1
        }
        if(i % 3 == 0){
            countSocks += 1
        }
        if(i % 5 == 0){
            countSocks -= 1
        }
        if(i % 10 == 0){
            countSocks += 2
        }

    }

    totalSocks = (pairs * 2) + countSocks

    if(totalSocks > 0){
        totalPairs = Math.floor(totalSocks / 2)
    }

    console.log(totalPairs)

    return pairs;
}

sockPairs(2, 5)  //should return 1.
sockPairs(1, 2)  //should return 0.
sockPairs(5, 11) //should return 4.
sockPairs(6, 25) //should return 3.
sockPairs(1, 8)  //should return 0.