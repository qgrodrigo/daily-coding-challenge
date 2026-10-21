function adjustThermostat(currentF, targetC) {

    let targetCToF = (targetC * 1.8) + 32;

    if(currentF == targetCToF){
        return 'Hold';
    }
    if(currentF < targetCToF){
        return `Cool: ${(targetCToF - currentF).toFixed(1)} degrees Fahrenheit`
    }
    if(currentF > targetCToF){
        return `Cool: ${(currentF - targetCToF).toFixed(1)} degrees Fahrenheit`
    }
    
}

//Tests
adjustThermostat(32, 0) //should return "Hold".
adjustThermostat(70, 25) //should return "Heat: 7.0 degrees Fahrenheit".
adjustThermostat(72, 18) //should return "Cool: 7.6 degrees Fahrenheit".
adjustThermostat(212, 100) //should return "Hold".
adjustThermostat(59, 22) //should return "Heat: 12.6 degrees Fahrenheit".