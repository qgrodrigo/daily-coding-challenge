// start of script.js **

function complementaryDNA(strand) {

    const dictionary = new Map();
    dictionary.set("A", "T");
    dictionary.set("T", "A");
    dictionary.set("C", "G");
    dictionary.set("G", "C");

    let complementary = "";
    for(let char of strand) {
        complementary += dictionary.get(char);
    }

    return complementary;
}

// end of script.js **

