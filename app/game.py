import random
player_1 = ' '
player_2 = ' '

def clear_game_boad():
    game_board = [' ']*10
    show_game_board(game_board)
    return game_board

def check_number_of_players():
    players = input("Select number of players(1 or 2): ")

    if players == '1' or players == '2':
        return players
    else:
        print("Please enter a valid input.")
        return check_number_of_players()

def show_game_board(game_board):
    print('             |               |       ')
    print("     "+game_board[1]+"       |       "+game_board[2]+"       |       "+game_board[3])
    print("-----------------------------------------")
    print('             |               |       ')
    print("     "+game_board[4]+"       |       "+game_board[5]+"       |       "+game_board[6])
    print("-----------------------------------------")
    print('             |               |       ')
    print("     "+game_board[7]+"       |       "+game_board[8]+"       |       "+game_board[9])

def show_game_end():
    print("--------------------------------------------")
    print("Game Over. Thanks for playing.")

def check_for_players():
    value = input("Please choose X or O: ").upper()
    
    if value == 'X':
       return ('X','O')
    elif value == 'O':
        return ('O','X')
    else:
        print ("Please enter a valid input.")
        return check_for_players()

def check_game_board(game_board,pos):
    if game_board[pos] == ' ' :
        return True
    elif pos in range (1,10):
        print('Please enter postion between 1 to 9')
        return False
    else:
        print("Invalid input")
        return False

def check_game_board_for_computer(game_board,player_1,player_2):
    player_position = []
    computer_possible_position = []
    computer_position = []
    player_block_loc = None
   
    for _ in range(1,10):
        if game_board[_] == player_1:
            player_position.append(_)
        elif game_board[_] == player_2:
            computer_position.append(_)
        else:
            computer_possible_position.append(_)
    
    if not computer_position:
        return random.choice(computer_possible_position)
    else:
        player_block_loc = get_computer_position(computer_position,game_board)
        if len(player_block_loc) >0 :
            print(player_block_loc)
            return player_block_loc[0]
        else:
            player_block_loc = get_computer_position(player_position,game_board)
            if len(player_block_loc) >0 :
                return player_block_loc[0]
            else:
                return random.choice(computer_possible_position)
    
def get_computer_position(check_list,game_board):
    
    new_possible_loc = []
    win_1 = [[1,2,3],[4,5,6],[7,8,9]]
    win_2 = [[1,4,7],[2,5,8],[3,6,9]]
    win_3 = [[1,5,9],[3,5,7]]
    
    if not new_possible_loc:
        for _ in win_1:
            if len(list(set(_).intersection(check_list))) > 1:
                loc = Diff(_,check_list)
                if(game_board[loc[0]] == ' '):
                    new_possible_loc = loc
                    break

    if not new_possible_loc:
        for _ in win_2:
            if len(list(set(_).intersection(check_list))) > 1:
                loc = Diff(_,check_list)
                if(game_board[loc[0]] == ' '):
                    new_possible_loc = loc
                    break
    
    if not new_possible_loc:
        for _ in win_3:
            if len(list(set(_).intersection(check_list))) > 1:
                loc = Diff(_,check_list)
                if(game_board[loc[0]] == ' '):
                    new_possible_loc = loc
                    break
    
    return new_possible_loc

def Diff(li1, li2):
    return (list(set(li1) - set(li2)))

def play_with_computer():
    player_score = []
    conputer_score = []

    print("-------------- Game Staring with computer ---------------")
    game_board=clear_game_boad()
    print(" ")
    player_1 , player_2 = check_for_players()
    print(f"Player 1 = {player_1} and Computer = {player_2}")
    print(" ")

    for _ in range(1,10):
        if _%2 != 0:
            print("Player 1 it is your turn. Enter Q to quit.")
            pos = input("Please enter the postion where you want to place: ")
            print(" ")
            if pos.upper() == 'Q':
                break
            play_game(game_board,player_1,pos)
            if check_win_condition(game_board):
                print ("Congratulation ! You won !")
                player_score.append(1)
                conputer_score.append(0)
                break
        else:
            print("Wait for Computer to play.")
            pos = check_game_board_for_computer(game_board,player_1,player_2)
            play_game(game_board,player_2,str(pos))
            if check_win_condition(game_board):
                print ("Computer won !")
                conputer_score.append(1)
                player_score.append(0)
                break                
    
    if not player_score and not conputer_score:
        player_score.append(0)
        conputer_score.append(0)
        print("Game Draw!!")

    show_game_end()
    return (player_score,conputer_score)

def play_with_opponent():
    player1_score = []
    player2_score = []
    print("-------------- Game Staring with opponent ---------------")
    game_board=clear_game_boad()
    print(" ")
    player_1 , player_2 = check_for_players()
    print(f"Player 1 = {player_1} and Player 2 = {player_2}")
    print(" ")
    for _ in range(1,10):
        if _%2 != 0:
            print("Player 1 it is your turn. Enter Q to quit.")
            pos = input("Please enter the postion where you want to place: ")
            print(" ")
            if pos.upper() == 'Q':
                break
            play_game(game_board,player_1,pos)
            if check_win_condition(game_board):
                print ("Congratulation ! Player 1 has won the game.")
                player1_score.append(1)
                player2_score.append(0)
                break
        else:
            print("Player 2 it is your turn. Enter Q to quit.")
            pos = input("Please enter the postion where you want to place: ")
            print(" ")
            if pos.upper() == 'Q':
                break
            play_game(game_board,player_2,pos)
            if check_win_condition(game_board):
                print ("Congratulation ! Player 2 has won the game.")
                player2_score.append(1)
                player1_score.append(0)
                break 
    
    if not player1_score and not player2_score:
        player1_score.append(0)
        player2_score.append(0)
        print("Game Draw!!")

    show_game_end()
    return (player1_score,player2_score)

def play_game(game_board,player,pos):
    while not check_game_board(game_board, int(pos)):
        pos = input("Please enter the postion where you want to place: ")
    while check_game_board(game_board, int(pos)):
        place_player_move(game_board,int(pos),player)
        break

def place_player_move(game_board,pos,value):
    game_board[pos] = value
    show_game_board(game_board)

def check_win_condition(game_board):
    if game_board[1] == game_board[2] == game_board[3] and game_board[1] == game_board[2] == game_board[3] != ' ':
        return True
    elif game_board[4]==game_board[5]==game_board[6] and game_board[4]==game_board[5]==game_board[6] != ' ':
        return True
    elif game_board[7] == game_board[8] == game_board[9] and game_board[7] == game_board[8] == game_board[9] != ' ':
        return True
    elif game_board[1] == game_board[4] == game_board [7] and game_board[1] == game_board[4] == game_board [7] != ' ':
        return True
    elif game_board[2] == game_board[5] == game_board [8] and game_board[2] == game_board[5] == game_board [8] != ' ':
        return True
    elif game_board[3] == game_board[6] == game_board [9] and game_board[3] == game_board[6] == game_board [9] != ' ':
        return True
    elif game_board[1] == game_board[5] == game_board[9] and  game_board[1] == game_board[5] == game_board[9] != ' ':
        return True
    elif game_board[3] == game_board[5] == game_board[7] and  game_board[3] == game_board[5] == game_board[7] != ' ':
        return True
    else:
        return False

def start_tic_tac_toe():
    players = check_number_of_players()

    if players == '1':
        
        player_score, computer_score = play_with_computer()
        return (player_score, computer_score,1)
        
    elif players == '2':
        
        player1_score, player2_score = play_with_opponent()
        return (player1_score, player2_score,2)
   




