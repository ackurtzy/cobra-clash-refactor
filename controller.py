class SnakeGameController:
    """
    Controls a two player snake game with text input
    """

    def __init__(self, model, view):
        """
        Sets up the controller with model and view
        """
        self._model = model
        self._view = view
        self._snake_one_direction = "RIGHT"
        self._snake_two_direction = "LEFT"

    def run(self):
        """
        Runs the game loop until a player wins
        """
        snake_one_won = False
        snake_two_won = False

        while not snake_one_won and not snake_two_won:
            self._view.draw()

            snake_one_move = input("Snake one move: ").upper()
            snake_two_move = input("Snake two move: ").upper()

            self._snake_one_direction = self._translate_input(
                snake_one_move, self._snake_one_direction
            )
            self._snake_two_direction = self._translate_input(
                snake_two_move, self._snake_two_direction
            )

            self._model.move_snakes(
                self._snake_one_direction, self._snake_two_direction
            )
            snake_one_won, snake_two_won = self._model.snake_won()

        self._view.draw()
        print("Snake one won:", snake_one_won)
        print("Snake two won:", snake_two_won)

    def _translate_input(self, move, current_direction):
        """
        Translates user input into a snake direction
        """
        move_dict = {
            "W": "UP",
            "S": "DOWN",
            "A": "LEFT",
            "D": "RIGHT",
            "UP": "UP",
            "DOWN": "DOWN",
            "LEFT": "LEFT",
            "RIGHT": "RIGHT",
        }
        return move_dict.get(move, current_direction)
