##import tools to generate random number##
import math
import random
def autoplay(health):
    #Outputs and commented out for faster computation
    win=0
    gold=0
    #whole program within while loop for health, as long as health is > 0, the game will contiue taking turns until gold limit is reached, health is 0, or instant death occurs at (4) (also health =0)
    while health>0:
       #tart game routine, establish initial values for "gold" and "health"
        health=health
        #print("Gold:",gold)
        #print("Health:", health)
        #print("Rolling the die!")

        rand_num=math.floor(10*random.random())+1
        #print(f"Health:{health} Gold:{gold}")
        #print(f"Rolled a {rand_num}") 
        
        
        if rand_num==7 or rand_num==1:
            rand_gold=math.floor(5*random.random()+1)
            rand_gold=rand_gold*100000
            #print(f"Gold Found:{rand_gold}")
            gold=gold+rand_gold
            ##check to see if user has three or more gold##
            if gold >=500000:
                #print(f"Ye found {rand_gold} gold!")
                #print(f"Gold: {gold}")
                #print(f"Health: {health}")  
                #*****Flag variable to mark a win (set to 0 still if loss)******
                win=1
                #print("***********WIN!***********")
                #print(f"Health:{health} Gold:{gold}")
            #else:
                #print(f"Ye found {rand_gold} gold!")
                #print(f"Gold: {gold}")
                #print(f"Health: {health}")
           
    

    ## You roll a 4.##
    ##Killed instantly. 5 is subtracted from health. Game ends because health is <=1##    
        elif rand_num==4:
            health=0
            #print("You were eaten by a monster of the deep.")
            #print("You are out of health")
            #print(f"Gold: {gold}")
            #print(f"Health: {health}")
            #print("***********LOSS!***********")
            #print(f"Health:{health} Gold:{gold}")
            win=0
            
        ## Your roll anything else
        ##Health is subtracted.##
        ##Amount subtracted is equal to roll, if health is >=1 player gets a new turn. 
        ## If not, the game ends.##
        else:
            health=health-rand_num
            if health<=0:
                health=0
                #print("You died of scurvy. Eat a vegetable and try again!")
                #print("You are out of health")
                #print(f"Gold: {gold}")
                #print(f"Health: {health}")
                #print("************LOSS!************")
                #print(f"Health:{health} Gold:{gold}")
                win=0
                
                
            #else:
                #print(f"You were struck by an an agressive seabird and lost {rand_num} health.")
                #print("Ouch!")
                #print(f"Gold: {gold}")
                #print(f"Health: {health}")
        #***For each game playthrough, if the win flag variable reaches 1, the function (autoplay(health) returns that flag. )   
        if win==1:
            return win
    
def level_1():
    cust_mon=[]
    def_mon=["the queen's navy", "bacteria","an agressive seabird", "a monster of a the deep", "a giant seal", "a poison snail", "Hank Hill", "slime mold", "Cthulu", "five beans" ]
