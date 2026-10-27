function format(seconds) {

    let timeFormated = '';
    let hoursText = '';
    let minutesText = '';
    let secondsText = '';

    let hours = Math.trunc(seconds / 3600);
    let minutes = Math.trunc((seconds % 3600) / 60);
    let restSeconds = (seconds % 3600) % 60;

    if(restSeconds < 10){
        secondsText = `0${restSeconds}`;
    }else{
        secondsText = restSeconds.toString();
    }

    if(minutes < 0){
        minutesText = '0';
    }
    else if(minutes > 0 && minutes < 10){
        if(hours < 1){
            minutesText = `${minutes}`;
        }else{
            minutesText = `0${minutes}`;
        }
    }else{
        minutesText = minutes.toString();
    }

    if(hours > 0){
        hoursText = `${hours}:`;
    }

    timeFormated = `${hoursText}${minutesText}:${secondsText}`;
    console.log(timeFormated);

    return timeFormated;
}

//Tests
format(500) //should return "8:20".
format(4000) //should return "1:06:40".
format(1) //should return "0:01".
format(5555) //should return "1:32:35".
format(99999) //should return "27:46:39".