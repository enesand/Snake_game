# Snake_game
Welcome to the Snake Game repository! This is a basic implementation of the classic Snake Game using Python and Pygame. Below, you'll find information on the game rules, properties, and how to set up and play the game.

# Game Rules and Properties
Monster and Money Vectors:
* There is a 30x30 pixels monster vector and a 30x30 pixels money vector.
* Initial monster coordinates are set to half of the height and width of the screen.
* Initial money coordinates are randomly generated within the appropriate area of the screen, excluding the score board.
  
Screen Size:
* The game screen has a size of 750x600 pixels.
  
Background Music:
* The background music, named background.mp3, plays continuously until the game is closed.
  
Score Board:
* A score board is located at the top of the screen with a 64-pixel font size.
  
Game Interaction(When the monster coordinates and money coordinates match):
* The score increases by 1 point.
* New money coordinates are randomly determined.
* An eating effect sound plays for a few seconds.
  
Game Restart( If the monster coordinates reach the edge of the screen):
* The game restarts from the beginning with a score of 0.
* New monster and money coordinates are set.
* A game over music plays for a few seconds.
