function formatNumber(number) {

    let country_code = "+" + number.slice(0,1);
    let city_code = "(" + number.slice(1,4) + ")";
    let digits = number.slice(4,7) + "-" + number.slice(7,12);
    let phoneNumber= country_code + " " + city_code + " " + digits;

    console.log(phoneNumber);

    return phoneNumber;
}

formatNumber("05552340182") //should return "+0 (555) 234-0182".
formatNumber("15554354792") //should return "+1 (555) 435-4792".