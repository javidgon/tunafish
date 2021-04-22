from uci import uci_loop

def test_uci_loop_set_up_cmds():
    testing_cmds = [
        'quit',
        'ucinewgame',
        'isready',
        'uci',
    ]

    expected_stdout = [
        'id name Tunafish',
        'id author José Vidal',
        'uciok',
        'readyok',
    ]

    stdout = uci_loop(testing_cmds)

    assert expected_stdout == stdout


def test_uci_loop_playing_cmds():
    testing_cmds = [
        'quit',
        'go wtime 1500000 btime 1500000 winc 0 binc 0',
        'position startpos moves d2d4',
    ]

    stdout = uci_loop(testing_cmds)

    assert 'bestmove' in stdout[0]
