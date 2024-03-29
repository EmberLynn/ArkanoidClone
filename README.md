# ArkanoidClone
A clone of Arkanoid written in PyGame

To Do's:

1. (DONE)Create start screen:
    - Class of additional screens; only render when required
2. (DONE)Display final score at end of game and provide option to restart or quit
3. (DONE)Add continue screen between levels
4. (DONE)Add High Score list to start screen (save top 10 scores of all time)
5. (DONE)Add a system of scaling difficulty (example, blocks take multiple hits):
    - With this, I will add sprites (or something) to blocks to exibit level of damage
6. Add Roguelite elements to game:
    - First, need to create a system that holds and execute boons
        - The game needs to be manipulated based on what a boon does
    - Let's start with pure boons:
        - (DONE) Faster paddle
        - (DONE) longer paddle
        - (DONE) get a second ball

Others in no particular order (nice-to-haves):

1. Change ball velocity based on where the ball hits the paddle
2. Graphics:
    - Make ball a round sprite
    - Make paddle a dog (BARKanoid is the name, afterall)
    - Have a set of various backgrounds for the LevelRenderer to use
3. (DONE)Regardless if it matters in pygame, I'd like to load and unload assets such as screens
    - clearing and writing to one object as needed
4. (DONE)Find better way to import modules in directories.
5. (DONE)Convert Buttons to a class
6. General code analysis and clean-up
    - Code optimization
    - Fixing mutators and accessors
    - Main (ArkanoidClone.py) is getting large; split into functions
        - Working on it... but not sure if it is making it more confusing or not...
7. (DONE)Add black outline to blocks (so they can easily be seen)
8. Launcher for the .exe
9. (DONE)In Windows, moving the game screen repeatedly or repeatedly focusing on another application can cause the game's surface to misalign with the window (I don't know what the fix would be for this or what is causing the issue)
    - NOTE: it was a me problem not a Windows problem and I fixed it when I updated to Python 3.10 and the newer PyGame version
10. (In Progress)I learned about rect.collidepoint -- this would have been an easier way to implement button clicks than what I ended up doing. I'd like to re-write button click implementation to use collidepoint instead.

Here are fantastic suggestions from my test player (Katz) that I will implements:
- Fart sound effect with block destruction (maybe not my fave suggestion...)
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