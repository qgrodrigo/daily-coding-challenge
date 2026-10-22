function wiseSpeak(sentence) {

    let words = sentence.split(' ');
    //console.log(words)

    let searchWords = ["have", "must", "are", "will", "can"]
    let acumulate = '';
    let firstHalf = '';
    let secondHalf = '';
    let wiseSentence = '';

    for (const element of words) {
        acumulate += ' ' + element;
        if(searchWords.includes(element)){
            firstHalf += acumulate
            acumulate = ''
        }

        secondHalf = acumulate
    }

    firstHalf = firstHalf + secondHalf.at(-1);
    secondHalf = secondHalf.replace(secondHalf.at(-1), ',');
    secondHalf = secondHalf.trim();
    secondHalf = secondHalf.charAt(0).toUpperCase() + secondHalf.slice(1);
    wiseSentence = secondHalf + firstHalf.toLowerCase();
    console.log(wiseSentence);


    return wiseSentence;
}

//Tests

wiseSpeak("You must speak wisely.") //should return "Speak wisely, you must."
wiseSpeak("You can do it!") //should return "Do it, you can!"
wiseSpeak("Do you think you will complete this?") //should return "Complete this, do you think you will?"
wiseSpeak("All your base are belong to us.") //should return "Belong to us, all your base are."
wiseSpeak("You have much to learn.") //should return "Much to learn, you have."