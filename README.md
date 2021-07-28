# snakes-and-ladders
My solution to the snakes and ladders kata on codewars (An Object oriented Python exercise). Be fair & don't just copy and submit 😉


![snakes](img/snakesandladdersboard.jpg)

## Requirements

### Rules

```

1.  There are two players and both start off the board on square 0.

2.  Player 1 starts and alternates with player 2.

3.  You follow the numbers up the board in order 1=>100

4.  If the value of both die are the same then that player will have another go.

5.  Climb up ladders. The ladders on the game board allow you to move upwards and get ahead faster. If you land exactly on a square that shows an image of the bottom of a ladder, then you may move the player all the way up to the square at the top of the ladder. (even if you roll a double).

6.  Slide down snakes. Snakes move you back on the board because you have to slide down them. If you land exactly at the top of a snake, slide move the player all the way to the square at the bottom of the snake or chute. (even if you roll a double).

7.  Land exactly on the last square to win. The first person to reach the highest square on the board wins. But there's a twist! If you roll too high, your player "bounces" off the last square and moves back. You can only win by rolling the exact number needed to land on the last square. For example, if you are on square 98 and roll a five, move your game piece to 100 (two moves), then "bounce" back to 99, 98, 97 (three, four then five moves.)

8.  If the Player rolled a double and lands on the finish square “100” without any remaining moves then the Player wins the game and does not have to roll again.
```

### Returns

Return "Player `n` Wins!". Where `n` is winning player that has landed on square 100 without any remainding moves left.

Return "Game over!" if a player has won and another player tries to play.

Otherwise return "Player `n` is on square x". Where `n` is the current player and x is the sqaure they are currently on.


### Usage / Playing yourself with a friend

Start Python consolse and import
```python
>>> from snakes_and_ladders import *
```

Initialize game
```python
>>> game = SnakesLadders()
```

Players now throw two dice alternatingly until the game is finished
```python
>>> game.play(6, 4)
'Player 1 is on square 10'
>>> game.play(2, 5)
'Player 2 is on square 14'

...
```

Of course you can get random die values if you don't have dice at hand
```python
>>> from random import randint
>>> die1 = randint(1,6)
>>> print(die1)
4
>>> die2 = randint(1,6)
>>> print(die2)
2
>>> game.play(die1, die2)
'Player 2 is on square 21'
```
