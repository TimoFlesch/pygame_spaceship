# spaceship game in python
I tried to familiarise myself with the *pygame* library and implemented
a very rudimental 2D game.
The objective is to steer a space ship through a field of asteroids without crashing into the. The score as well as the speed with which asteroids are being approached increase with each successfully avoided asteroid.  

![example]("./assets/game_screen.png")


note: if you observe high single core usage (perhaps even maxed out), uninstall pygame and install the latest dev version
```bash
pip uninstall pygame
pip install "pygame>=2.0.0.dev1"
```
## how to start the game
from the command line, navigate to the *code* folder and call
```bash
python spacegame.py
```

## game mechanics
### controls
Use the four *arrow keys* to control the space ship. It flies forward automatically, but you can increase the speed by pressing *up*

### objectives
avoid crashing into asteroids.

### how to close the game
close the window by pressing the small x in the top right corner, or by hitting the *ESC* button whenever think you've had enough.


## Resources
All externally imported assets are open source.  
Rocket image by <a href="https://pixabay.com/users/dawnydawny-2157612/?utm_source=link-attribution&amp;utm_medium=referral&amp;utm_campaign=image&amp;utm_content=2442125">dawnydawny</a> from <a href="https://pixabay.com/?utm_source=link-attribution&amp;utm_medium=referral&amp;utm_campaign=image&amp;utm_content=2442125">Pixabay</a>  
Asteroid image obtained from <a href="https://opengameart.org/content/asteroid-generator-and-a-set-of-generated-asteroids"> opengameart</a>
