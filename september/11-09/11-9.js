function reverseSentence(sentence) {
    
    let words = sentence.trim().split(/\s+/);
    words.reverse();
    let reverse = words.join(' ');

    console.log(reverse)
    
    return reverse;
}