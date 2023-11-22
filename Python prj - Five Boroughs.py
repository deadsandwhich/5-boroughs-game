#Starts with a title and a preamble text.
#When the game is over, has a victory text.
#Includes “cheats” that are only to be used during the programming stage for testing purposes.
#Is entirely your work, & only uses the elements of coding that we talked about

#       5 boroughs, 2 player game, 10 soldiers each
#user goes first, pick base borough, computer pick one unoccupied one randomly as base
# random amount of turns alloted for total moves of both players
#rake tuns ptting soldiers in boroughs
#nce turns are up, players with higher amount of soldiers in borough wins
# if 0-0 it is a tie

## start off with some importing of things, because we need randomness   ;-;
import random



##intro cus why not, it looks less cluttered when i put together the pieces later on
def intro():
    spacing(10)
    print("It was unthinkable.")
    print("Living life as every other day,shattering to chaos in the next.")
    print("")
    print("Vengeful mushrooms descended from the sky above,")
    print("annihalating humans and lifeforms that stood in it's destructive path.")
    print("Greedy little fungi that stomped, smashed, and snatched")
    spacing(1)
    print("Now, it is up to you to protect all of new york from these invading mushrooms!")
    spacing(2)

##rules of the game I have yet to type out because it is so tiring
def rules():
    print("The rule of the the game: defend")
    print("If the amount of soldiers sent to one building is greater then that of the mushrooms")
    print("Than that building was won by ou and you get points porportional to the amount of soldiers that")
    print("were sent by you to the amount of soldiers sent by mushrooms")
    print("The cheat function will be avalable typing the word cheat when prompted during a move turn")
    spacing(3)




#total amount of rounds in the game at current time
total =0
#number of rounds played
roundsPlayed =0


#spacing tool for formatting
def spacing(num):
    for i in range(num):
        print("")


#thing for making divider line
def dotLine():
    print("......................................")


#invalid message thing so I don't have to type it out aganin and to make it look less cluttered
def invalid():
    print("*** Invalid input ***")
    print("")



##returns lengthof the thing
def bLength(anum):
    return len(borough[anum])

    
#buildings which also stores the num of soldiers in it
# if length of one row = 4, that means its a base
borough  = [["Manhattan",0,0],
             ["Brooklyn" ,0,0],
             ["Bronx",0,0],
             ["Queens" ,0,0],
             ["Staten Island",0,0]]


#define the cheat displaying format
def cheat():
    dotLine()
    spacing(2)
    print("The data is displayed in the format of : [ building name, # of ur soldiers, enemy soldiers]")
    spacing(2)
    for i in range(5):
        print(borough[i])
    print("")
    print("# of rounds played:", roundsPlayed)
    print("")
    print("# of rounds left:",total - roundsPlayed)
    print("")
    print("Player Base:        ",isItBase(1))
    print("")
    print("Enemy Mushroom Base:",isItBase(0))
    
    
    dotLine()

##wanna cheat? 
def wannaCheat():
    while True:
        try:
            wannaCheat = input("Do you want to cheat: (type cheat to cheat,anything else for no cheating)")
            if wannaCheat=="cheat":
                cheat()
                break
            else:
                print("Don't worry, you can always cheat next time!")
                break
        except ValueError:
            invalid()
            continue
        else:
            break
    

# create a function for placing soldiers in randomly
def computerMove():
    abuilding = random.randint(1,5)  #randomly choose building
    temp = borough[abuilding-1][2]    #not neccesary but easier for me to read
    borough[abuilding-1][2] = temp + 1 #incement by one without ++    T_T




##function for playermove
def playerMove():
    print("1. Manhattan")
    print("2. Brooklyn")
    print("3. The Bronx")
    print("4. Queens")
    print("5. Staten Island")

    
    
    ##you know a loop to check inputs are valid and stuff
    
    while True:
        try:
            theBuilding = int(input("Please enter the building number the soldier will be assigned to: "))
            if theBuilding<1 or theBuilding>5:
                invalid()
                continue
        except ValueError:
            invalid()
            print("Please re-enter building number:")
            continue
        else:
            break
    borough[theBuilding-1][1] = borough[theBuilding-1][1]+1
    spacing(3)
    






    
    
