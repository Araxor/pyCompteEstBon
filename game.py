#!/usr/bin/env python3
from CompteEstBon import CompteEstBon


def print_target(game):
    print("Target: {}".format(game.target))


def print_numbers(game):
    print("Numbers:")
    numbers = game.get_numbers()
    for index, number in enumerate(numbers):
        # If the number is used, show it
        status = "(used)" if number[1] else ""
        print("{}: {} {}".format(index, number[0], status))


def print_results(game):
    results = game.get_results()
    print("Results:")
    for index, result in enumerate(results, start=6):
        # If the number is used, show it
        status = "(used)" if result[1] else ""
        print("{}: {} {}".format(index, result[0], status))


def print_operations(game):
    print("Operations:")
    for op in game.get_operations_strings():
        print(op)


def handle_input(game):
    user_input = input("What to do? ")
    # Handle number requests
    if user_input in [str(n) for n in range(6)]:
        game.use_base_number(int(user_input))
    # Handle the results requests
    elif user_input in [str(n) for n in range(6, 6+len(game.results))]:
        game.use_result(int(user_input)-6)
    # Handle operator requests
    elif user_input in ['+', '-', '*', '/']:
        game.use_operator(user_input)


def print_status(game):
    print_target(game)
    print_numbers(game)
    print_results(game)
    print_operations(game)
    print()


def game_loop(game):
    print_status(game)
    handle_input(game)
    print()

if __name__ == "__main__":
    game = CompteEstBon()

    while not game.finished:
        try:
            game_loop(game)

        except KeyboardInterrupt:
            print()
            break

    if game.finished:
        print("Congratulations! You won!")
