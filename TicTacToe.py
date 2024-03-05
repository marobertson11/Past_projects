def openspace(att,play,lisT):
  if play==1:
      if att==1:
          lisT[9]='  X  |'
      elif att==2:
          lisT[10]='  X  |'
      elif att==3:
          lisT[11]='  X  '
      elif att==4:
          lisT[6]='  X  |'
      elif att==5:
          lisT[7]='  X  |'
      elif att==6:
          lisT[8]='  X  '
      elif att==7:
          lisT[2]='  X  |'
      elif att==8:
          lisT[3]='  X  |'
      elif att==9:
          lisT[4]='  X  '
  elif play==2:
      if att==1:
          lisT[9]='  O  |'
      elif att==2:
          lisT[10]='  O  |'
      elif att==3:
          lisT[11]='  O  '
      elif att==4:
          lisT[6]='  O  |'
      elif att==5:
          lisT[7]='  O  |'
      elif att==6:
          lisT[8]='  O  '
      elif att==7:
          lisT[2]='  O  |'
      elif att==8:
          lisT[3]='  O  |'
      elif att==9:
          lisT[4]='  O  '
  return(lisT)

def checkPlay(play,pieceList,sets,xplay,oplay):
  que=input('Do you want to play again? yes/Yes/y for yes or no/No/n for no\n->')
  if (que=="yes" or que=="Yes"or que=="y"):
      pieceList={1:'     |     |     ',2:'     |',3:'     |',4:'     ',5:'_____|_____|_____',6:'     |',7:'     |',8:'     ',9:'     |',10:'     |',11:'     '}
      sets=[]
      xplay=[]
      oplay=[]
      showBoard(pieceList)
      play=1
      game(play,pieceList,sets,xplay,oplay)
  elif (que=="no" or que=="No" or que=="n"):
      return False
  
def checkwin(colist):
  if (1 in colist and 2 in colist and 3 in colist):
      return True
  elif (1 in colist and 4 in colist and 7 in colist):
      return True
  elif (1 in colist and 5 in colist and 9 in colist):
      return True
  elif (4 in colist and 5 in colist and 6 in colist):
      return True
  elif (2 in colist and 5 in colist and 8 in colist):
      return True
  elif (7 in colist and 8 in colist and 9 in colist):
      return True
  elif (3 in colist and 5 in colist and 7 in colist):
      return True
  elif (3 in colist and 6 in colist and 9 in colist):
      return True   
  else: 
      return False
  
def showBoard(board):
  st=('%s\n%s%s%s\n%s\n%s\n%s%s%s\n%s\n%s\n%s%s%s\n%s'%(board[1],board[2],board[3],board[4],board[5],board[1],board[6],board[7],board[8],board[5],board[1],board[9],board[10],board[11],board[1]))
  print(st)
  
def game(play,pieceList,sets,xplay,oplay):
  stilPlay=True
  che=[1,2,3,4,5,6,7,8,9]
  while stilPlay==True:
      print('The Choices go as so...\n7 is the top left corner\t\t8 is the top middle\t\t9 is the top right choice\n4 is the middle left\t\t\t5 is the center box\t\t6 is the middle right\n1 is the bottom left corner\t\t2 is the bottom middle\t3 is the bottom right corner')
      if play ==1:            
          print('It is Player 1s turn')
          gu=int(input('Which spot would you like to take?\n->'))
          if gu not in sets: 
              print('You have chosen %d'%(gu))
              res=int(input('Are you sure this is the spot you want? Enter 1 for yes or 2 for no  '))
              if res!=1:
                  game(play,pieceList,sets,xplay,oplay)
              else:
                  pieceList=openspace(gu,play,pieceList)        
                  showBoard(pieceList)
                  play=2
                  sets.append(gu)
                  xplay.append(gu)
                  sets.sort()
                  if checkwin(xplay)==True:
                      print('Player 1 has won\nCongrats')
                      stilPlay=checkPlay(play,pieceList,sets,xplay,oplay)
          elif gu in sets:
              print("That choice has already been chosen")
              game(play,pieceList,sets,xplay,oplay)
          if che==sets:
              print('Stalemate')
              stilPlay=checkPlay(play,pieceList,sets,xplay,oplay)
          
      elif play== 2:
          print('It is Player 2s turn')
          gu=int(input('Which spot would you like to take?\n->'))
          if gu not in sets: 
              print('You have chosen %d'%(gu))
              res=int(input('Are you sure this is the spot you want? Enter 1 for yes or 2 for no  '))
              if res!=1:
                  game(play,pieceList,sets,xplay,oplay)
              else:
                  pieceList=openspace(gu,play,pieceList)        
                  showBoard(pieceList)
                  play=1
                  sets.append(gu)
                  oplay.append(gu)
                  sets.sort()
                  if checkwin(oplay)==True:
                      print('Player 2 has won\nCongrats')
                      stilPlay=checkPlay(play,pieceList,sets,xplay,oplay)
          elif gu in sets:
              print("That choice has already been chosen")
              game(play,pieceList,sets,xplay,oplay)
          if che==sets:
              print('Stalemate')
              stilPlay=checkPlay(play,pieceList,sets,xplay,oplay)
      
play=1
pieceList={1:'     |     |     ',2:'     |',3:'     |',4:'     ',5:'_____|_____|_____',6:'     |',7:'     |',8:'     ',9:'     |',10:'     |',11:'     '}
sets=[]
xplay=[]
oplay=[]
print('This is the game of Tic Tac Toe\nPlayer 1 will be Xs and Player 2 will be Os ')
print("This is the playing board:'")
showBoard(pieceList)
game(play,pieceList,sets,xplay,oplay)