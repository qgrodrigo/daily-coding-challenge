function count(str) {

    str = str.toLowerCase();
    const VOWELS = ['a', 'e', 'i', 'o', 'u'];
    let vowelsCount = 0;
    let consonantsCount = 0;

    const isAlpha = str => !/[^a-z]/i.test(str);

    for (const char of str) {
        if (isAlpha(char)){
            if (VOWELS.includes(char)){
                vowelsCount += 1;
            }else{
                consonantsCount += 1
            }
        }
    }

    console.log([vowelsCount, consonantsCount]);

    return [vowelsCount, consonantsCount];
}

//Tests:
count("Hello World") //should return [3, 7].
count("JavaScript") //should return [3, 7].
count("Python") //should return [1, 5].
count("freeCodeCamp") //should return [5, 7].
count("Hello, World!") //should return [3, 7].
count("The quick brown fox jumps over the lazy dog.") //should return [11, 24].