function imageSearch(images, term) {

    let searchResult = [];

    for(let image of images){
        if(image.toLowerCase().includes(term.toLowerCase())){
            searchResult.push(image);
        }
    }

    console.log(searchResult);

    return searchResult;
}

//Tests
imageSearch(["dog.png", "cat.jpg", "parrot.jpeg"], "dog") //should return ["dog.png"].
imageSearch(["Sunset.jpg", "Beach.png", "sunflower.jpeg"], "sun") //should return ["Sunset.jpg", "sunflower.jpeg"].
imageSearch(["Moon.png", "sun.jpeg", "stars.png"], "PNG") //should return ["Moon.png", "stars.png"].
imageSearch(["cat.jpg", "dogToy.jpeg", "kitty-cat.png", "catNip.jpeg", "franken_cat.gif"], "Cat") //should return ["cat.jpg", "kitty-cat.png", "catNip.jpeg", "franken_cat.gif"].