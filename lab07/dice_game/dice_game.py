from game_controller import GameController


def main():
    gc = GameController()
    print("--------------------------------")
    print("Welcome to street craps!")
    print("""Rules:
If you roll 7 or 11 on your first roll, you win.
If you roll 2, 3, or 12 on your first role, you lose.
If you roll anything else, that's your 'point', and
you keep rolling until you either roll your point
again (win) or roll a 7 (lose)""")
    print()

    gc.start_play()


main()
