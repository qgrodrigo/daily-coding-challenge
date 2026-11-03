function infected(days) {

    let infectedCount = 1;

    for(let i= 1; i < days + 1; i++){
        infectedCount *= 2;

        if(i % 3 == 0){
            const parchNumber = Math.ceil(infectedCount * 0.2);
            infectedCount -= parchNumber; 
        }
    }

    console.log(infectedCount);

    return infectedCount;
}

// Tests:
infected(1) //should return 2.
infected(3) //should return 6.
infected(8) //should return 152.
infected(17) //should return 39808.
infected(25) //should return 5217638.