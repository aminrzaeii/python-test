#amin rezaei
#rock_paper_scissor_game
a = str(input("whats your name? :"))
b = str(input("whats your name? :"))
print(f"hi {a} and {b} welcome to the game")
print("ok rock? paper? scissor?")
player1 = input("please make your move {a} : ")
player2 = input("Please make your move {b} : ")
if player1 == "rock" and player2 == "rock" :
  print("Try again")
elif player1 == "rock" and player2 == "paper" :
   print(f"{b} is the winner")
elif player1 == "rock" and player2 == "scissor" :
  print(f"{a} is the winner")
elif player1 == "paper" and player2 == "rock" :
 print(f"{a} is the winner")
elif player1 == "paper" and player2 == "paper" :
  print("try again")
elif player1 == "paper" and player2 == "scissor":
 print(f"{b} is the winner")
elif player1 == "scissor" and player2 == "rock" :
 print(f"{b} is the winner")
elif player1 == "scissor" and player2 == "paper" :
 print(f"{a} is the wineer")
elif player1 == "scissor" and player2 == "scissor" :
 print("try again")
else :
 print(end)
