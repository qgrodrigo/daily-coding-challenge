function arrayDiff(arr1, arr2) {

    let arrayDif = [];

    for(const element of arr1){
        if(!arr2.includes(element)){
        arrayDif.push(element);
        }
    }


    for(const element of arr2){
        if(!arr1.includes(element)){
        arrayDif.push(element);
        }
    }

    arrayDif.sort();

    return arrayDif;
}