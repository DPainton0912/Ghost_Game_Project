from Input_Module import Get_Player_Saying_Answer
def Minigame_Saying_Start():
    print("The early **** gets the worm.")
    answer = Get_Player_Saying_Answer()
    if answer == "bird":
        return 1
    else:
        return 0