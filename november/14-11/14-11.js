function daysUntilWeekend(dateString) {

    let day = new Date(dateString).getUTCDay();
    const WEEKEND = [0, 6];
    let message = '';

    if (WEEKEND.includes(day)){
        message = "It's the weekend!";
    } else{
        let daysToWeekend = 6 - day;
        if (daysToWeekend == 1){
            message = `${daysToWeekend} day until the weekend.`;
        } else{
            message = `${daysToWeekend} days until the weekend.`;
        }
    }

    console.log(message)

    return message;
}

//Tests:
daysUntilWeekend("2025-11-14") //should return "1 day until the weekend.".
daysUntilWeekend("2025-01-01") //should return "3 days until the weekend.".
daysUntilWeekend("2025-12-06") //should return "It's the weekend!".
daysUntilWeekend("2026-01-27") //should return "4 days until the weekend.".
daysUntilWeekend("2026-09-07") //should return "5 days until the weekend.".
daysUntilWeekend("2026-11-29") //should return "It's the weekend!".