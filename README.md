# ArkanoidClone
A clone of Arkanoid written in PyGame

To Do's:
1.(DONE)Create start screen:
    Class of additional screens; only render when required
2.(DONE)Display final score at end of game and provide option to restart or quit
3.Add continue screen between levels
4.Add High Score list to start screen (save top 10 score of all time)
5.Add a system of scaling difficulty (example, blocks take multiple hits):
    With this, I will add sprites to blocks to exibit level of damage
6.Add Roguelite elements to game:
    Example. Choice or upgrade after each screen -- a pro that comes with a con?

Others in no particular order:
1.Change ball velocity based on where the ball hits the paddle
2.Graphics:
    a. Make ball a round sprite
    b. Make paddle a dog (BARKanoid is the name, afterall)
    c. Have a set of various backgrounds for the LevelRenderer to use
3.Regardless if it matters in pygame, I'd like to load and unload assets such as screens
4.Find better way to import modules in directories.
5.Convert Buttons to a class