# ArkanoidClone
A clone of Arkanoid written in PyGame

To Do's:

1. (DONE)Create start screen:
    - Class of additional screens; only render when required
2. (DONE)Display final score at end of game and provide option to restart or quit
3. (DONE)Add continue screen between levels
4. Add High Score list to start screen (save top 10 scores of all time)
5. Add a system of scaling difficulty (example, blocks take multiple hits):
    - With this, I will add sprites to blocks to exibit level of damage
6. Add Roguelite elements to game:
    - Example. Choice or upgrade after each screen -- a pro that comes with a con?

Others in no particular order (nice-to-haves):

1. Change ball velocity based on where the ball hits the paddle
2. Graphics:
    - Make ball a round sprite
    - Make paddle a dog (BARKanoid is the name, afterall)
    - Have a set of various backgrounds for the LevelRenderer to use
3. Regardless if it matters in pygame, I'd like to load and unload assets such as screens
4. Find better way to import modules in directories.
5. (DONE)Convert Buttons to a class
6. General code analysis and clean-up
    - Code optimization
    - Fixing mutators and accessors
7. Add black outline to blocks (so they can easily be seen)
8. Launcher for the .exe

Here are fantastic suggestions from my test player (Katz) that I will implements:
- Fart sound effect with block destruction (maybe not my fave suggestion...)
- Add outline to the blocks so even colour blind individuals can see them all
- Add a Lime somewhere...
- For the Roguelike elements:
    - longer bar
    - screen wrap
    - ball skins (each skin comes with a boon)
    - stronger ball hit (to add when block take multi-hits)
    - ball destroys multiple blocks per hit
    - multi-ball
    - multi-bars
- Temporary randomily generated block that offers a boon when hit
- Add a story mode to the game
- The floor is rising level (maybe much later in the game; an additional difficulty mode)