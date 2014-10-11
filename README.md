# pyCompteEstBon

A simple python implementation of the game "Le compte est bon", from the french TV show "Des chiffres et des lettres". The rules of the game can be found on [Wikipedia](http://en.wikipedia.org/wiki/Des_chiffres_et_des_lettres#Le_compte_est_bon_.28.22the_total_is_right.22.29).

## Dependencies

The script has been tested with:

- Python 3.4.0

## Usage

### Start the game

```sh
./game.py
```

### Play the game

The initial game will look like this (number may vary):
```
Target: 356
Numbers:
0: 10 
1: 2 
2: 2 
3: 6 
4: 25 
5: 2 
Results:
Operations:
? ? ? = ?

What to do? 
```

- Enter the index of a number to use it in current operation (e.g. enter 0 to use number 10, in the above example).
- Enter an operator (+, -, *, /) to use it in current operation
- When an operation is complete, it will automatically switch to the next one. The result will be indexed so you can use it.
- The game is won when the result of an operation is equal to the target number.

## License

This project is licensed under the terms of the GPL version 2 license.