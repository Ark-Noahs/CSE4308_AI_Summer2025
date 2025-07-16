# noe chairez 
# 1002018540
# CSE4308_002 --> Summer 2025 Course 

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



'''



import sys #help us use command line args 

#funct to handle depth.......................................
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
        print("ERROR: missing arguments, currently < 2 args")
        sys.exit(1)

    try:
        #attempt to set red and blue to args...
        num_red  = int(args[0])
        num_blue = int(args[1])
    except ValueError:
        print("ERROR: issues with setting red or blue w/ vars in 'parse_the_args()' funct")
        sys.exit(1)

    #below are defaults.....
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
            print("ERROR: issue with {args[i]}")
        i = i + 1   #increment and look at next value 
    
    return num_red, num_blue, version, first_player, depth 



if __name__ == "__main__":

    #passing command line to be processed into individual vars....
    red,blue,version,first_player,depth = parse_the_args() #funct go on right side in python

    print("DEBUG below remove when done....")
    print(f"red marbles: {red}")
    print(f"blue marbles: {blue}")
    print(f"version being played: {version}")
    print(f"first turn goes to: {first_player}")
    print(f"depth limit: {depth} NOTE: this is part of extra credit if attempting it")
    print(f"")
    