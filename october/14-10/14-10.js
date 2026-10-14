function count(text, pattern) {
    
    text = text.replace(/ /g, '');
    let count = 0;


    for (let index = 0; index < text.length - pattern.length + 1; index++) {
        if(text.slice(index, (index + pattern.length)) == pattern){
            count += 1;
        }
        
    }

    console.log(count);

    return count;
}

count('abcdefg', 'def') //should return 1.
count('hello', 'world') //should return 0.
count('mississippi', 'iss') //should return 2.
count('she sells seashells by the seashore', 'sh') //should return 3.
count('101010101010101010101', '101') //should return 10.