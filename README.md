# SnakeGame
A snake game Using pygame.


1. Pygame
   
Purpose: Pygame is a cross-platform set of Python modules designed for writing video games. It includes computer graphics and sound libraries, which makes it a popular choice for developing simple games.


Functions and Classes Used:

pygame.init(): Initializes all the imported Pygame modules.
pygame.display.set_mode(): Sets up the display window with a specified size.
pygame.display.set_caption(): Sets the title of the window.
pygame.time.Clock(): Creates a clock object to manage the frame rate.
pygame.font.Font(): Loads a font for rendering text.
pygame.Rect: Represents a rectangle object used for the snake's body, head, and apple.
pygame.event.get(): Retrieves a list of all events currently in the event queue.
pygame.draw.rect(): Draws a rectangle on the screen.
pygame.KEYDOWN: Event type used to detect when a key is pressed.
pygame.QUIT: Event type used to detect when the window is closed.
pygame.display.flip(): Updates the full display surface to the screen.
pygame.quit(): Uninitializes all Pygame modules and exits the program.


2. random
   
Purpose: The random module is used to generate random numbers. In this game, it’s used to randomly position the apple on the screen.
Functions Used:
random.randint(): Returns a random integer between the specified range.

Overview of the Code:

Game Mechanics:
The game is a basic Snake game where the player controls a snake that moves around the screen, eating apples that spawn randomly. Each time the snake eats an apple, it grows longer.

Snake Class:
Manages the snake’s position, movement, and checks if it has collided with itself, which causes the game to reset.

Apple Class:
Handles the random positioning and drawing of the apple.

Main Game Loop:

Handles user input, updates the snake and apple, checks for collisions, and renders the game elements on the screen.
