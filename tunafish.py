import chess
import chess.svg
import chess.polyglot
import random
import math

from typing import List

def get_piece_value(piece: object, i: int, j: int) -> int:
    pawn_eval_white = [
        [0.0,  0.0,  0.0,  0.0,  0.0,  0.0,  0.0,  0.0],
        [5.0,  5.0,  5.0,  5.0,  5.0,  5.0,  5.0,  5.0],
        [1.0,  1.0,  2.0,  3.0,  3.0,  2.0,  1.0,  1.0],
        [0.5,  0.5,  1.0,  2.5,  2.5,  1.0,  0.5,  0.5],
        [0.0,  0.0,  0.0,  2.0,  2.0,  0.0,  0.0,  0.0],
        [0.5, -0.5, -1.0,  0.0,  0.0, -1.0, -0.5,  0.5],
        [0.5,  1.0, 1.0,  -2.0, -2.0,  1.0,  1.0,  0.5],
        [0.0,  0.0,  0.0,  0.0,  0.0,  0.0,  0.0,  0.0]
    ];

    pawn_eval_black = pawn_eval_white[::-1]

    knight_eval_white = [
        [-5.0, -4.0, -3.0, -3.0, -3.0, -3.0, -4.0, -5.0],
        [-4.0, -2.0,  0.0,  0.0,  0.0,  0.0, -2.0, -4.0],
        [-3.0,  0.0,  1.0,  1.5,  1.5,  1.0,  0.0, -3.0],
        [-3.0,  0.5,  1.5,  2.0,  2.0,  1.5,  0.5, -3.0],
        [-3.0,  0.0,  1.5,  2.0,  2.0,  1.5,  0.0, -3.0],
        [-3.0,  0.5,  1.0,  1.5,  1.5,  1.0,  0.5, -3.0],
        [-4.0, -2.0,  0.0,  0.5,  0.5,  0.0, -2.0, -4.0],
        [-5.0, -4.0, -3.0, -3.0, -3.0, -3.0, -4.0, -5.0]
    ];

    knight_eval_black = knight_eval_white[::-1]

    bishop_eval_white = [
        [ -2.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -2.0],
        [ -1.0,  0.0,  0.0,  0.0,  0.0,  0.0,  0.0, -1.0],
        [ -1.0,  0.0,  0.5,  1.0,  1.0,  0.5,  0.0, -1.0],
        [ -1.0,  0.5,  0.5,  1.0,  1.0,  0.5,  0.5, -1.0],
        [ -1.0,  0.0,  1.0,  1.0,  1.0,  1.0,  0.0, -1.0],
        [ -1.0,  1.0,  1.0,  1.0,  1.0,  1.0,  1.0, -1.0],
        [ -1.0,  0.5,  0.0,  0.0,  0.0,  0.0,  0.5, -1.0],
        [ -2.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -2.0]
    ];

    bishop_eval_black = bishop_eval_white[::-1]

    rook_eval_white = [
        [  0.0,  0.0,  0.0,  0.0,  0.0,  0.0,  0.0,  0.0],
        [  0.5,  1.0,  1.0,  1.0,  1.0,  1.0,  1.0,  0.5],
        [ -0.5,  0.0,  0.0,  0.0,  0.0,  0.0,  0.0, -0.5],
        [ -0.5,  0.0,  0.0,  0.0,  0.0,  0.0,  0.0, -0.5],
        [ -0.5,  0.0,  0.0,  0.0,  0.0,  0.0,  0.0, -0.5],
        [ -0.5,  0.0,  0.0,  0.0,  0.0,  0.0,  0.0, -0.5],
        [ -0.5,  0.0,  0.0,  0.0,  0.0,  0.0,  0.0, -0.5],
        [  0.0,   0.0, 0.0,  0.5,  0.5,  0.0,  0.0,  0.0]
    ];
    
    rook_eval_black = rook_eval_white[::-1]

    queen_eval_white = [
        [ -2.0, -1.0, -1.0, -0.5, -0.5, -1.0, -1.0, -2.0],
        [ -1.0,  0.0,  0.0,  0.0,  0.0,  0.0,  0.0, -1.0],
        [ -1.0,  0.0,  0.5,  0.5,  0.5,  0.5,  0.0, -1.0],
        [ -0.5,  0.0,  0.5,  0.5,  0.5,  0.5,  0.0, -0.5],
        [  0.0,  0.0,  0.5,  0.5,  0.5,  0.5,  0.0, -0.5],
        [ -1.0,  0.5,  0.5,  0.5,  0.5,  0.5,  0.0, -1.0],
        [ -1.0,  0.0,  0.5,  0.0,  0.0,  0.0,  0.0, -1.0],
        [ -2.0, -1.0, -1.0, -0.5, -0.5, -1.0, -1.0, -2.0]
    ];

    queen_eval_black = queen_eval_white[::-1]

    king_eval_white = [
        [ -3.0, -4.0, -4.0, -5.0, -5.0, -4.0, -4.0, -3.0],
        [ -3.0, -4.0, -4.0, -5.0, -5.0, -4.0, -4.0, -3.0],
        [ -3.0, -4.0, -4.0, -5.0, -5.0, -4.0, -4.0, -3.0],
        [ -3.0, -4.0, -4.0, -5.0, -5.0, -4.0, -4.0, -3.0],
        [ -2.0, -3.0, -3.0, -4.0, -4.0, -3.0, -3.0, -2.0],
        [ -1.0, -2.0, -2.0, -2.0, -2.0, -2.0, -2.0, -1.0],
        [  2.0,  2.0,  0.0,  0.0,  0.0,  0.0,  2.0,  2.0 ],
        [  2.0,  3.0,  1.0,  0.0,  0.0,  1.0,  3.0,  2.0 ]
    ];

    king_eval_black = king_eval_white[::-1]

    value = 0
    if piece.piece_type == chess.PAWN:
        value = 10 + (pawn_eval_white[i][j] if piece.color == chess.WHITE else pawn_eval_black[i][j])
    elif piece.piece_type == chess.ROOK:
        value = 50 + (rook_eval_white[i][j] if piece.color == chess.WHITE else rook_eval_black[i][j])
    elif piece.piece_type == chess.KNIGHT:
        value = 30 + (knight_eval_white[i][j] if piece.color == chess.WHITE else knight_eval_black[i][j])
    elif piece.piece_type == chess.BISHOP:
        value = 30 + (bishop_eval_white[i][j] if piece.color == chess.WHITE else bishop_eval_black[i][j])
    elif piece.piece_type == chess.QUEEN:
        value = 90 + (queen_eval_white[i][j] if piece.color == chess.WHITE else queen_eval_black[i][j])
    elif piece.piece_type == chess.KING:
        value = 900 + (king_eval_white[i][j] if piece.color == chess.WHITE else king_eval_black[i][j])
    else:
        raise Exception(f'Unknown Piece: {piece.piece_type}')
    
    return value if piece.color == chess.WHITE else -value


