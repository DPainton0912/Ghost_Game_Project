from random import randint
from Input_Module import Get_Player_Saying_Answer
def Minigame_Saying_Start():
    saying_num = randint(1,5)
    if saying_num == 1:
        print("The early **** gets the worm.")
    elif saying_num == 2:
        print("Beat around the ****.")
    elif saying_num == 3:
        print("********* killed the cat.")
    elif saying_num == 4:
        print("Time ***** when your having fun.")
    elif saying_num == 5:
        print("We'll cross that ****** when we come to it.")
    answer = Get_Player_Saying_Answer()
    if saying_num == 1 and answer == "bird":
        return 1
    elif saying_num == 2 and answer == "bush":
        return 1
    elif saying_num == 3 and answer == "curiosity":
        return 1
    elif saying_num == 4 and answer == "flies":
        return 1
    elif saying_num == 5 and answer == "bridge":
        return 1
    else:
        return 0