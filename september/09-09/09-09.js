function allUnique(str) {
  
    let isUnique = true;

  for (let index = 0; index < str.length -2; index++) {
    
    let cut = str.substring(index +1, str.length);
    console.log(str[i])

    if(cut.includes(str[index])){
        isUnique = false;
    }
    
  }

  return isUnique;
}