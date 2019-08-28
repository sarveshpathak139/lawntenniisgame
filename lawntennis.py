server_score = 0 
opp_score = 0
while True:   
    i = raw_input("Enter who wins this match S or O")
    if(i == 's' and server_score < 30):        
        server_score += 15
    elif(i == 's' and server_score == 30 and server_score <= 40):
        server_score += 10
    elif(i == 's' and server_score >= 40):
        server_score += 1
        r = server_score - opp_score
        if (r >= 2):
            print ("Server has won the game")
            exit()
    elif(i == 'o' and opp_score < 30):        
        opp_score += 15
    elif(i == 'o' and opp_score == 30 and opp_score <= 40):
        opp_score += 10
    elif(i == 'o' and opp_score >= 40):
        opp_score += 1
        r1 = opp_score - server_score
        if (r1 >= 2):
            print ("Opponent wins this game")
            exit()
    if(server_score > 40 and opp_score > 40 and server_score == opp_score):
        server_score = 40
        opp_score = 40
        print (server_score , opp_score)
    else:
        print (server_score , opp_score)  
