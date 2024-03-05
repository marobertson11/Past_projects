##import time
#*ogStr=[]
#newStr=[]
#ogStr=input("Enter Original String: ")
#newStr=input("Enter New String: ")
#startTime=time.time()
#if(len(ogStr) != len(newStr)):
#  print("Length of the original string is", len(ogStr), "and the length of the new #string is", len(newStr))
#  print("Lengths of the two strings do not match.")
 # endTime=time.time()
#  totalTime=endTime-startTime
#  print(totalTime, "is the total time to calculate this example")
#  quit()
#
#for i in range(0,len(ogStr)):
#  print("Original String[i]:", ogStr[i], " and New String[i]:", newStr[i])
#  if(ogStr[i] != newStr[i]):
#    print("The strings does not match at index placement", i)
#    endTime=time.time()
#    totalTime=endTime-startTime
#    print(totalTime, "is the total time to calculate this example")
#    quit()

#print("The strings do match")
#endTime=time.time()
#totalTime=endTime-startTime
#print(totalTime, "is the total time to calculate this example")
#quit()

#search a list of strings for a specific string

#This program will go throught a string and locate another string that has been entered

def string_search(string, sub_str):
  needPrint = True
  counter=0
  long_sub=sub_str
  print(string)
  print(sub_str)
  for i in range(0,len(string) - len(sub_str) + 1):
    index = i
    for j in range(0,len(sub_str)):
      #These 3 lines are optional
      if(needPrint):
        print(string)
        print(long_sub)
        
      if string[index] == sub_str[j]:
        index += 1
        counter+=1
        needPrint = False
      else:
        long_sub=" " + long_sub
        needPrint = True
        break
      if counter == len(sub_str):
        return i
  return -1

string_in = input("Enter full string: ")
sub_str_in = input("Enter sub string to search: ")
match=sub_str_in
#string_in = "1234 56"
#sub_str_in = "5"

#Visualization Stuff
counter  = 0
limit = len(string_in) - len(sub_str_in)



#runs search Algorithm 
res = string_search(string_in, match)
#print("Found Match at:" + res)
if(res!=-1):
  print("Index: ",res, " is where '",match,"' starts in the full string", sep='')
else:
  print("The matching string was not in the full string")