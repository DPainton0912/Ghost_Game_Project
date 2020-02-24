from random import randint
import Hint_Module
import Checking_Module
import Input_Module
import Highscore_Module
import Minigame_Saying_Module
def Play_Again(Score,Pname):
  acceptedinput = False
  while acceptedinput == False:
    again = str(input("Play again? Y/N "))
    again = again.lower()
    if again == "y":
      return(0) 
    elif again == "n":
      print("Not brave enough huh?")
      print("Lets see how you stacked up against the others!")
      Highscore_Module.Display_Highscores(Score,Pname)
      print("Come back when you're brave enough to try again.")
      return(1)
def Ghost_Found(TotalScore, Player_Name):
  print("Ghost!")
  print("Run away!")
  print("Game Over! " + Player_Name + " scored: ", TotalScore, end=".\n")
  #Check if user wants to try again, if yes reset loop and if no end game
  retry = Play_Again(TotalScore,Player_Name)
  return(retry)
def Safe_Found(score_result):
  print("No ghost!")
  print("You enter the next room.")
  #Add points to score total and continue game
  if score_result == 0 :
    return (1)
  else:
    return (2)
def Play_game():
  score = 0
  print("Ghost Game")
  PName = Input_Module.Get_Player_name()
  ghost_door = randint(1,3)
  minigame_result = Minigame_Saying_Module.Minigame_Saying_Start()
  hint_door = Hint_Module.Display_Hint(ghost_door, minigame_result)
  result = int(Checking_Module.Check_Door_Result(ghost_door,hint_door))
  while result != 2:
    score = score + Safe_Found(result)
    hint_door = Hint_Module.Display_Hint(ghost_door, minigame_result)
    result = int(Checking_Module.Check_Door_Result(ghost_door, hint_door))
  restart = Ghost_Found(score,PName)
  return (restart)