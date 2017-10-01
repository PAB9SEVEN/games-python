import random
global again,again1,again2
global count
count=0
def play():
    print "1:STONE"
    print "2:PAPER"
    print "3:SCISSORS"
    comp=random.randrange(1,3)
    userchoice=raw_input("Enter your choice")
    
    if(comp==1):
        
        
      print "computer has selected stone"
      if(userchoice==1):
          
          print "user has selected stone"
          print "Tie"
      elif(userchoice==2):
          print "user has selected paper"
          print "Oooo you win  :)"
      else:
          print "user has selected scissors"
          print "Aghh..computer wins again :/"
      #else:
          #print "INVALID INPUT PLEASE CHECK"
    
      again=raw_input("do you still want to play")
      if(again.upper()=="YES"):
          global count
          count+=1
      
     
    elif(comp==2):
      
      print "computer has selected paper"
      if(userchoice==1):
          print "user has selected stone"
          print " Aghh..computer wins  :/"
      elif(userchoice==2):
          print "you have selected paper"
          print "Tie"
      else:
          print "you have selected scissors"
          print "you win"
      #else:
       #   print "INVALID INPUT PLEASE CHECK"
          
        
      again1=raw_input("do you still want to play?")
      if(again1.upper()=="YES"):
          global count
          count+=1
    else:
      print "computer has selected scissors"
      if(userchoice==1):
          print "user has selected stone"
          print " Oooo..you win  :/"
      elif(userchoice==2):
          print "you have selected paper"
          print "Aghh..computer wins"
      else:
          print "you have selected scissors"
          print "Tie"
      #else:
       #   print "INVALID INPUT PLEASE CHECK"
          
      again2=raw_input("do you still want to play?")
      if(again2.upper()=="YES"):
          global count
          count+=1

print "HELLO"
print "Welcome..!Lets start playing.."
print "Press YES for playing and NO for quiting"
user=raw_input("enter your choice")
if user.upper()=="YES":
    print "Well lets get started"
    play()
else:
    print "Ok ByeBye.."
    

while(count>0):
    play()
print "fine goodbye have a nice day"
    
