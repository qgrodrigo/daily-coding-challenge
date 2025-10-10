public class code {
    public float launchFuel(float payload){
        float count = 0;

        while (payload > 1) {
            payload = payload / 5;
            count += payload;
        }
        return count;
    }
    
   
}
