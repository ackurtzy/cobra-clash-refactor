"""
Contains the viewer class to view the game graphically
"""

from abc import ABC, abstractmethod
import pygame


class SnakeGameView(ABC):
    """
    An abstract class used to view the snake game with an
    abstract method "draw" for different ways to display
    the board.

    Attributes:
        _model: An instance of the SnakeGameModel class
    """

    def __init__(self, model):
        """
        Initializes an instance of the SnakeGameView class

        Parameters:
            model: An instance of the SnakeGameModel class
        """
        super().__init__()
        self._model = model

    @property
    def model(self):
        """
        A property that returns the snake game model stored in the
        SnakeGameModel instance
        """
        return self._model

    @abstractmethod
    def draw(self, frame_rate):
        """
        An abstract method defined in the following class to view the game
        """


class GraphicalView(SnakeGameView):
    """
    A class inheriting from the SnakeGameView class to display the game
    graphically using pygame

    Attributes:
        _width: An integer the width of the game window
        _height: An integer representing the height of the game window
        _model: An instance of the SnakeGameMode class
        _screen: A surface representing the game window surface
            created using pygame
        _shift: A float representing the shift value to center
            the game board horizontally
        _in_bounds_shift: An integer representing the shift value to
            properly place assets on the board
        _snake_one_head: A surface representing the image of the head
            of Snake One
        _snake_one_body: A surface representing the body of Snake One
        _snake_two_head: A surface representing the image of the head
            of Snake Two
        _snake_two_body: A surface representing the body of Snake Two
    """

    def __init__(self, model, width, height):
        """
        Initializes an instance of the GraphicalView class

        Parameters:
            model: An instance of the SnakeGameModel class
            width: An integer representing the width of the game window
            height: An integer representing the height of the game window
        """
        super().__init__(model)

        self._width = width
        self._height = height

        # Initializing pygame
        pygame.init()
        self._screen = pygame.display.set_mode((width, height))
        pygame.display.set_caption("Cobra Clash")

        # To place the assets properly on the board
        self._shift = (width - height) / 2
        self._in_bounds_shift = 50

    def _snake_head_direction(self, snake_head, direction):
        """
        Rotates the snake's head image according to the snake's direction

        Parameters:
            snake_head: A surface representing the image of the snake's head
            direction: A string representing the direction in which the snake
                wants to go

        Returns:
            A surface representing the rotated image
        """

        head_directions = {
            "UP": pygame.transform.rotate(snake_head, 180),
            "DOWN": pygame.transform.rotate(snake_head, 0),
            "RIGHT": pygame.transform.rotate(snake_head, 90),
            "LEFT": pygame.transform.rotate(snake_head, -90),
        }
        return head_directions[direction]

    def _draw_snake(self, snake, snake_body, snake_head):
        """
        Draws the given snake onto the board

        Args:
            snake: An instance of the snake class
            snake_body: A surface representing the image of the snake's body
            snake_head: A surface representing the image of the snake's head

        Returns:
            None
        """

        for index, location in enumerate(snake.locations):
            x_value = location[1] * 50 + self._shift + self._in_bounds_shift
            y_value = location[0] * 50 + self._in_bounds_shift
            direction = snake.directions[0]
            if index == 0:
                self._screen.blit(
                    self._snake_head_direction(snake_head, direction),
                    (x_value, y_value),
                )
                continue
            self._screen.blit(snake_body, (x_value, y_value))

    def _draw_running_game(self):
        """
        Draws all the assets of the game on the screen when it is running
        """
        snake_one_head = pygame.image.load("images/snake_head_one.png")
        snake_one_body = pygame.Surface((50, 50))
        snake_one_body.fill("Green")

        snake_two_head = pygame.image.load("images/snake_head_two.png")
        snake_two_body = pygame.Surface((50, 50))
        snake_two_body.fill("Red")

        background = pygame.image.load("images/background.png")
        snake_map = pygame.image.load("images/snake_map.jpeg")
        apple_image = pygame.image.load("images/apple.png")

        self._screen.blit(background, (0, 0))
        self._screen.blit(snake_map, (self._shift, 0))

        self._draw_snake(self._model.snake_one, snake_one_body, snake_one_head)
        self._draw_snake(self._model.snake_two, snake_two_body, snake_two_head)

        for apple in self._model.apples:
            x_value = apple[1] * 50 + self._shift + self._in_bounds_shift
            y_value = apple[0] * 50 + self._in_bounds_shift
            self._screen.blit(apple_image, (x_value, y_value))

    def draw(self, frame_rate):
        """
        Draws the board for a running game
        """
        self._draw_running_game()

        pygame.display.update()
        pygame.time.Clock().tick(frame_rate)
