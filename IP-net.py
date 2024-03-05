import os
import time
import math

def determineIncrement(cidr):
  netInc1=[8,16,24,32]
  netInc2=[7,15,23,31]
  netInc4=[6,14,22,30]
  netInc8=[5,13,21,29]
  netInc16=[4,12,20,28]
  netInc32=[3,11,19,27]
  netInc64=[2,10,18,26]
  netInc128=[1,9,17,25]

  if cidr in netInc1:
    return 256
  elif cidr in netInc2:
    return 2
  elif cidr in netInc4:
    return 4
  elif cidr in netInc8:
    return 8
  elif cidr in netInc16:
    return 16
  elif cidr in netInc32:
    return 32
  elif cidr in netInc64:
    return 64
  elif cidr in netInc128:
    return 128
  elif cidr not in range (1,33):
    return 0

def validate(myIP):
  octets=myIP[0]
  cidr=myIP[1]
  octet1=octets[0]
  octet2=octets[1]
  octet3=octets[2]
  octet4=octets[3]

  if octet1.isdigit():
    octet1=int(octet1)
  else:
    return False
  if octet2.isdigit():
    octet2=int(octet2)
  else:
    return False
  if octet3.isdigit():
    octet3=int(octet3)
  else:
    return False
  if octet4.isdigit():
    octet4=int(octet4)
  else:
    return False
  if cidr.isdigit():
    cidr=int(cidr)
  else:
    return False
  if octet1 not in range(255):
    return False
  if octet2 not in range(256):
    return False
  if octet3 not in range(256):
    return False
  if octet4 not in range(256):
    return False
  if cidr not in range(1,32):
    return False
  return True

def parseIP(strIP):
  per='.'
  if per in strIP:
    octets=strIP.split('.')
    if '/' in octets[3]:
      cidr=octets[3].split('/')
      octets[3]=cidr[0]
      strCIDR=cidr[1]
    else:
      print("Invalid CIDR notation")
      return
  else:
    print('Invalid IP!')
    return
  parsedIP=[]
  parsedIP.append(octets)
  parsedIP.append(strCIDR)
  return parsedIP
def dis_dir():
  print("""
                Submask Calculator
            When prompted enter an IP in dotted decimal
            form. The script will display the NFLB if the 
            subnet created.
            """)
def get_IP():
  ip=input("Enter IP in dotted decimal/CIDR notation: ")
  return ip
def sub(cidr):
  inc=[128,64,32,16,8,4,2,1]
  oct=math.floor(cidr/8)
  n=0
  per='.'
  mask=""
  while n!=oct:
    mask+='255.'
    n+=1
  net=0
  n=(cidr%8)-1
  while n>=0:
    net+=inc[n]
    n-=1
  mask+=str(net)
  ct=0
  for item in mask:
    if item == per:
      ct+=1
  while ct<3:
    mask+=".0"
    ct+=1
  return mask
  
def main():
  dis_dir()
  valid=False
  while not valid:
    myIP=get_IP()
    myNewIP=parseIP(myIP)
    if len(myNewIP)==2:
      valid=validate(myNewIP)
    if not valid:
      print("Something went wrong with the validation")
      exit(1)
    octets=myNewIP[0]
    octet1=int(octets[0])
    octet2=int(octets[1])
    octet3=int(octets[2])
    octet4=int(octets[3])
    cidr=int(myNewIP[1])
    submask=sub(cidr)
    netInc=determineIncrement(cidr)
    if netInc==0:
      print("Invalid CIDR entered")

    if cidr>=24:
      netID=str(octet1) + '.' + str(octet2) + '.' + str(octet3) + '.'
      firstIP=netID
      lastIP=netID
      bdcstIP=netID
      networkID=int(math.floor(octet4/netInc)*netInc)
      netID+=str(networkID)
      firstIP+=str(networkID+1)
      lastIP+=str(networkID + netInc-2)
      bdcstIP+=str(networkID+netInc-1)
    elif cidr>=16:
      netID=str(octet1) + '.' + str(octet2) + '.'
      firstIP=netID
      lastIP=netID
      bdcstIP=netID
      networkID=int(math.floor(octet3/netInc)*netInc)
      netID+=str(networkID)+'.0'
      firstIP+=str(networkID+1)+'.1'
      lastIP+=str(networkID+netInc-1)+'.254'
      bdcstIP+=str(networkID+netInc-1)+'.255'
    elif cidr>=8:
      netID=str(octet1) + '.'
      firstIP=netID
      lastIP=netID
      bdcstIP=netID
      networkID=int(math.floor(octet2/netInc)*netInc)
      netID+=str(networkID)+'.0'+'.0'
      firstIP+=str(networkID+1)+'.0'+'.1'
      lastIP+=str(networkID+netInc-1)+'.255'+'.254'
      bdcstIP+=str(networkID+netInc-1)+'.255'+'.255'
    elif cidr>=1:
      networkID=int(math.floor(octet1/netInc)*netInc)
      netID=str(networkID)+'.0'+'.0'+'.0'
      firstIP=str(networkID+1)+'.0'+'.0'+'.1'
      lastIP=str(networkID+netInc-1)+'.255'+'.255'+'.254'
      bdcstIP=str(networkID+netInc-1)+'.255'+'.255'+'.255'
    print("IP %d.%d.%d.%d results in NFLB as follows: \n\n" %(octet1,octet2,octet3,octet4))
    print("NetID: \t\t%s \nFirst: \t\t%s\nLast: \t\t%s\nBdcst: \t\t%s\nSubmask: \t%s\nIncrement: \t%d" %(netID,firstIP,lastIP,bdcstIP,submask,netInc))
    time.sleep(5)
    
while __name__=="__main__":
  main()


