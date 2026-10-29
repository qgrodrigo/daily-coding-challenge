function navigate(commands) {
    
    let back = [];
    let current = 'Home';
    let forward = [];

    for (let command of commands) {

        if(command.includes('Visit')){
            let page = command.slice(6, command.length);
            back.push(current);
            current = page;
            forward.length = 0;

        }

        if(command == 'Back'){
            if (back.length > 0){
                forward.push(current);
                current = back[back.length -1];
                back.pop();
            }

        }

        if(command == 'Forward'){
            if(forward.length > 0){
                back.push(current);
                current = forward[0];
            }
        }

        
    }

    console.log(current)

    return current;
}

//Tests:
navigate(["Visit About Us", "Back", "Forward"]) //should return "About Us".
navigate(["Forward"]) //should return "Home".
navigate(["Back"]) //should return "Home".
navigate(["Visit About Us", "Visit Gallery"]) //should return "Gallery".
navigate(["Visit About Us", "Visit Gallery", "Back", "Back"]) //should return "Home".
navigate(["Visit About", "Visit Gallery", "Back", "Visit Contact", "Forward"]) //should return "Contact".
navigate(["Visit About Us", "Visit Visit Us", "Forward", "Visit Contact Us", "Back"]) //should return "Visit Us".