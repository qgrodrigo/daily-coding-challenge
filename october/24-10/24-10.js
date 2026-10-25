function dive(map, coordinates) {

    let xPosition = coordinates[0];
    let yPosition = coordinates[coordinates.length-1];
    let countAllOs = 0;
    let positions = [];

    for(let i=0; i < map.length; i++){
        for(let j=0; j < map[i].length; j++){
            if(map[i][j] == 'O'){
                countAllOs += 1
                positions.push([i,j]);
            }

        }
    }

    const ok = positions.some(fila =>
        fila.length === coordinates.length &&
        fila.every((v, i) => v === coordinates[i])
    );

    
    if(ok && positions.length > 1){
        console.log('Found')
        return 'Found';
    }
    if(ok && positions.length == 1){
        console.log('Recovered')
        return 'Recovered';
    }

    if(map[xPosition][yPosition] == '-'){
        console.log('Empty')
        return 'Empty';
    }

    if(map[xPosition][yPosition] == 'X'){
        console.log('Found')
        return 'Found';
    }

}

dive([[ "-", "X"], [ "-", "X"], [ "-", "O"]], [2, 1]) //should return "Recovered".
dive([[ "-", "X"], [ "-", "X"], [ "-", "O"]], [2, 0]) //should return "Empty".
dive([[ "-", "X"], [ "-", "O"], [ "-", "O"]], [1, 1]) //should return "Found".
dive([[ "-", "-", "-"], [ "X", "O", "X"], [ "-", "-", "-"]], [1, 2]) //should return "Found".
dive([[ "-", "-", "-"], [ "-", "-", "-"], [ "O", "X", "X"]], [2, 0]) //should return "Recovered".
dive([[ "-", "-", "-"], [ "-", "-", "-"], [ "O", "X", "X"]], [1, 2]) //should return "Empty".