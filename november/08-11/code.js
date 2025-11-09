// start of script.js **

function canPost(message) {

  let postType = "";

  if(message.length <= 40){
    postType = "short post";
  }else if(message.length > 40 && message.length <= 80){
    postType = "long post";
  }else if(message.length > 80){
    postType = "invalid post";
  }

  return postType;
}

// end of script.js **

