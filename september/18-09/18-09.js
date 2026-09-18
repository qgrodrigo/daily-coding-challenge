function costToFill(tankSize, fuelLevel, pricePerGallon) {

    let cost = (tankSize - fuelLevel) * pricePerGallon;
    let costFormat = `$${cost.toFixed(2)}`;

    console.log(costFormat);


    return costFormat;
}


costToFill(20, 0, 4.00) //should return "$80.00".
costToFill(15, 10, 3.50) //should return "$17.50".
costToFill(18, 9, 3.25) //should return "$29.25".
costToFill(12, 12, 4.99) //should return "$0.00".
costToFill(15, 9.5, 3.98) //should return "$21.89".