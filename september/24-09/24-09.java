boolean isPerfectSquare(int n){

        double square = Math.sqrt(n);

        if(square >= 0){
            
            if(square % 1 == 0){
                return true;
            
            }else{
                
                return false;
            }
        }else{

            return false;
        }

}    
    

    

