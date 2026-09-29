import java.util.Arrays;
import java.util.List;

public class longest_word {

    public static String getLongestWord(String sentence){

        sentence = sentence.replace(".", "");
        List<String> words = Arrays.asList(sentence.split("\\s+"));

        String long_word = words.get(0);

        for(int i = 1; i < words.size(); i++){
            if (words.get(i).length() > long_word.length()) {
                long_word = words.get(i);
            }
        }

        return long_word;
    }
    
}
