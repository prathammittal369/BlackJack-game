print("************************************************************************************************************************************************Welcome to BlackJack Game***********************************************************************************************************************************************")
import random

'''
    A/Ace =11 or 1
    Queen=10
    King=10
    Jack=10
    
    And declaration of all no. in numbers list
'''
numbers=["A",2,3,4,5,6,7,8,9,10,"K","Q","J"]
ace=[1,11]



def choosing_no(player_dealer_card):
    if( type(player_dealer_card) == type(1) ):
        return player_dealer_card
    else:
        if(player_dealer_card=="K"):
            return 10;
        elif(player_dealer_card=="J"):
            return 10;
        elif(player_dealer_card=="Q"):
            return 10;
        elif(player_dealer_card=="A"):
            return "1/11";


play_again="Y"
while(play_again=="Y"):
    #1st card of player
    player_1_card=numbers[ random.randint(0,len(numbers) -1) ]

    #2nd card of player
    player_2_card=numbers[ random.randint(0,len(numbers) -1) ]
            
    # 1st no. of player
    player_1_no=choosing_no(player_1_card)

    # 2nd no. of player 
    player_2_no=choosing_no(player_2_card)

    print(f"So you got {player_1_card} card and {player_2_card} card")


    # Player total points
    def player_ace_card(ace_1,ace_2):
        if(ace_1=="1/11"):
            ace_1=int(input("So as you know you got Ace card what do you wanna select 1 or 11?"))
            return ace_1
        if(ace_2=="1/11"):
            ace_2=int(input("So as you know you got Ace card what do you wanna select 1 or 11?"))
            return ace_2


    if(player_1_no=="1/11"):
        player_1_no=player_ace_card(player_1_no,player_2_no)
    elif(player_2_no=="1/11"):
        player_2_no=player_ace_card(player_1_no,player_2_no)
        
    player=player_1_no + player_2_no




    # 1st card of dealer 
    dealer_1_card=numbers[ random.randint(0,len(numbers) -1) ]

    # 2nd card of dealer
    dealer_2_card=numbers[ random.randint(0,len(numbers) -1) ]

    #1st no. of dealer
    dealer_1_no=choosing_no(dealer_1_card)

    #2nd no. of dealer 
    dealer_2_no=choosing_no(dealer_2_card)

    print(f"And dealer got {dealer_1_card} card and one card")

    # dealer total points
    def dealer_ace_card(dealer_ace_1,dealer_ace_2):
        if(dealer_ace_1=="1/11"):
            dealer_ace_1=ace[random.randint(0,1)]
            return dealer_ace_1
        if(dealer_ace_2=="1/11"):
            dealer_ace_2=ace[random.randint(0,1)]
            return dealer_ace_2
                
    if(dealer_1_no=="1/11"):
        dealer_1_no=dealer_ace_card(dealer_1_no,dealer_2_no)
    elif(dealer_2_no=="1/11"):
        dealer_2_no=dealer_ace_card(dealer_1_no,dealer_2_no)
    dealer_ace_card(dealer_1_no,dealer_2_no)
    dealer=dealer_1_no + dealer_2_no
    


    # asking for choosing cards from player
    choose_card_by_player="Y"
    while(choose_card_by_player=="Y"):
        choose_card_by_player=str(input("Do you wan to choose or take cards?\nY for yes and N for no "))
        choose_card_by_player=choose_card_by_player.upper()
        if(choose_card_by_player=="Y"):
            player_1_card=numbers[ random.randint(0,len(numbers) -1) ]
            print(f"So you got {player_1_card} card")
            player_1_no=choosing_no(player_1_card)
            if(player_1_no=="1/11"):
                player_1_no=player_ace_card(player_1_no,0)
            player+=player_1_no
        if(player>21):
            print("It's a burst!!\nYou lose :(")
            break
    if(player>21):
        break


    # asking for choosing cards from dealer
    # 0 for yes and 1 for no
    def choose_card_by_dealer():
        return random.randint(0,1)
    
    count1=0
    count=0
    
    # if the dealer want's to take card
    if(dealer<17):
        while(dealer<17):
            if(count1==0):
                print(f"Dealer's second card is {dealer_2_card}")
                count1+=1
            dealer_1_card=numbers[ random.randint(0,len(numbers) -1) ]
            print(f"So dealer has choosen the cards and got {dealer_1_card} card")
            dealer_1_no=choosing_no(dealer_1_card)
            if(dealer_1_no=="1/11"):
                dealer_1_no=dealer_ace_card(dealer_1_no,0)
            dealer+=dealer_1_no
    elif(21>dealer>=17):
        while(21>dealer>=17):
            if(count==0):
                print(f"Dealer's second card is {dealer_2_card}")
                count+=1
            if(choose_card_by_dealer()==0): # yes
                dealer_1_card=numbers[ random.randint(0,len(numbers) -1) ]
                print(f"So dealer has choosen the cards and got {dealer_1_card} card")
                dealer_1_no=choosing_no(dealer_1_card)
                if(dealer_1_no=="1/11"):
                    dealer_1_no=dealer_ace_card(dealer_1_no,0)
                dealer+=dealer_1_no
            else:
                break
    if(dealer>21):
        print("You Win!!")
    elif(player>dealer):
        print("You Win!! :)")
    elif(player==dealer):
        print("It's a draw :(")
    else:
        print("You lose :(")
    play_again=input("Wanna play again?:)\nY for yes N for no ")
    play_again=play_again.upper()