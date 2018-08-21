from game import start_tic_tac_toe
player1_score = []
player2_score = []
draw_score = []

def start_game():
   
    first_player_score,second_player_score,game_type = start_tic_tac_toe()
    answer = input("Press any key to continue the game. Select Q to quit the game.").upper()
    while answer == 'Q':
        display_score(first_player_score,second_player_score,game_type)
    else:
        display_score(first_player_score,second_player_score,game_type)
        return start_game()

def display_score(first_player_score,second_player_score,game_type):
    
    player1_score.append(sum(first_player_score))
    player2_score.append(sum(second_player_score))

    if sum(second_player_score) and sum(second_player_score) == 0:
        draw_score.append(1)
    
    print("                   Win ")
    print(f"Player 1:           {sum(player1_score)}")

    if game_type == 1:
        print(f"Computer :          {sum(player2_score)}")
    if game_type == 2:
        print(f"Player 2:           {sum(player2_score)}")

    print(f"Draw : {sum(draw_score)}")
    print(" ")


start_game()

    