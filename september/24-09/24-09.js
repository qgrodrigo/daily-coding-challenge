function isPerfectSquare(n) {

    let isPerfect = false;
    let square = Math.sqrt(n);
    //console.log(square);

    if(n >= 0){
        if(square % 1 == 0){
            isPerfect = true;
        }else{
            isPerfect = false;
        }
    }else{
        isPerfect = false;
        
    }

    console.log(isPerfect);

    return isPerfect;
}