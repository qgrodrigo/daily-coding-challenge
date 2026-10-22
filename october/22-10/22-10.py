def wise_speak(sentence):

    search_words = ["have", "must", "are", "will", "can"]
    words = sentence.split()
    advice = ''
    first_half = ''
    second_half = ''

    for word in words:
        advice += " " + word
        if word in search_words:
            first_half += advice
            advice = ''
        second_half = advice


    first_half = first_half + second_half[-1]
    second_half = second_half.replace(second_half[-1], ',')

    wise_sentece = second_half.strip().capitalize() + first_half.lower()

    print(wise_sentece)

        


    return wise_sentece

##Tests:
wise_speak("You must speak wisely.") #should return "Speak wisely, you must."
wise_speak("You can do it!") #should return "Do it, you can!"
wise_speak("Do you think you will complete this?") #should return "Complete this, do you think you will?"
wise_speak("All your base are belong to us.") #should return "Belong to us, all your base are."
wise_speak("You have much to learn.") #should return "Much to learn, you have."