function tooMuchScreenTime(hours) {
    
    let tooMuch = false;
    
    //condicionals
    //Si un solo día tiene 10 horas o más, es demasiado.
    for(const element of hours){
        if(element >= 10){
        tooMuch = true;
        }
    }
    //Si el promedio de tres días seguidos es mayor o igual a 8 horas, es demasiado.
    for(let i=0; i <= hours.length - 3; i++){
            
            let group = hours.slice(i,i+3)
            let sum = 0;
            for (const element of group){
                sum += element;

            }
            let mean = sum / 3;

            if(mean >= 8){
            tooMuch = true;
            }

        }

    //Si el promedio de los siete días es mayor o igual a 6 horas, es demasiado.
    let sum = 0;
    for(const element of hours){
        sum += element
    }

    //console.log(sum);

    let mean = sum / hours.length;

    //console.log(mean);

    if(mean >= 6){
        tooMuch = true
    }

    
    return tooMuch;
}