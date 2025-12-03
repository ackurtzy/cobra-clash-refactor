from double_snake_game_model import SnakeGameModel


def main():
    """
    Runs a short test of the double snake game model
    """
    game = SnakeGameModel()

    print(game)
    game.move_snakes("RIGHT", "LEFT")
    print(game)
    game.move_snakes("UP", "DOWN")
    print(game)
    game.move_snakes("LEFT", "RIGHT")
    print(game)


if __name__ == "__main__":
    main()