#3calculating the battle points using the ratio method
def battlePts():
    
    player = 0
    computer = 0
    for i in range(5):
        num =0
        if borough[i][1]>borough[i][2]:
           if borough[i][2]==0:
               num = borough[i][1]
           else:
               num = int( borough[i][1]/borough[i][2])
           if bLength(i)==4:
               num = num*2
           player = player+ num
           print(borough[i][0],":  ", "Player Wins (scored",num,"points)")
            
        if borough[i][1]<borough[i][2]:
            if borough[i][1]==0:
               num = borough[i][2]
            else:
               num = int(borough[i][2]/borough[i][1])
            if bLength(i)==4:
                num = num*2
            computer = computer +num
            print(borough[i][0],":  ", "Mushrooms Win (scored",num,"points)")
        if borough[i][1]==borough[i][2]:
            print("TIE. No points scored.")

        
        dotLine()
        spacing(5)
    print("Final Score: Mushrooms",computer," , Player",player)

    if computer > player:
        print("Mushrooms have won the battle, continuing there rampage across the earth . . . ")
        spacing(3)
        print("                (≖‿≖)")
        spacing(2)
    if player>computer:
        print("You win!!!!")
        spacing(3)
        print("                ( ˘▽˘)っ♨")
        spacing(2)
    if player== computer:
        print("A stalemate it seems . . . looks like both sides are tied.")
            
    

##not neccesary to seperate into a function, but just for readibility cus why not
def chooseBase():
    print("1. Manhattan")
    print("2. Brooklyn")
    print("3. The Bronx")
    print("4. Queens")
    print("5. Staten Island")
    while True:
        try:
            num= int(input("Please enter the building # you would like to select as your base: "))
            if num<1 or num >5:
                invalid()
                continue
        except ValueError:
            invalid()
            print("Please re-enter building number:")
            continue
        else:
            break
    borough[num-1].append(1)
    spacing(2)
    dotLine()


##function to randomly select an enemy base
def enemyBase():
    abuilding = random.randint(1,5)  #randomly choose building
    while len(borough[abuilding-1])==4:
        abuilding = random.randint(1,5)
        
    borough[abuilding-1].append(0)




##Checks if the boruogh is a base , returns base name when it is else returns not selected
def isItBase(num):
    for i in range(len(borough)):
        if len(borough[i])==4 and borough[i][3]==num:
            return borough[i][0]
    return "not selected"




    
###Start constructing game with the functions i have created in the above#######################
#lore

    
intro()
while True:
    try:
        enter = int(input("<Press 1 to start defense sequence>"))
        if enter!=1:
            invalid()
            continue
    except ValueError:
        invalid()
        print("Please enter 1 to start defense sequence>")
        continue
    else:
        break       

spacing(5)
rules()
spacing(4)
print("- -- - -- - -- - -- - -- - -- - -- - -- - -- - -- - -- - -- -")
print("                   * The Placement*       ")
spacing(2)

total = 10

for i in range(10):
    playerMove()
    spacing(2)
    roundsPlayed =1+roundsPlayed
    computerMove()
    wannaCheat()
    spacing(2)

spacing(5)

for i in range(2):
    spacing(3)
    print(". . ")
    spacing(2)
    print(".")
    
spacing(5)
print("Now for both of you to choose the base. Player first:")
dotLine()
spacing(1)

chooseBase()
spacing(3) 
dotLine()
enemyBase()

spacing(5)
print("- -- - -- - -- - -- - -- - -- - -- - -- - -- - -- - -- - -- -")
print("                   * The Building*       ")
spacing(3)
numOfTurns = random.randint(10,25)
total = numOfTurns+total


for i in range(numOfTurns):
    playerMove()
    spacing(2)
    roundsPlayed =1+roundsPlayed
    computerMove()
    wannaCheat()
    spacing(2)

    
spacing(7)
dotLine()
print("- -- - -- - -- - -- - -- - -- - -- - -- - -- - -- - -- - -- -")
print("                   * The final Battle*       ")


battlePts()
spacing(5)
print("And thus, that concludes this saga , for now")
spacing(2)
print("- -- - -- - -- - -- - -- - -- - -- - -- - -- - -- - -- - -- -")
print("                   * Fine*       ")
