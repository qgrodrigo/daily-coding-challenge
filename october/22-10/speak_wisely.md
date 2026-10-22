#Speak Wisely, You Must
Given a sentence, return a version of it that sounds like advice from a wise teacher using the ##following rules:

Words are separated by a single space.
Find the first occurrence of one of the following words in the sentence: "have", "must", "are", "will", "can".
Move all words before and including that word to the end of the sentence and:
Preserve the order of the words when you move them.
Make them all lowercase.
And add a comma and space before them.
Capitalize the first letter of the new first word of the sentence.
All given sentences will end with a single punctuation mark. Keep the original punctuation of the sentence and move it to the end of the new sentence.
Return the new sentence, make sure there's a single space between each word and no spaces at the beginning or end of the sentence.
For example, given "You must speak wisely." return "Speak wisely, you must."

##Tests:
wise_speak("You must speak wisely.") should return "Speak wisely, you must."
wise_speak("You can do it!") should return "Do it, you can!"
wise_speak("Do you think you will complete this?") should return "Complete this, do you think you will?"
wise_speak("All your base are belong to us.") should return "Belong to us, all your base are."
wise_speak("You have much to learn.") should return "Much to learn, you have."