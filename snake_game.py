from snake_game_model import SnakeGameModel
from snake_view import SnakeGameTextView
from controller import SnakeGameController


def main():
    """
    Runs a game of snake using the controller
    """
    model = SnakeGameModel()
    view = SnakeGameTextView(model)
    controller = SnakeGameController(model, view)
    controller.run()


if __name__ == "__main__":
    main()
