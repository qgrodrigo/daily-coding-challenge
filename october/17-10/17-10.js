function mask(card) {

    let maskedVersion = '';


    for(let i=0; i < card.length; i++){

        if(i < card.length-4){

        if(card[i] == ' ' || card[i] == '-'){
            maskedVersion += card[i];

        }else{

            maskedVersion += '*';

        }    
        }else{

        maskedVersion += card[i];
        
        }

    }

    console.log(maskedVersion);


    return maskedVersion;
}

mask("4012-8888-8888-1881") //should return "****-****-****-1881".
mask("5105 1051 0510 5100") //should return "**** **** **** 5100".
mask("6011 1111 1111 1117") //should return "**** **** **** 1117".
mask("2223-0000-4845-0010") //should return "****-****-****-0010".