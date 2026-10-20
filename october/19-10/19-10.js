function calculateTips(mealPrice, customTip) {

    let price = parseFloat(mealPrice.slice(1,mealPrice.length));
    let tips = [];

    let fifteenPercentTip = `$${(price * 15 / 100).toFixed(2)}`; 
    let twentyPercentTip = `$${(price * 20 / 100).toFixed(2)}`;

    customTip = `$${(price * parseFloat(customTip.slice(0, customTip.length -1)) /100).toFixed(2)}`; 

    tips.push(fifteenPercentTip);
    tips.push(twentyPercentTip);
    tips.push(customTip);

    console.log(tips)

    return tips;
}

//Tests
calculateTips("$10.00", "25%") //should return ["$1.50", "$2.00", "$2.50"].
calculateTips("$89.67", "26%") //should return ["$13.45", "$17.93", "$23.31"].
calculateTips("$19.85", "9%") //should return ["$2.98", "$3.97", "$1.79"].