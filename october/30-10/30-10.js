function nthPrime(n) {

    let count = 0;
    let index = 1;
    let lastPrime = 0;

    while (count < n) {
        if(isPrime(index) == true){
            count += 1
            lastPrime = index
        }

        index += 1;
    }

    console.log(lastPrime)
    return lastPrime;
}

function isPrime(number){

    let isPrime = true;

    if(number <= 1) {
        isPrime = false;
    }

    for(let i=2; i < number -1; i++){
        if(number % i == 0){
            isPrime = false;
            break;
        }else{
            continue;
        }
    }

    return isPrime;

}

//Tests
nthPrime(5) //should return 11.
nthPrime(10) //should return 29.
nthPrime(16) //should return 53.
nthPrime(99) //should return 523.
nthPrime(1000) //should return 7919.