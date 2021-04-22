# Tunafish

Simple Chess Engine built in Python. Supports both Standalone and UCI-powered Chess GUIs modes.

## How to Play Standalone

```
>> pip install -r requirements.txt

>> python tunafish.py

-----------------------------------------------
Welcome to TunaFish Chess Engine
Enjoy playing against the AI :)
-----------------------------------------------
TURN NUM: 0 ------

8 ♜  ♞  ♝  ♛  ♚  ♝  ♞  ♜
7 ♟︎  ♟︎  ♟︎  ♟︎  ♟︎  ♟︎  ♟︎  ♟︎
6 .   .   .   .   .   .  .   .
5 .   .   .   .   .   .  .   .
4 .   .   .   .   .   .  .   .
3 .   .   .   .   .   .  .   .
2 ♙  ♙  ♙  ♙  ♙  ♙  ♙  ♙
1 ♖  ♘  ♗  ♕  ♔  ♗  ♘  ♖
  a  b  c  d  e  f  g  h

Your Move:
```

## How to play using Chess GUIs (e.g., Arena Chess GUI)

In Windows, click on install a new "Engine" and select `tunafish.bat` file.

In Linux, click on install a new "Engine" and select `uci.py`.

## TODO

* Pawn Promotion
* Castling
* En passant
* Provide more detail about engine nodes search.