##Start game routine, establish initial values for "gold" and "health"
    print("So you seek the treasure rumored to be in excess of 500000 gold!?") 
    print("Well...with luck you may be on the path to riches but...")
    print("For now you have but the clothes on your back.")
    health=20
    gold=0
    r=1
    while r!=0:
        print("Would you like to create a custom monster list? Enter 1 to create one or 0 to use default monster list.")
        create=int(input(">"))
        if create==1:
            i=0
            r=0
            print("Enter ten monsters below.")
            while i<10:
                monster=input(">")
                cust_mon.append(monster)
                i+=1
            while i>0:
                print(cust_mon[i-1])
                i-=1
            mon=cust_mon
        elif create==0:
            mon=def_mon
            r=0
        else: 
            print("Sorry, that wasn't a valid selection. Try again.")
    print("Gold:",gold)
    print("Health:", health)
    print("Roll the die!")
    

    

    print("Enter any value to roll, or enter 0 to return to the main menu.")
    
    x=1
    while x !=0:
        roll=int(input(">"))
        if roll==0:
            x=0
            break
        else:
            rand_num=math.floor(10*random.random())+1
            print(f"Rolled a {rand_num}") 
            
    
    ##Random number is generated.##
    ##Here we establish what happens based on the number rolled##
    ##For a 1, player gets a random amount of gold, stored in "rand_gold"##
    ##"rand_gold" is added to "gold"##

            
        

        if rand_num==7 or rand_num==1:
            rand_gold=math.floor(5*random.random()+1)
            rand_gold=rand_gold*100000
            gold=gold+rand_gold
              ##check to see if user has three or more gold##
            if gold >=500000:
                x=0
                print(f"Ye found {rand_gold} gold!")
                print(f"Gold: {gold}")
                print(f"Health: {health}")
                print("Congratulations Treasure Seeker! You won!!")  
                print("Returning to Main Menu")
            else:
                print(f"Ye found {rand_gold} gold!")
                print(f"Gold: {gold}")
                print(f"Health: {health}")
                print("Enter any value to roll, or enter 0 to return to the main menu.")
           
      

    ## You roll a 4.##
    ##Killed instantly. 5 is subtracted from health. Game ends because health is <=1##    
        elif rand_num==4:
            health=0
            x=0
            y=math.floor((rand_num-1)*random.random())+1
            print(f"You were killed by {mon[y-1]}.")
            print("You are out of health")
            print(f"Gold: {gold}")
            print(f"Health: {health}")
            print("Returning to Main Menu")
        ## Your roll anything else
        ##Health is subtracted.##
        ##Amount subtracted is equal to roll, if health is >=1 player gets a new turn. 
        ## If not, the game ends.##
        else:
            health=health-rand_num
            if health<=0:
                health=0
                x=0
                y=math.floor((rand_num-1)*random.random())+1
                print(f"You were slain by {mon[y-1]}. Try again!")
                print("You are out of health")
                print(f"Gold: {gold}")
                print(f"Health: {health}")
                print("Returning to Main Menu")
                
                
            else:
                print(f"You were attacked by {mon[rand_num-1]} and lost {rand_num} health.")
                print("Ouch!")
                print(f"Gold: {gold}")
                print(f"Health: {health}")
                print("Enter any value to roll, or enter 0 to return to the main menu.")
                
    ##Menu from HW#2 as a function    
def menu():
## 1. ASCII Title Art
    print(r"""
          _______                               
         |_______|                             
            | |_ __ ___  __ _ ___ _   _ _ __ ___  
            | | '__/ _ \/ _` / __| | | | '__/ _ \ 
            | | | |  __/ (_| \__ \ |_| | | |  __/ 
            \_/_|  \___|\__,_|___/\__,_|_|  \___| 
             _____           _                      
            /  ___|         | |                     
            \ `--.  ___  ___| | _____ _ __          
             `--. \/ _ \/ _ \ |/ / _ \ '__|         
            /\__/ /  __/  __/   <  __/ |            
            \____/ \___|\___|_|\_\___|_|            
                                                    
                                            """)

    print('Welcome Traveler!')
    print()
    print("This is Treasure Seeker, a game where you may find hidden booty...")
    print("or perish at the mercy of the sea!")
    print('To continue, please make a selection from the menu.')
    print()
    print('0 - Quit')
    print('1 - Play Treasure Seeker')
    print('2 - Autoplay Probability Simulation')
    
            
            


    
re=1

while re !=0:
    menu()
    choice = int(input(">"))
    if choice==1:
        
        level_1()
        print(r"""
              
              """)
    elif choice==0:
        print('Until next time, Traveler.')
        re=0
    
    elif choice==2:
        #gather number of playthroughs to simulate
        print("Autoplay mode. How many playthroughs would you like to simulate?")
        plays=int(input(">"))
        ##store "plays" and create another equal variable that can be -1 from for each run through the loop. 
        games=plays
        #gather user set health amount to use in each turn
        print("Enter starting health for each playthrough")
        health=int(input(">"))
        print("Running Simulation.")
        ##set initial win counter to 0
        wins=0
        #While loop to keep running the autoplay function as many times as specified by user in "plays" variable
        while games>0:
            #print("***********************************")
            #print(f"Wins: {wins}")
            #print("***********************************")
            #call "autoplay()" and pass user input health to it. Set output of "autoplay(health)" to win variable in the main calling routine. 
            win=autoplay(health)
            #remove 1 from games each time through the loop to ensure it runs input(games) number of times
            games=games-1
            #if flag 1 is returned in a playthrough, add one to the variable wins
            if win==1:
                wins=wins+1
                #ompute percentage of total plays is a win
        win_per=wins/plays*100
     
        print(f"The simulation of {plays} consecutive playthroughs, each with a starting health of {health} is complete.")
        print(f"The simulation resulted in a win {win_per} % of the time.")
        
    else:
        print('Sorry that is not a valid selection. Try Again. ')
        print(r"""
              
              """)




