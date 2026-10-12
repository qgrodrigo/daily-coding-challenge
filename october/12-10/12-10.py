def battle(our_team, opponent):

    team_words = our_team.split()
    opponent_words = opponent.split()


    our = 0
    opp = 0

    for team, opponent in zip(team_words, opponent_words):

        if(sum_words_value(team) > sum_words_value(opponent)):
            our += 1

        if(sum_words_value(team) < sum_words_value(opponent)):
            opp += 1

    print(our)
    print(opp)

    if our > opp:
       return 'We win'
    
    if our < opp:
        return 'We lose'     

    if our == opp:
        return 'Draw'    



def sum_words_value(word):
    value = 0
        
    for letter in word:
        if(letter == letter.upper()):
            value += (ord(letter) - 64) * 2 
        else:
            value += ord(letter) - 96

    return value




#print(battle("hello world", "hello word")) #should return 
print(battle("Hello world", "hello world")) #should return "We win"
#print(battle("lorem ipsum", "kitty ipsum")) #should return "We lose".