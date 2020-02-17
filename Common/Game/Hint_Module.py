from random import randint
def Display_Hint(DoorSpooky):
  hint_num = randint(1,5)
  door_hint = randint(1,3)
  print("Three doors ahead...")
  #Generate a hint for the doors
  if door_hint == 1 and door_hint != DoorSpooky:
    if hint_num == 1:
      print("You hear no sound from behind the first door.")
    elif hint_num == 2:
      print("You sense no presense from behind the first door.")
    elif hint_num == 3:
      print("You see nothing unusual coming from behind the first door.")
    elif hint_num == 4:
      print("The first door is the ghost door.")
    elif hint_num == 5:
      print("I don't know, figure it out yourself.")
  elif door_hint == 2 and door_hint != DoorSpooky:
    if hint_num == 1:
      print("You hear no sound from behind the second door.")
    elif hint_num == 2:
      print("You sense no presense from behind the second door.")
    elif hint_num == 3:
      print("You see nothing unusual coming from behind the second door.")
    elif hint_num == 4:
      print("The second door is the ghost door.")
    elif hint_num == 5:
      print("I don't know, figure it out yourself.")
  elif door_hint == 3 and door_hint != DoorSpooky:
    if hint_num == 1:
      print("You hear no sound from behind the last door.")
    elif hint_num == 2:
      print("You sense no presense from behind the last door.")
    elif hint_num == 3:
      print("You see nothing unusual coming from behind the last door.")
    elif hint_num == 4:
      print("The last door is the ghost door.")
    elif hint_num == 5:
      print("I don't know, figure it out yourself.")
  if door_hint ==  1 and door_hint == DoorSpooky:
    if hint_num == 1:
      print("You hear an eerie silence from behind the first door.")
    elif hint_num == 2:
      print("You sense an ominous presense from behind the first door.")
    elif hint_num == 3:
      print("You see a sinister light coming from behind the first door.")
    elif hint_num == 4:
      print("The first door is not the ghost door.")
    elif hint_num == 5:
      print("I don't know, figure it out yourself.")
  elif DoorSpooky ==  2 and door_hint == DoorSpooky:
    if hint_num == 1:
      print("You hear an eerie silence from behind the second door.")
    elif hint_num == 2:
      print("You sense an ominous presense from behind the second door.")
    elif hint_num == 3:
      print("You see a sinister light coming from behind the second door.")
    elif hint_num == 4:
      print("The second door is not the ghost door.")
    elif hint_num == 5:
      print("I don't know, figure it out yourself.")
  elif DoorSpooky ==  3 and door_hint == DoorSpooky:
    if hint_num == 1:
      print("You hear an eerie silence from behind the last door.")
    elif hint_num == 2:
      print("You sense an ominous presense from behind the last door.")
    elif hint_num == 3:
      print("You see a sinister light coming from behind the last door.")
    elif hint_num == 4:
      print("The last door is not the ghost door.")
    elif hint_num == 5:
      print("I don't know, figure it out yourself.")
  return(door_hint)