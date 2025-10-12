// start of script.js **

function hexToDecimal(hex) {
  
  let count = 0;
  hex = hex.split('').reverse().join('');
  let i = 0;
  
  while(i < hex.length){
    count += toDecimal(hex.substring(i, i+1)) * (16 ** i);
    i += 1;
  } 
  
  return count;
}

function toDecimal(hex){
  let decimal = hex;

  if(hex == "A"){
    decimal = "10";
  }else if(hex == "B"){
    decimal = "11";
  }else if(hex == "C"){
    decimal = "12";
  }else if(hex == "D"){
    decimal = "13";
  }else if(hex == "E"){
    decimal = "14";
  }else if(hex == "F"){
    decimal = "15";
  }

  return parseInt(decimal);
}