def evaluate_board(board: object) -> int:
    total_evaluation = 0

    for i in range(8):
        for j in range(8):
            square = chess.square(i, j)
            piece = board.piece_at(square)

            if piece is not None:
                total_evaluation += get_piece_value(piece, i, j)
    
    return total_evaluation


def calculate_best_move_based_on_randomness(board: object, turn_color: bool) -> object:
    """
    We pick a move by randomly picking one of the available moves for that color.
    """
    moves_to_choose_from = []
    for move in board.legal_moves:
        square = move.from_square
        piece = board.piece_at(square)
        if piece is not None and turn_color == piece.color:
            moves_to_choose_from.append(move)

    return random.choice(moves_to_choose_from)


def calculate_best_move_based_on_position_evaluation(board: object, turn_color: bool) -> object:
    """
    We pick a move by evaluating the Board and calculating the opposite's side value on the table. We pick the move that disminishes the
    opposite side value on the Board the most. It only considers the current turn.
    """
    opposite_side_color = not turn_color
    possible_moves = [move for move in board.legal_moves]
    best_move = {
        'moves': [],
        'value': 99999
    }

    for move in possible_moves:
        board.push(move)
        board_value = evaluate_board(board)
        board.pop()

        if board_value < best_move['value']:
            best_move['value'] = board_value
            best_move['moves'].append(move)
        elif board_value == best_move['value']:
            best_move['moves'].append(move)
    
    # To make it more "real", we pick a random move from the best ones.
    return random.choice(best_move['moves'])


