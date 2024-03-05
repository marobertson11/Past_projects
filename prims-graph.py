def beenThereDoneThat(vertex, newCity): #Check to see if we have visited this city
  for item in vertex:
    if newCity == item:
      return True
  return False

def newLocation(locations,city): #Creates List of all vertices and where their index starts
  for i in range(0,len(locations)):
    if(locations[i][0] == city):
      return int(locations[i][1])

def totalWeight(daList):#add total weight of visited cities
  sum=0
  for item in daList:
    sum+=int(item.split()[2])
  return sum

def whereTheyAt(statement): #shows where each new starting city starts 
  arrangement=[]
  lineA = statement[0].split()[0]
  arrangement.append([lineA, 0])
  for index in range(0,len(statement)-1):
    if(statement[index].split()[0] != lineA):
      lineA = statement[index].split()[0]
      arrangement.append([lineA,index])
  return arrangement

#open and read file
f = open("./city-pairs.txt", 'r')
statement = f.readlines()
f.close()
#set up variables
edges=[]
shortList=[]
vertex=[]
counter=0
minWeight=600
minIndex=0
vertex.append(statement[0].split()[0])
lineA = statement[0].split()[0]
index=0
stillRunning = True
totalLength=len(statement)
locations = whereTheyAt(statement)
#go through lines
while stillRunning:
  if(index == totalLength): 
    #go through section to determine what was the smallest 
    edgeLength = len(edges)
    for i in range(0,edgeLength):
      if int(edges[i][2]) < minWeight:
        if(beenThereDoneThat(vertex,edges[i][1]) == False):
          minIndex = i
          minWeight = int(edges[i][2])
        elif(beenThereDoneThat(vertex,edges[i][1]) == True):
          if(shortList[-1].split()[0] != edges[i][1] and shortList[-1].split()[1] == edges[i][0]):
            if(int(shortList[-1].split()[2]) > int(edges[i][2])) :
              shortList.pop()
              shortList.append(statement[(index-(edgeLength-i))])
    shortList.append(statement[(index-(edgeLength-minIndex))])
    index = newLocation(locations,edges[minIndex][1]) - 1
    lineA = statement[index+1].split()[0] 
    vertex.append(lineA)
    edges=[]  
    minWeight=600
    minIndex=0
  elif(statement[index].split()[0] == lineA): # still a part of the edges of that vertex
    edges.append(statement[index].split())
  elif(statement[index].split()[0] != lineA): 
    #go through section to determine what was the smallest 
    edgeLength = len(edges)
    for i in range(0,edgeLength):
      if int(edges[i][2]) < minWeight:
        if(beenThereDoneThat(vertex,edges[i][1]) == False):
          minIndex = i
          minWeight = int(edges[i][2])
        elif(beenThereDoneThat(vertex,edges[i][1]) == True):
          if(shortList[-1].split()[0] != edges[i][1] and shortList[-1].split()[1] == edges[i][0]):
            if(int(shortList[-1].split()[2]) > int(edges[i][2])) :
              shortList.pop()
              shortList.append(statement[(index-(edgeLength-i))])
    shortList.append(statement[(index-(edgeLength-minIndex))])
    index = newLocation(locations,edges[minIndex][1]) - 1
    lineA = statement[index+1].split()[0] 
    vertex.append(lineA)
    edges=[]  
    minWeight=600
    minIndex=0
  index += 1
  if len(vertex) > len(locations):
    stillRunning = False

shortList.pop()
#output results to file
totWeight = totalWeight(shortList)
o = open("./Prim-graph.txt", 'w')
o.write("----- Shortest length -----\n")
for item in shortList:
  o.write(item)
o.write("\nTotal Weight: %d" %(totWeight) )
o.close()