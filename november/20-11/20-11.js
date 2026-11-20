function longestWord(sentence) {
    
    let longest = '';

    for (const word of sentence.split(' ')) {
        const clean = [...word].filter(ch => /[a-zA-Z]/.test(ch)).join('');
        if (clean.length > longest.length){
            longest = clean;
        }
    }

    console.log(longest);

    return longest;
}

//Tests:
longestWord("The quick red fox") //should return "quick".
longestWord("Hello coding challenge.") //should return "challenge".
longestWord("Do Try This At Home.") //should return "This".
longestWord("This sentence... has commas, ellipses, and an exclamation point!") //should return "exclamation".
longestWord("A tie? No way!") //should return "tie".
longestWord("Wouldn't you like to know.") //should return "Wouldnt".
