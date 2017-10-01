import time
import sys
import random
global fill
global board
board=[0,1,2,
       3,4,5,
       6,7,8]
    
#def update_board():
def show():
    
    print board[0],'|',board[1],'|',board[2]
    print '----------'
    print board[3],'|',board[4],'|',board[5]
    print '----------'
    print board[6],'|',board[7],'|',board[8]
    print '----------'
    
def start_game():
   
    global count
    global user_no
    global computer_no
    #global fill
    global no_used
    no_used=[]
    global board

    fill=True
    while fill:
      #print board[0]
        #print board[1]
        
        #count=0
        #user_choice=raw_input('Your choice-->X/O')
        computer_no=random.randrange(0,8)
        user_no=int(input("Enter the spot"))

        while(computer_no==user_no):
            computer_no=random.randrange(0,8)
            
        while(user_no in no_used):
            user_no=int(input("Enter the spot"))
        while(computer_no in no_used):
            computer_no=random.randrange(0,8)
        
        no_used.append(user_no)
        no_used.append(computer_no)
        #print computer_no
        #print user_no
        #print no_used
        board[user_no]='X'
        board[computer_no]='O'
        print board[user_no]
        print board[computer_no]
        if(board[0]=='X' and board[1]=='X' and board[2]=='X' or board[3]=='X' and board[4]=='X' and board[5]=='X' or board[6]=='X' and board[7]=='X' and board[8]=='X' or board[0]=='X' and board[4]=='X' and board[8]=='X' or board[2]=='X' and board[4]=='X' and board[6]=='X' or board[0]=='X' and board[3]=='X' and board[6]=='X' or board[1]=='X' and board[4]=='X' and board[7]=='X' or board[2]=='X' and board[5]=='X' and board[8]=='X'):
            fill=False
            print "You win.."
        
        elif(board[0]=='O' and board[1]=='O' and board[2]=='0' or board[3]=='O' and board[4]=='O' and board[5]=='O' or board[6]=='O' and board[7]=='O' and board[8]=='O' or board[0]=='O' and board[4]=='O' and board[8]=='O' or board[2]=='O' and board[4]=='O' and board[6]=='O' or board[0]=='O' and board[3]=='O' and board[6]=='O' or board[1]=='O' and board[4]=='O' and board[7]=='O' or board[2]=='O' and board[5]=='O' and board[8]=='O' ):
            fill=False
            print "Computer wins"
        else:
            fill=True

        show()                                                                                                                                                                                                                        

        
def main():
    start_game()

main()
    
