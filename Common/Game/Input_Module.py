import Checking_Module
def Get_Player_name():
  name = input("Please enter your name: ").lower().capitalize()
  return (str(name))
def Get_Player_Door_input():
  num_input = False
  print("Which door will you open?")
  while num_input == False:
    try:
      door = int(input("1, 2, 3? "))
      if Checking_Module.Check_input_Range(door) == True:
        return (door)
      else:
        print("Please input a either 1, 2 or 3!")
    except:
      print("Please input a either 1, 2 or 3!")
def Get_Player_Saying_Answer():
  player_answer = input("What is the missing word? ").strip().lower()
  return player_answer