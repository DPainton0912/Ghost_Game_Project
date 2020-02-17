#Ghost Game
import Gameplay_Module
def Startup():
  gamestate = 0
  while gamestate == 0:
    gamestate = Gameplay_Module.Play_game()
Startup()