import Input_Module
def Check_input_Range(Number):
  if Number == 1 or Number == 2 or Number == 3:
    return (True)
  else:
    return(False)
def Check_Door_Result(DoorSpooky,DoorHint):
  door_num = Input_Module.Get_Player_Door_input()
  if door_num == DoorSpooky:
    return (2)    
  elif door_num != DoorHint and DoorHint != DoorSpooky:
    return(1)     
  else:
    return (0)