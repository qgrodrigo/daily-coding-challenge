function secondLargest(arr) {

    arr.sort((a,b) => a -b );
    
    let unique_list = [];

    for (const element of arr) {

        if(!unique_list.includes(element)){
            unique_list.push(element);
        }
        
    }

    let second = unique_list[unique_list.length -2];
    console.log(second);

    return second;
}