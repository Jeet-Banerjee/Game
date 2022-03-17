print("Team:INDIA")
print("Enter no.of players played in different format")
Num = int(input())
for i in range (0 ,Num):
  name = str(input("Enter the player Name:"))
  age = int(input("Enter the age of the player:"))
  format = str(input("playing format of the player:"))
  score = []
  runs=int(input("Total runs made in that particular format:"))
  runs = int(input("Highest Runs Scored:"))
  country = str(input("Highest Runs Scored Vs Country:"))
  matches = int(input("Total no.of matches played:"))
  score.append(runs)

  six = int(input("Total Sixers:"))
  score.append(six)

  st_rate = float(input("Maximum Strike Rate:"))
  score.append(st_rate)
 
