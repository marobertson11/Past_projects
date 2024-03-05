import os
import time
print("\t\t\t This is Hangman")#create the design of the hangman
board=['___________','|         |','|         ','|         ',"|","|"]
st=('%s\n%s\n%s\n%s\n%s\n%s\n%s\n'%(board[0],board[1],board[1],board[2],board[3],board[4],board[5]))
print(st) # print design
blank= ' ' #decimal value is 32 for a space -> ord(blank)
word=input("Enter a word or phrase: ")
Liset=[]
char=[]
char=word#list holding correct word
char=([word[i:i+1] for i in range(0, len(word), 1)]) 
os.system('clear')
num=len(word)
good=0
lines="\t"
ct=0#basic counting variable
while ct!=num:
  if char[ct]!=blank: #not a space
    ct+=1#move forward
    Liset.append("_")#add an underline
  else:#there is a space
    ct+=1
    good+=1
    Liset.append("  ")#double space
  lines=lines+Liset[ct-1] + " " #add the new lines
ct=0#resue counting variable
bad=0#bad guesses
print(st,'\n',lines,'\n')#print the design of the hangman and the lines for word
while True:
  gset=[]#list of guesses already guessed
  while bad<6:
    guess=input("Enter a letter: ")
    if guess not in gset:#not already chosen
      gset.append(guess)#add it to the list
      if guess.lower() in char or guess.upper() in char:#non-case sensitive
        print ("The letter entered is in the word")
        c1=0#counting variable
        while c1<len(char):
          if guess.lower()==char[c1]:
            Liset[c1]=guess.lower()#add letter to underlined word in lowercase
            good+=1
          elif guess.upper()==char[c1]:
            Liset[c1]=guess.upper()##add letter to underlined word in uppercase
            good+=1
          c1+=1#move along
        if good==len(char):#got all of the letters
          time.sleep(2)
          os.system('clear')
          print("You have choosen all of the letters")
          break
      else:#wrong letter
        print("What if i told you you were wrong?")
        bad+=1
      ct=0
      lines="\t"
      while ct!=len(Liset):
        lines=lines + Liset[ct] + " "
        ct+=1
    elif guess in gset:
      print("You've already guessed this")
    time.sleep(1.5)
    os.system('clear')
    if bad==1:#all of the bad guess's consequences
      board[2]='|         O'
    elif bad==2:
      board[3]='|         |'
    elif bad==3:
      board[3]='|         |\\'
    elif bad==4:  
      board[3]="|        /|\\"
    elif bad==5:
      board[4]='|          \\'
    elif bad==6:
      board[4]='|        / \\'
      print("\nYou have killed this person \n The phrase or word was",word)
    st=('%s\n%s\n%s\n%s\n%s\n%s\n%s'%(board[0],board[1],board[1],board[2],board[3],board[4],board[5]))
    print(st,'\n\n',lines,'\n\t')#print design and lines
    print("You have previously guessed: ", end="")#print guesses
    for i in gset:
      print(i, end=" ")
    print()
  break
if good==len(char):#all done
  ct=0
  lines=""
  while ct!=len(Liset):
          lines=lines + Liset[ct] + " "
          ct+=1
  st=('%s\n%s\n%s\n%s\n%s\n%s\n%s'%(board[0],board[1],board[1],board[2],board[3],board[4],board[5]))

  print(st,"\n\n",lines)