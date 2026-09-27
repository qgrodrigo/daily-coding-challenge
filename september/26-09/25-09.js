function speeding(speeds, limit) {

    let average = 0;
    let count = 0;
    let sumExces = 0;
    let answerList = [];

    for(const i of speeds){
        if(i > limit){
            count += 1;
            sumExces += (i-limit);

        }
    }

    if(count == 0){
        answerList = [0,0];
    }else{
        average = sumExces / count;
        answerList = [count, average];
    }

    console.log(answerList);
        
    return answerList;
}