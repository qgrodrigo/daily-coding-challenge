//** start of script.js **

function classification(temp) {

  let message = "";

  if(temp <= 3699){
    message = "M";
  }
  else if(temp <= 5199){
    message = "K";
  }
  else if(temp <= 5999){
    message = "G";
  }
  else if(temp <= 7499){
    message = "F";
  }
  else if(temp <= 9999){
    message = "A";
  }
  else if(temp <= 29999){
    message = "B";
  }
  else{
    message = "O";
  }
        

  return message;
}

//** end of script.js **

