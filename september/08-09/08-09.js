function buildAcronym(str) {

  let words = str.split(' ');
  const ignoreWords = ['a', 'for', 'an', 'and', 'by', 'of'];
  let acronym = '';

  for(let i=0; i < words.length; i++){
    
    let word = words[i];
    if(i == 0){
      acronym += word[0].toUpperCase();
    }else{
      if(!ignoreWords.includes(word)){
        acronym += word[0].toUpperCase();
      }
    }
  }  

  return acronym;
}