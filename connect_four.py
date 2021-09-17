def possibility():
  if (pos_i == 5):
    return True
  if (board[pos_i+1][pos_j] != "  "):
    return True
  return False 

def check():
  for i in range(6):
    for j in range(3):
      if (board[i][j] == board[i][j+1] ==
      board[i][j+2] == board[i][j+3] != "  "):
        return True
  for j in range(6):
    for i in range(3):
      if (board[i][j] == board[i+1][j] ==
      board[i+2][j] == board[i+3][j] != "  "):
        return True   
  for i in range(0, 3):
    for j in range(0, 3):
      if (board[i][j] == board[i+1][j+1] ==
      board[i+2][j+2] == board[i+3][j+3] != "  "):
        return True
  for i in range(0, 3):
    for j in range(3, 6):
      if (board[i][j] == board[i+1][j-1] ==
      board[i+2][j-2] == board[i+3][j-3] != "  "):
        return True
  return False
   
def cout():
  for i in range(6):
    print(" "*4 + str(i+1), end="")
  print(), print(" "*2 + "+----"*6 + "+")
  for i in range(6):
    print(i+1, end= " ")
    for j in range(6):
      print("| " + board[i][j], end=" ")
    print("| " + str(i+1))
    print(" "*2 + "+----"*6 + "+")
  for i in range(6):
    print(" "*4 + str(i+1), end="")
  print()

print("This is the game connect four:")
count, board = 36, [["  "]*6 for i in range(6)]
cout()

while(count):
  pos_i = int(input(("First" if (count % 2 == 0) else "Second") + 
  " player, enter the line number:")) - 1
  pos_j = int(input(("First" if (count % 2 == 0) else "Second") + 
  " player, enter the column number:")) - 1
  if (possibility()):
    board[pos_i][pos_j] = "x " if (count % 2 == 0) else "o "
    cout()
    if (check()): break
    count -= 1

if (count > 0):
  print(("First" if (count % 2 == 0) else "Second") + 
  " player won")
else:
  print("Friendship won")