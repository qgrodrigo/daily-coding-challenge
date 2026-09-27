import java.util.ArrayList;
import java.util.List;

public class CaugthSpeeding {
    
    public static List<Number> speeding(List<Integer> speeds, int limit){

        int count = 0;
        double average = 0;
        int sumExcess = 0;
        List<Number> answerList = new ArrayList<>();

        for (Integer i : speeds) {
            if(i > limit){
                count += 1;
                sumExcess += (i - limit);
            }
        }

        if (count == 0) {
            answerList = List.of(0,0);
        }else{
            average = (double)sumExcess / count;
            answerList = List.of(count, average);
        }

        System.out.println(answerList);

        return answerList;
    }
    
}
