//** start of script.js **

function hasExoplanet(readings) {
  let average =  minimunAverage(readings);
  //return readings;
  return foundExoplanet(readings,average);
}

function foundExoplanet(readings, average){
  let found = false;
  for(const element of readings){
    if(charToLuminosity(element) <= average){
      found = true;
      break;
    }
  }
  return found;
}

function minimunAverage(readings){
  let count = 0;
  let minimun;
  for(const element of readings){
    count += charToLuminosity(element);
  }
  minimun = (count / readings.length) * (80 / 100);
  console.log(minimun);
  return minimun;
}

function charToLuminosity(c) {
  if (c >= 'A' && c <= 'Z') {
    return c.charCodeAt(0) - 'A'.charCodeAt(0) + 10;
  } else if (c >= '0' && c <= '9') {
    return parseInt(c);
  } else {
    throw new Error("Carácter inválido");
  }
}



//** end of script.js **

