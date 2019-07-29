# spaceship game in python
I tried to familiarise myself with pygame and implemented
a very rudimental 2D game. 
The objective is to steer a space ship through a field of asteroids without crashing into the. The score as well as the speed with which asteroids are being approached increase with each successfully avoided asteroid.  


note: if you observe high single core usage (perhaps even maxed out), uninstall pygame and install the latest dev version
```bash
pip uninstall pygame
pip install "pygame>=2.0.0.dev1"
```
## how to start the game
from the command line, call 
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
