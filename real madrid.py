#amin rezaei
print("Here's a football team that we want players to know it in any post for example real madrid")
list = ["coach" , "GK" , "CB" , "CMF" , "CF"]
Name = {
      "coach" : "Ancelotti" ,
      "GK" : "kepa" ,
      "CB" : "Rüdiger" ,
      "CMF" : "kroos" ,
      "CF" : "vini"
}
a = str(input("Choose a post : "))
if a == "coach" :
 print("Coach of the team : " , Name["coach"])
elif a == "GK" :
 print("The keeper of this team : " , Name["kepa"])
elif a == "CB" :
  print("The defender of this team : " , Name["CB"])
elif a == "CMF" :
 print("The midfielder of this team : " , Name["CMF"])
else :
 print("The striker of this team : " , Name["CF"])
