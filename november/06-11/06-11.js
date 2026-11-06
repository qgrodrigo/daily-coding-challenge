function getWeekday(dateString) {

    let dayOfWeek = new Date(dateString).toLocaleDateString("en-US", {weekday: "long", timeZone:"UTC"});

    console.log(dayOfWeek);

    return dayOfWeek;
}

//Tests
getWeekday("2025-11-06") //should return Thursday.
getWeekday("1999-12-31") //should return Friday.
getWeekday("1111-11-11") //should return Saturday.
getWeekday("2112-12-21") //should return Wednesday.
getWeekday("2345-10-01") //should return Monday.