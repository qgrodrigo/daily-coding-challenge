function isMirror(str1, str2) {

    let cleanStr1 = str1.replace(/[^a-zA-Z0-9]/g, '');
    let cleanStr2 = str2.replace(/[^a-zA-Z0-9]/g, '');
    let invertStr2 = cleanStr2.split('').reverse().join('');

    if (cleanStr1 == invertStr2) {
        
        console.log(true);
        return true;

    }else{

        console.log(false);
        return false;

    }
}