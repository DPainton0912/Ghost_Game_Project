from pathlib import Path
def Return_Score_Path():
  score_path = Path("Common/Leaderboards/Leaderboard_Scores.txt")
  return(score_path)
def Return_Name_Path():
  names_path = Path("Common/Leaderboards/Leaderboard_Names.txt")
  return(names_path)
def List_Concanating(InputList):
  unrefined_List = InputList
  unrefined_List = str(unrefined_List).replace("[", "")
  unrefined_List = unrefined_List.replace("]", "")
  unrefined_List = unrefined_List.replace("'", "")
  unrefined_List = unrefined_List.replace(" ", "")
  return(unrefined_List)
def Find_Highscore_Names():
  path_Names = Return_Name_Path()
  highscores_name = path_Names.read_text()
  highscores_name_list = highscores_name.split(",")
  return(highscores_name_list)
def Find_Highscores_Scores():
  path_Scores = Return_Score_Path()
  highscores_score = path_Scores.read_text()
  highscores_score_list = highscores_score.split(",")
  return(highscores_score_list)
def Display_Highscores(CurrentScore,PName):
  Names = Find_Highscore_Names()
  Scores = Find_Highscores_Scores()
  path_Names = Return_Name_Path()
  path_Scores = Return_Score_Path()
  for i in range(1,10):
    if CurrentScore >= int(Scores[i]):
      print("New highscore!")
      Names.insert((i), PName)
      Scores.insert((i), CurrentScore)
      Names.pop()
      Scores.pop()
      break
  for i in range(11):
    print(Names[i], "\t", Scores[i])
    path_Names.write_text(List_Concanating(Names))
    path_Scores.write_text(List_Concanating(Scores))