function moonPhase(dateString) {

    const baseDate = new Date("2000-01-06").getTime() / 1000;  // segundos
    const toDate   = new Date(dateString).getTime() / 1000;

    let diferenceDays = (toDate - baseDate) / 86400;
    let days = diferenceDays % 28 + 1;

    let phase = '';

    if(days >= 1 && days <= 7){
        phase = 'New';
    }
    if(days >= 8 && days <= 14){
        phase = 'Waxing';
    }
    if(days >= 15 && days <= 21){
        phase = 'Full';
    }
    if(days >= 22 && days <= 28){
        phase = 'Waning';
    }
    

    console.log(phase);

    return phase;
}

moonPhase("2000-01-12") //should return "New".
moonPhase("2000-01-13") //should return "Waxing".
moonPhase("2014-10-15") //should return "Full".
moonPhase("2012-10-21") //should return "Waning".
moonPhase("2022-12-14") //should return "New".