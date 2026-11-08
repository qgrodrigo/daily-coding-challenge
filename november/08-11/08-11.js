function canPost(message) {

    let postType = '';

    if(message.length <= 40){
        postType = 'short post';
    }

    if(message.length > 40 && message.length <= 80){
        postType = 'long post';
    }

    if(message.length > 80){
        postType = 'invalid post';
    }

    console.log(postType);

    return postType;
}


//Tests
canPost("Hello world") //should return "short post".
canPost("This is a longer message but still under eighty characters.") //should return "long post".
canPost("This message is too long to fit into either of the character limits for a social media post.") //should return "invalid post".