# noe chairez 
# 1002018540
# CSE4308_002 --> Summer 2025 Course --> due on july 30th 

'''
Program has use play against computer where each take a turm removing marble. Has two versions (standard game and mis�re)
Rules:
    -each player can remove 1 or 2 marbles 
    -standard version: loser loses game when pile is empty on their turn 
    -mis�re version: winner wins whenpile is empty on their turn //^^opposite of 



*MUST be able to run w/ following arguments from command line:
                red_blue_nim.py <num-red> <num-blue> [-version] [-first-player] [-d <depth>]

                <num-red>      =     sets num of red marbles 
                <num-blue>     =     sets num of blue marbles 
                -<version>     =     *default: player loses if pile is empty  <--no input 
                                     *-m     : misere version

                -<first-player>=     *default: -h will allow user to go first
                -d <depth>     =     EXTRA CREDIT OPTIONAL! --> use for depth limit search

*   -On user turn: enter input 
    -on Computer turn must use MinMax algorithm w Apha-Beta Pruning
            -->NOTE: i got the algorithm code from GeeksforGeeks.org <----!
                     HERE IS DIRECT LINK: https://www.geeksforgeeks.org/dsa/minimax-algorithm-in-game-theory-set-4-alpha-beta-pruning/


'''








import sys #help us use command line args 

#minmax function w/ alpha beta pruning from GeeksforGeeks.org link is at top of file ^ .......
def minmax(red, blue, is_maximizing, alpha, beta, version, depth=None, current_depth=0):
    
    #The game is over when either pile is empty.....
    if red == 0 or blue == 0:
        score = (2 * red) + (3 * blue) 

        if version == "misere":
            result = score      #positive score --> WINNER
        else:
            result = -score     #negative score --> LOSER

        return (result, None)
    
    if depth is not None:            #verifies depth limit
        if current_depth == depth:   #if depth limit is reached return score
            return (0, None)
    
    #gets us list of moves from current........
    move = []

    if red >= 2:
        move.append(('R', 2))   #rm 2 red marbles
    if blue >= 2:
        move.append(('B', 2))   #rm 2 blue marbles

    if red >= 1:
        move.append(('R', 1))   #rm 1 red marble
    if blue >= 1:
        move.append(('B', 1))   #rm 1 blue marble 

    #reverse move order for misere version........
    if version == "misere":
        move.reverse()
    
    best_move = None #var to hold best move found


    #MAXimizing computer............
    if is_maximizing:
        max_eval = float('-inf')   #start w lowest possible score
    
        #loop through all possible move....
        for pile, count in move:
            new_red = red
            new_blue = blue

            #apply the move....
            if pile == 'R':
                new_red = new_red - count
            elif pile == 'B':
                new_blue = new_blue - count 

            #recursive call to minmax(human ).....
            eval_score, _ = minmax(new_red, new_blue, False, alpha, beta, version, depth, current_depth + 1) 

            #update the max evaluation if the move is better....
            if eval_score > max_eval:
                max_eval = eval_score
                best_move = (pile,count)
            

            #alpha beta pruning-->update alpha....
            if eval_score > alpha:
                alpha = eval_score
            

            #if beta is <= alpha then prune...
            if beta <= alpha:
                break

        return (max_eval, best_move)
    
    else:   # <----------------------MINimizing player(Human)....
        
        min_eval = float('inf')   #start w highest score possible

        #loop through each possible move....
        for pile, count in move:
            new_red = red
            new_blue = blue

            #apply the move....
            if pile == 'R':
                new_red = new_red - count 
            elif pile == 'B':
                new_blue = new_blue - count 
            

            #recursion: call minmax for the computer turn now....
            eval_score, _ = minmax(new_red, new_blue, True, alpha, beta, version, depth, current_depth + 1)

            #update min evaluation if this move is better..
            if eval_score < min_eval:
                min_eval = eval_score
                best_move = (pile, count)

            #alpha beta pruning, update beta....
            if eval_score < beta:
                beta = eval_score 

            #if beta is <= alpha then prune...
            if (beta <= alpha) :
                break
        return (min_eval, best_move)            

#funct to handle the hooman turn.....
def hand_of_hooman(red, blue):
    while True:
        #get pile input
        pile = input("Which pile do you want to take from? (R/B): ").strip().upper()

        if pile not in ['R', 'B']:   #use list, same as pile !- 'R' and pile != 'B' 
            print("ERROR: enter valid input (R/B)")
            continue

        #verifies that the pile selected has something to rm 
        if pile == 'R':    #nest the if's bc got error w/ placement of 'max_remove' 
            if red == 0:
                print("ERROR: No more red marbles in the pile")
                continue
            max_remove = red
        else:                   # pile == 'B'
            if blue == 0:
                print("ERROR: No more blue marbles in the pile")
                continue
            max_remove = blue

        #select the num of marbles to remove 1 or 2
        try:
            count = int(input("enter the num of mrbles you want to remove(1 or 2): ").strip())
        except ValueError:
            print("ERROR:enter a valid number (1 or 2)")
            continue

        #  verify that within range and marbles are removable.....
        if count not in [1, 2] or count > max_remove:
            print(f"ERROR:You can only take 1 or 2 marbles, and no more than {max_remove} from the {pile} pile.")
            continue

        #update marble counts.....
        if pile == 'R':
            red = red - count 
        else:
            blue = blue - count

        return red, blue

