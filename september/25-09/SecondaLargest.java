
import java.util.Collections;
import java.util.List;

public class SecondaLargest {
    

    public static int secondLargest(List<Integer>  arr){

        int second;

        Collections.sort(arr);
        second = arr.get(arr.size() -2);

        return second;
    }
    
}
