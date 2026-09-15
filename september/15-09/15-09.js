function adjustThermostat(temp, target) {

    let adjust = '';

    if (temp < target){
        adjust = 'heat';
    }else if(temp > target){
        adjust = 'cool';
    }else{
        adjust = 'hold';
    }

    return adjust;
}