def calculate_best_move_based_on_minimax_evaluation(board: object, turn_color: bool, depth: int = 3) -> object:
    """
    We pick a move by evaluating the Board using minimax. Basically we iterate over all the possible moves (and multiple depths) and calculate the best
    move to reduce the most the board value of our opponent. It considers multiple turns.
    """
    def minimax(board, depth, isMaximixingPlayer):
        if depth == 0:
            return evaluate_board(board)
        
        possible_moves = [move for move in board.legal_moves]

        if isMaximixingPlayer:
            best_move_value = -99999

            for move in possible_moves:
                board.push(move)
                best_move_value = max(best_move_value, minimax(board, depth - 1, not isMaximixingPlayer))
                board.pop()
        else:
            best_move_value = 99999
    
            for move in possible_moves:
                board.push(move)
                best_move_value = min(best_move_value, minimax(board, depth - 1, isMaximixingPlayer))
                board.pop()

        return best_move_value

    opposite_side_color = not turn_color
    possible_moves = [move for move in board.legal_moves]
    best_move = {
        'moves': [],
        'value': 99999
    }

    for move in possible_moves:
        board.push(move)
        board_value = minimax(board, depth - 1, opposite_side_color)
        board.pop()

        if board_value <= best_move['value']:
            best_move['value'] = board_value
            best_move['moves'].append(move)
    
    # To make it more "real", we pick a random move from the best ones.
    return random.choice(best_move['moves'])

def calculate_best_move_based_on_minimax_evaluation_and_alpha_beta_pruning(board: object, turn_color: bool, depth: int = 3) -> object:
    """
    We pick a move by evaluating the Board using minimax. Basically we iterate over all the possible moves (and multiple depths) and calculate the best
    move to reduce the most the board value of our opponent. It considers multiple turns.

    See https://www.geeksforgeeks.org/minimax-algorithm-in-game-theory-set-4-alpha-beta-pruning/ for more information.
    """
    def minimax(board, depth, alpha, beta, isMaximixingPlayer):
        if depth == 0:
            # If the computer plays with blacks then we need to multiply this by -1. See https://stackoverflow.com/a/59132927/966922
            return evaluate_board(board)
        
        possible_moves = [move for move in board.legal_moves]

        if isMaximixingPlayer:
            best_move_value = -99999

            for move in possible_moves:
                board.push(move)
                best_move_value = max(best_move_value, minimax(board, depth - 1, alpha, beta, not isMaximixingPlayer))
                board.pop()
                alpha = max(alpha, best_move_value)
                if beta <= alpha:
                    return best_move_value
        else:
            best_move_value = 99999
    
            for move in possible_moves:
                board.push(move)
                best_move_value = min(best_move_value, minimax(board, depth - 1, alpha, beta, isMaximixingPlayer))
                board.pop()
                beta = min(beta, best_move_value)
                if beta <= alpha:
                    return best_move_value

        return best_move_value

    opposite_side_color = not turn_color
    possible_moves = [move for move in board.legal_moves]
    best_move = {
        'moves': [],
        'value': 99999
    }

    for move in possible_moves:
        board.push(move)
        board_value = minimax(board, depth - 1, -10000, 10000, opposite_side_color)
        board.pop()

        if board_value <= best_move['value']:
            best_move['value'] = board_value
            best_move['moves'].append(move)
    
    # To make it more "real", we pick a random move from the best ones.
    return random.choice(best_move['moves'])

