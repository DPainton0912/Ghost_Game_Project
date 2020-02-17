#Ghost Game
from random import randint
#Open the Leaderboard files and take information from them
file_open = open("Leaderboard_Names.txt", "r")
highscores_name = file_open.read()
file_open.close()
file_open = open("Leaderboard_Scores.txt", "r")
highscores_score = file_open.read()
file_open.close()
highscores_name = highscores_name.split(",")
highscores_score = highscores_score.split(",")
#Game start, set up variables and get users name
print('Ghost Game')
feeling_brave = True
num_input = False
score = 0
name = input('Please enter your name: ').lower()
#Start the game loop
while feeling_brave:
    ghost_door = randint(1,3)
    hint_num = randint(1,5)
    door_hint = randint(1,3)
    print('Three doors ahead...')
    #Generate a hint for the doors
    if door_hint == 1 and door_hint != ghost_door:
        if hint_num == 1:
            print('You hear no sound from behind the first door.')
        elif hint_num == 2:
            print('You sense no presense from behind the first door.')
        elif hint_num == 3:
            print('You see nothing unusual coming from behind the first door.')
        elif hint_num == 4:
            print('The first door is the ghost door.')
        elif hint_num == 5:
            print('I don\'t know, figure it out yourself.')
    elif door_hint == 2 and door_hint != ghost_door:
        if hint_num == 1:
            print('You hear no sound from behind the second door.')
        elif hint_num == 2:
            print('You sense no presense from behind the second door.')
        elif hint_num == 3:
            print('You see nothing unusual coming from behind the second door.')
        elif hint_num == 4:
            print('The second door is the ghost door.')
        elif hint_num == 5:
            print('I don\'t know, figure it out yourself.')
    elif door_hint == 3 and door_hint != ghost_door:
        if hint_num == 1:
            print('You hear no sound from behind the last door.')
        elif hint_num == 2:
            print('You sense no presense from behind the last door.')
        elif hint_num == 3:
            print('You see nothing unusual coming from behind the last door.')
        elif hint_num == 4:
            print('The last door is the ghost door.')
        elif hint_num == 5:
            print('I don\'t know, figure it out yourself.')
    if door_hint ==  1 and door_hint == ghost_door:
        if hint_num == 1:
            print('You hear an eerie silence from behind the first door.')
        elif hint_num == 2:
            print('You sense an ominous presense from behind the first door.')
        elif hint_num == 3:
            print('You see a sinister light coming from behind the first door.')
        elif hint_num == 4:
            print('The first door is not the ghost door.')
        elif hint_num == 5:
            print('I don\'t know, figure it out yourself.')
    elif ghost_door ==  2 and door_hint == ghost_door:
        if hint_num == 1:
            print('You hear an eerie silence from behind the second door.')
        elif hint_num == 2:
            print('You sense an ominous presense from behind the second door.')
        elif hint_num == 3:
            print('You see a sinister light coming from behind the second door.')
        elif hint_num == 4:
            print('The second door is not the ghost door.')
        elif hint_num == 5:
            print('I don\'t know, figure it out yourself.')
    elif ghost_door ==  3 and door_hint == ghost_door:
        if hint_num == 1:
            print('You hear an eerie silence from behind the last door.')
        elif hint_num == 2:
            print('You sense an ominous presense from behind the last door.')
        elif hint_num == 3:
            print('You see a sinister light coming from behind the last door.')
        elif hint_num == 4:
            print('The last door is not the ghost door.')
        elif hint_num == 5:
            print('I don\'t know, figure it out yourself.')
    #Get users input for which door they will open and make sure it is an integer
    print('Which door will you open?')
    while num_input == False:
        door = input('1, 2, 3? ')
        try:
            door_num = int(door)
            num_input = True
        except:
            print("Please input a number!")
    #Check if the user has chosen the ghost door or not
    if door_num == 1 or door_num == 2 or door_num == 3:
        if door_num == ghost_door:
          print('Ghost!')
          feeling_brave = False
          print('Run away!')
          print('Game Over! ' + name + ' scored: ', score, end='.\n')
          #Check if user wants to try again, if yes reset loop and if no end game
          again = input('Play again? y/n ')
          if again == 'y':
             print('Ghost Game')
             score = 0
             num_input = False
             feeling_brave = True
          else:
             print('Not brave enough huh?')
             print('Come back when you\'re brave enough to try again.')
             #Show the highscores from the leaderboard
             for i in range(1,10):
                 if score >= int(highscores_score[i]):
                     print('New highscore!')
                     highscores_name.insert((i), name)
                     highscores_score.insert((i), score)
                     highscores_name.pop()
                     highscores_score.pop()
                     break
             for i in range(11):
                 print(highscores_name[i], '\t', highscores_score[i])
             file_open = open("Leaderboard_Names.txt", "w")
             highscores_name = str(highscores_name).replace("[", "")
             highscores_name = highscores_name.replace("]", "")
             highscores_name = highscores_name.replace("'", "")
             highscores_name = highscores_name.replace(" ", "")
             highscores_name = file_open.write(highscores_name)
             file_open.close()
             file_open = open("Leaderboard_Scores.txt", "w")
             highscores_score = str(highscores_score).replace("[", "")
             highscores_score = highscores_score.replace("]", "")
             highscores_score = highscores_score.replace("'", "")
             highscores_score = highscores_score.replace(" ", "")
             highscores_score = file_open.write(highscores_score)
             file_open.close()
        else:
             print('No ghost!')
             print('You enter the next room.')
             num_input = False
             #Add points to score total and continue game
             if door_num != door_hint and door_hint != ghost_door:
                 score = score + 2
             else:
                 score = score + 1
    else:
        print('Press 1, 2 or 3 to continue.')
        #Reset and continue from game loop
        feeling_brave = False
        num_input = False
        score = 0
        feeling_brave = True