#funct to handle the final results
def endGame(red, blue, version ,current_player):
    print("\n!!!!!!!!!!!!!!! GAME OVER !!!!!!!!!!!!!!!!!")
    print(f"remaining marbles:\nRed:{red}\nBlue:{blue}")

    #red gets 2 pts every marble and blue gets 3 per 
    score = (2 * red) + (3 * blue)

    if version == "standard":               #standard version results
        #player w last move before end game wins in standard 

        if current_player == "human":
            not_LOZER = "computer"
        else:
            not_LOZER = "human"
        print(f"Winner: {not_LOZER}\nThe Grand Master wins with a lump sum of {score} points!!!")
        
    else:                                   #Misere Version results 
        
        #player who goes next at end game wins 
        not_LOZER = current_player 
        print(f"Winner: {not_LOZER}\nThe Grand Master wins with a lump sum of {score} points!!")




#funct to handle depth EXTRA CREDIT......................................
def handle_depth(args):

    try:
        depth = int(args) #attempt to make into int
        return depth 
    except ValueError:
        print("ERROR: coudnt convert depth to an int in funct 'handle_depth()' ")
        sys.exit(1)
   

#funct to parse the command line args........................
def parse_the_args():
    args = sys.argv[1:]  #ignore the first arg which is file name by starting on element 1

    #need to know num of red and blue in order to run program everything else has a default ....
    if len(args) < 2:
        print("ERROR: missing arguments, currently < 2 args IF statement in 'parse_the_args' function")
        sys.exit(1)

    try:
        #attempt to set red and blue to args...
        num_red  = int(args[0])
        num_blue = int(args[1])
    except ValueError:
        print("ERROR: issues with setting red or blue w/ vars in 'parse_the_args()' funct")
        sys.exit(1)

    #below are the defaults..........
    version      = "standard"
    first_player = "computer"
    depth        = None        #OPTIONAL FOR EXTRA CREDIT

    #below will look for version, first_player from command line 
    
    i = 2   #command line got 6 args but ignored first so 5 but already processed first 2 so setting i @ 2

    while i < len(args):
        if args[i] == '-m':
            version = "misere"    #set the games version to misere
        elif args[i] == '-h':
            first_player = 'human'#sets the first player to the human/user
        elif args[i]== '-d':
            i = i + 1  #if -d is entered then look at next element to view depth 
            if i < len(args):
                depth = handle_depth(args[i])
            else:
                print(f"ERROR: issue in while loop of 'parse_the_args' ")
                sys.exit(1)
        else:
            print("ERROR: issue with {args[i]} in 'parse_the_args' ")
        i = i + 1   #increment and look at next value 
    
    return num_red, num_blue, version, first_player, depth 

    
def start_debug(red, blue, version, first_player, depth):
    print("The Game has begun, here are the following vars from your input")    #debug 
    print(f"red marbles: {red}")
    print(f"blue marbles: {blue}")
    print(f"version being played: {version}")
    print(f"first turn goes to: {first_player}")
    print(f"depth limit: {depth} NOTE: this is part of extra credit if attempting it\n")


if __name__ == "__main__":

    #passing command line to be processed into individual vars....
    red,blue,version,first_player,depth = parse_the_args() #funct go on right side in python

    #funct to verify that args are properly put into their vars 
    start_debug(red, blue, version, first_player, depth )
    
    current_player = first_player    #player one is set to whoever gets first turn in arg^


    #GAME FUNCTIONALLITY STARTS HERE....
    print("***********GAME STARTS************")

    while red > 0 and blue > 0:
        print("\n  ----->CURRENT MARBLES<----- ")
        print(f"red marbles: {red}")
        print(f"Blue marbles: {blue}")
        print(f"It is your move: {current_player}")

        #hooman turn............
        if current_player == "human":
            red,blue = hand_of_hooman(red,blue) #call hooman function to handle user input
        
        #Computers move.....
        else:      
            _, move = minmax(red, blue, True, float('-inf'), float('inf'), version, depth) #_ is seen as throw away var and being ignored  
            pile, count = move  
            print(f"The computers decision: Takes {count} marbles from {pile} pile")


            if pile == 'R':
                red = red - count 
            else: 
                blue = blue - count 
        
        if current_player == "computer":    #swapping players turn 
            current_player = "human"
        else:
            current_player = "computer"


    #funct to show results and determine winner based off of the versiom played...
    endGame(red, blue, version, current_player)
         



