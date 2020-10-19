from Live import load_game, welcome


def main():
    name = input("Welcome, please enter your name: ")
    print("\n" + welcome(name))
    load_game()


if __name__ == "__main__":
    main()
