function to12(time) {

    let hour = parseInt(time.slice(0, 2));
    let minute = time.slice(2, time.length);
    let hour_to_12 = ''

   
    if(hour < 12 ){

        if(hour == 0){
            hour_to_12 += '12:' + minute + ' AM'
        }else{
            hour_to_12 += hour + ':' + minute + ' AM'
        }
        
    }
    if(hour > 12){
        hour_to_12 += (hour - 12).toString() + ':' + minute + ' PM'
    }
     

    console.log(hour_to_12);

    return hour_to_12;
}

to12("1124") //should return "11:24 AM".
to12("0900") //should return "9:00 AM".
to12("1455") //should return "2:55 PM".
to12("2346") //should return "11:46 PM".
to12("0030") //should return "12:30 AM".