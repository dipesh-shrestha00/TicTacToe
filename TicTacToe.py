"""
Mini-max Tic-Tac-Toe Player
"""

import ttt_gui
import TTTgui as provided
#uncomment this part if u want to run in codeskulptor
# Set timeout, as mini-max can take a long time
#import codeskulptor
#codeskulptor.set_timeout(60)

# SCORING VALUES - DO NOT MODIFY
SCORES = {provided.PLAYERX: 1,
          provided.DRAW: 0,
          provided.PLAYERO: -1}

def mm_move(board, player):
    """
    Make a move on the board.
    
    Returns a tuple with two elements.  The first element is the score
    of the given board and the second element is the desired move as a
    tuple, (row, col).
    """
    winner = board.check_win()
    if winner != None:
        return SCORES[winner],(-1,-1)
    else:
        empty_squares = board.get_empty_squares()
        answer = (-1,(-1,-1))
        for square in empty_squares:
            board_copy = board.clone()
            board_copy.move(square[0],square[1],player)
            new_player = provided.switch_player(player)
            score = mm_move(board_copy,new_player)[0]
            if score * SCORES[player] == 1:
                return (score,square)
            elif score * SCORES[player] > answer[0]:
                answer = (score,square)
            elif answer[0] == -1:
                answer = (answer[0],square)
    return answer[0] * SCORES[player],answer[1]

def move_wrapper(board, player, trials):
    """
    Wrapper to allow the use of the same infrastructure that was used
    for Monte Carlo Tic-Tac-Toe.
    """
    move = mm_move(board, player)
    assert move[1] != (-1, -1), "returned illegal move (-1, -1)"
    return move[1]

# Test game with the console or the GUI.
# Uncomment whichever you prefer.
# Both should be commented out when you submit for
# testing to save time.

#provided.play_game(move_wrapper, 1, False)        
ttt_gui.run_gui(3, provided.PLAYERO, move_wrapper, 1, False)
