from __future__ import print_function
from __future__ import division
import logging
import argparse
import chess

from tunafish import perform_ai_turn

FEN_INITIAL = "rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1"


def output(line):
    logging.basicConfig(filename="tunafish.log", level=logging.DEBUG)

    print(line)
    logging.debug(line)


def uci_loop(testing_cmds=None):
    history_stdout = []
    stdout = []
    stack = []
    board = None

    while True:
        if stack:
            gui = stack.pop()
        else:
            if testing_cmds is not None:
                gui = testing_cmds.pop()
            else:
                gui = input()

        if gui == "uci":
            # ID Phase
            stdout.append("id name Tunafish")
            stdout.append("id author José Vidal")
            stdout.append("uciok")
        elif gui == "isready":
            # Checking Readiness
            stdout.append("readyok")
        elif gui == "ucinewgame":
            # Start new Game
            stack.append("position fen " + FEN_INITIAL)
        elif gui.startswith("position"):
            # Provide a new Position
            params = gui.split(" ")
            idx = gui.find("moves")

            if idx >= 0:
                moveslist = gui[idx:].split()[1:]
            else:
                moveslist = []

            if params[1] == "fen":
                if idx >= 0:
                    fenpart = gui[:idx]
                else:
                    fenpart = gui

                _, _, fen = fenpart.split(" ", 2)

            elif params[1] == "startpos":
                fen = FEN_INITIAL

            else:
                pass

            turn_color = chess.WHITE if fen.split()[1] == "w" else chess.BLACK

            board = chess.Board(fen)
            for move_uci in moveslist:
                board.push_uci(move_uci)

        elif gui.startswith("go"):
            # To calculate the score we can just substract
            # Minimax valuation White - Minimax valuation black.
            # If it's positive, white wins. If it's negative, black wins.
            # e.g., info depth 3 score cp 34 time 55 nodes 7890 pv {}
            turn_color = not turn_color

            board = perform_ai_turn(board, turn_color)

            ai_move = board.peek()
            stdout.append(f"bestmove {ai_move.uci()}")

        elif gui == "quit":
            break

        for line in stdout:
            output(line)

        history_stdout += stdout
        stdout.clear()

    return history_stdout


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "module",
        help="tunafish.py file (without .py)",
        type=str,
        default="tunafish",
        nargs="?",
    )

    uci_loop()


if __name__ == "__main__":
    main()
