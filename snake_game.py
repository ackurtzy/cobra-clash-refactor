from snake_game_model import SnakeGameModel
from snake_view import SnakeGameTextView


def main():
    """
    Runs a short test of the double snake game model
    """
    game = SnakeGameModel()
    view = SnakeGameTextView(game)

    view.draw()
    game.move_snakes("RIGHT", "LEFT")
    view.draw()
    game.move_snakes("UP", "DOWN")
    view.draw()
    game.move_snakes("LEFT", "RIGHT")
    view.draw()


if __name__ == "__main__":
    main()