def replace_char_by_chess_symbol(c: str):
    if c == 'P':
        return '♙'
    elif c == 'R':
        return '♖'
    elif c == 'N':
        return '♘'
    elif c == 'B':
        return '♗'
    elif c == 'Q':
        return '♕'
    elif c == 'K':
        return '♔'

    if c == 'p':
        return '♟︎'
    elif c == 'r':
        return '♜'
    elif c == 'n':
        return '♞'
    elif c == 'b':
        return '♝'
    elif c == 'q':
        return '♛'
    elif c == 'k':
        return '♚'

    return c

def display_board(board: object):
    """
    Display board by using Chess symbols from Unicode set.
    """
    map_of_pieces = board.piece_map()

    matrix = []
    submatrix = []
    c = 0
    for idx in range(8*8):
        c += 1
        try:
            piece_char = str(map_of_pieces[idx])
        except KeyError:
            chess_symbol = '.'
        else:
            chess_symbol = replace_char_by_chess_symbol(piece_char)

        submatrix.append(chess_symbol)

        if c % 8 == 0:
            matrix.append(submatrix)
            submatrix = []

    matrix = matrix[::-1] # Reverse rows
    #matrix = [row[::-1] for row in matrix] # Reverse columns

    y = ['1', '2', '3', '4', '5', '6', '7', '8']

    for idx_row, row in enumerate(matrix):

        for idx_column, column in enumerate(row):
            if idx_column == 0:
                print('')
                print(f'{y.pop()} ', end='')

            print(f'{column}  ', end='')
    
    print('')

    for i in ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']:
        if i == 'a':
            print(' ', end='')

        print(f' {i} ', end='')

    print('')


def perform_ai_turn(board: object, turn_color: bool):
    ###################################
    # AI TURN
    ###################################

    #ai_move = calculate_best_move_based_on_randomness(board, turn_color)
    #ai_move = calculate_best_move_based_on_position_evaluation(board, turn_color)
    #ai_move = calculate_best_move_based_on_minimax_evaluation(board, turn_color, depth=3)
    ai_move = calculate_best_move_based_on_minimax_evaluation_and_alpha_beta_pruning(board, turn_color, depth=4)

    board.push(ai_move)

    return board


def perform_human_turn(board: object):
    ###################################
    # HUMAN TURN
    ###################################

    correct_human_move = False
    while not correct_human_move:
        human_move_uci = input('\nYour Move: ')
        try:
            human_move = chess.Move.from_uci(human_move_uci)
        except ValueError:
            print('Invalid Move. Please try again.')
            continue

        if human_move not in board.legal_moves:
            print('Invalid Move. Please try again.')
            continue

        try:
            board.push(human_move)
        except AssertionError:
            print('Invalid Move. Please try again.')
            continue

        correct_human_move = True

    return board

def main():
    print('-----------------------------------------------')
    print('Welcome to TunaFish Chess Engine')
    print('Enjoy playing against the AI :)')
    print('-----------------------------------------------')

    board = chess.Board()

    moves = []

    # White always starts.
    turn_color = chess.WHITE
    while True:
        print(f'TURN NUM: {len(moves)} ------')

        display_board(board)

        board = perform_human_turn(board)

        human_move = board.peek()

        moves.append(human_move)

        turn_color = not turn_color

        board = perform_ai_turn(board, turn_color)

        ai_move = board.peek()

        moves.append(ai_move)

        display_board(board)

        print(f'\nAI Move: {moves[-1].uci()}\n')

        turn_color = not turn_color

        if board.outcome() is not None:
            raise Exception(f'Game finished in {len(moves)} moves.')
        
        input('Click ENTER to go to the next TURN...')
        

if __name__ == '__main__':
    main()