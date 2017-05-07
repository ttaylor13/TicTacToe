#Tim Taylor
#Project 4 question 1
#CS133

import random

#Initialize variables
permission = 'yes'
choices = list()
win = 0
lose = 0
tie = 0
cpuTurn = 0
chosenAlready = list()
turns = 0
didCpuWin = False

gridTop = '-'*8 + '|' + '-'*8 + '|' + '-'*8
gridMid = ' '*8 + '|' + ' '*8 + '|'

#Define functions
def putInLeter(a1,a2,a3):
    letterIn = ' '*3 + a1 + ' '*4 + '|' + ' '*4 + a2 + ' '*3 + '|' + ' '*4 + a3
    return letterIn

def cpuMove(move):
    boardValues[move] = 'X'
    moveStr = str(move)
    chosenAlready.append(moveStr)
    print('The computer chose ' + str(move) + '.')
    print(gridMid  + '\n' + putInLeter(boardValues[1],boardValues[2],boardValues[3]) + '\n' + gridMid  + '\n' +  gridTop
    + '\n' + putInLeter(boardValues[4],boardValues[5],boardValues[6]) + '\n' + gridMid+ '\n' + gridTop + '\n' + gridMid + '\n' + putInLeter(boardValues[7],boardValues[8],boardValues[9]) + '\n' + gridMid)
            
           

def didCpuWin():
    if (boardValues[1] == 'X' and boardValues[2] == 'X' and boardValues[3] == 'X') or(boardValues[4] == 'X' and boardValues[5] == 'X' and boardValues[6] == 'X')or(boardValues[7] == 'X' and boardValues[8] == 'X' and boardValues[9] == 'X')or(boardValues[1] == 'X' and boardValues[4] == 'X' and boardValues[7] == 'X')or(boardValues[2] == 'X' and boardValues[5] == 'X' and boardValues[8] == 'X')or(boardValues[3] == 'X' and boardValues[6] == 'X' and boardValues[9] == 'X')or(boardValues[1] == 'X' and boardValues[5] == 'X' and boardValues[9] == 'X')or(boardValues[3] == 'X' and boardValues[5] == 'X' and boardValues[7] == 'X'):
         print('\n' + 'The computer won.' + '\n')
         didCpuWin = True
         return didCpuWin        

#Main program code
print('\n' + 'Welcome to the game of Tic-Tac-Toe!' + '\n')
while permission == 'yes':
  boardValues = {1:'1',2:'2',3:'3',4:'4',5:'5',6:'6',7:'7',8:'8',9:'9'}
  print(gridMid  + '\n' + putInLeter(boardValues[1],boardValues[2],boardValues[3]) + '\n' + gridMid  + '\n' +  gridTop  + '\n' + putInLeter(boardValues[4],boardValues[5],boardValues[6])
  + '\n' + gridMid+ '\n' + gridTop + '\n' + gridMid + '\n' + putInLeter(boardValues[7],boardValues[8],boardValues[9]) + '\n' + gridMid)
  
  while cpuTurn != -1 and turns <=9:
     while True:
          #player's turn
          if cpuTurn == 0:          
            while True:
              print('Enter a number from the grid or enter 10 to end round: ')         
              try:
                  playerInput = int(input())
                  if playerInput > 10 or playerInput <= 0:
                    print("Number entered out of requested range.")#re-ask first question if out of range
                    continue
                  else:
                      cpuTurn = 1
              except ValueError:
                      print("Please enter an integer.")
                      continue
              if playerInput == 10:
                print('\n' + 'Round ended.' + '\n')
                cpuTurn = -1
                break
              else:
                playerInputStr = str(playerInput)
                if playerInputStr not in chosenAlready:
                  boardValues[playerInput] = 'O'
                  chosenAlready.append(playerInputStr)
                  print('Player chose ' + playerInputStr + '.')
                  turns += 1
                  print(gridMid  + '\n' + putInLeter(boardValues[1],boardValues[2],boardValues[3]) + '\n' + gridMid  + '\n' +  gridTop
                  + '\n' + putInLeter(boardValues[4],boardValues[5],boardValues[6]) + '\n' + gridMid+ '\n' + gridTop + '\n' + gridMid + '\n' + putInLeter(boardValues[7],boardValues[8],boardValues[9]) + '\n' + gridMid)
                  if (boardValues[1] == 'O' and boardValues[2] == 'O' and boardValues[3] == 'O') or(boardValues[4] == 'O' and boardValues[5] == 'O' and boardValues[6] == 'O')or(boardValues[7] == 'O' and boardValues[8] == 'O' and boardValues[9] == 'O')or(boardValues[1] == 'O' and boardValues[4] == 'O' and boardValues[7] == 'O')or(boardValues[2] == 'O' and boardValues[5] == 'O' and boardValues[8] == 'O')or(boardValues[3] == 'O' and boardValues[6] == 'O' and boardValues[9] == 'O')or(boardValues[1] == 'O' and boardValues[5] == 'O' and boardValues[9] == 'O')or(boardValues[3] == 'O' and boardValues[5] == 'O' and boardValues[7] == 'O'):
                      print('\n' + 'You won!' + '\n')
                      cpuTurn = -1
                      win += 1
                      break
                  break
                else: 
                  print('That box is aready chosen. Please choose an availible box.')
                  continue
                
          #computer's turn               
          if cpuTurn == 1:
              while True:                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              
                  cpuInput = random.randint(1,9)
                  cpuInputStr = str(cpuInput)
                  
    #end in a tie********************************************************************************************************************************************************************************************
                  
                  if turns == 9:
                      turns = 10
                      break

     #computer's first move***************************************************************************************************************************************************************************************************


                  elif turns == 1 and '5' not in chosenAlready:
                      turns += 1
                      cpuMove(5)
                      cpuTurn = 0
                      break
                        
                  elif turns == 1 and boardValues[5]=='O':
                      turns += 1
                      choices = [1,3,7,9]
                      move = random.choice(choices)
                      cpuMove(move)                                                                            
                      cpuTurn = 0
                      break
                          
                        
     #Computer's move for special cases************************************************************************************************************************************************************************************
                        
                  elif ((boardValues[1]=='O' and boardValues[9]=='O' and boardValues[5]=='X' and turns == 3) or (boardValues[3]=='O' and boardValues[7]=='O' and boardValues[5]=='X' and turns == 3)) and ('2' not in chosenAlready or '4' not in chosenAlready or '6' not in chosenAlready or '8' not in chosenAlready):
                      turns += 1
                      choices = [2,4,6,8]
                      move = random.choice(choices)
                      if move not in chosenAlready:
                          cpuMove(move)
                          cpuTurn = 0
                          break                                                                         

                  
                  elif (boardValues[7]=='O' and boardValues[5]=='O' and boardValues[3]=='X' and turns == 3) and ('9' not in chosenAlready):
                      turns += 1
                      cpuMove(9)
                      cpuTurn = 0
                      break  
                        
                  elif (boardValues[3]=='O' and boardValues[5]=='O' and boardValues[7]=='X' and turns == 3) and ('1' not in chosenAlready):
                      turns += 1
                      cpuMove(1)
                      cpuTurn = 0
                      break
                        
                  elif (boardValues[5]=='O' and boardValues[9]=='O' and boardValues[1]=='X' and turns == 3) and ('7' not in chosenAlready):
                      turns += 1
                      cpuMove(7)
                      cpuTurn = 0
                      break

                  elif (boardValues[1]=='O' and boardValues[5]=='O' and boardValues[9]=='X' and turns == 3) and ('3' not in chosenAlready):
                      turns += 1
                      cpuMove(3)
                      cpuTurn = 0
                      break
                        
 #computer's offense starts here************************************************************************************************************************************************************************
                        
                  elif (boardValues[2]=='X' and boardValues[5]=='X') and '8' not in chosenAlready:
                      turns += 1
                      cpuMove(8)
                      if didCpuWin() == True:
                          lose += 1
                          cpuTurn = -1
                          break
                      else:
                          cpuTurn = 0
                          break
                        
                  elif (boardValues[1]=='X' and boardValues[4]=='X') and '7' not in chosenAlready:
                      turns += 1
                      cpuMove(7)
                      if didCpuWin() == True:
                          lose += 1
                          cpuTurn = -1
                          break
                      else:
                          cpuTurn = 0
                          break
                      
                  elif (boardValues[3]=='X' and boardValues[2]=='X') and '1' not in chosenAlready:
                      turns += 1
                      cpuMove(1)
                      if didCpuWin() == True:
                          lose += 1
                          cpuTurn = -1
                          break
                      else:
                          cpuTurn = 0
                          break
                      
                  elif (boardValues[4]=='X' and boardValues[7]=='X') and '1' not in chosenAlready:
                      turns += 1
                      cpuMove(1)
                      if didCpuWin() == True:
                          lose += 1
                          cpuTurn = -1
                          break
                      else:
                          cpuTurn = 0
                          break
                      
                  elif (boardValues[2]=='X' and boardValues[8]=='X') and '5' not in chosenAlready:
                      turns += 1
                      cpuMove(5)
                      if didCpuWin() == True:
                          lose += 1
                          cpuTurn = -1
                          break
                      else:
                          cpuTurn = 0
                          break
                      
                  elif (boardValues[1]=='X' and boardValues[7]=='X') and '4' not in chosenAlready:
                      turns += 1
                      cpuMove(4)
                      if didCpuWin() == True:
                          lose += 1
                          cpuTurn = -1
                          break
                      else:
                          cpuTurn = 0
                          break
                      
                  elif (boardValues[2]=='X' and boardValues[5]=='X') and '8' not in chosenAlready:
                      turns += 1
                      cpuMove(8)
                      if didCpuWin() == True:
                          lose += 1
                          cpuTurn = -1
                          break
                      else:
                          cpuTurn = 0
                          break
                      
                  elif (boardValues[5]=='X' and boardValues[8]=='X') and '2' not in chosenAlready:
                      turns += 1
                      cpuMove(2)
                      if didCpuWin() == True:
                          lose += 1
                          cpuTurn = -1
                          break
                      else:
                          cpuTurn = 0
                          break
                      
                  elif (boardValues[2]=='X' and boardValues[8]=='X') and '5' not in chosenAlready:
                      turns += 1
                      cpuMove(5)
                      if didCpuWin() == True:
                          lose += 1
                          cpuTurn = -1
                          break
                      else:
                          cpuTurn = 0
                          break
                      
                  elif (boardValues[3]=='X' and boardValues[6]=='X') and '9' not in chosenAlready:
                      turns += 1
                      cpuMove(9)
                      if didCpuWin() == True:
                          lose += 1
                          cpuTurn = -1
                          break
                      else:
                          cpuTurn = 0
                          break
                      
                  elif (boardValues[6]=='X' and boardValues[9]=='X') and '3' not in chosenAlready:
                      turns += 1
                      cpuMove(3)
                      if didCpuWin() == True:
                          lose += 1
                          cpuTurn = -1
                          break
                      else:
                          cpuTurn = 0
                          break
                      
                  elif (boardValues[3]=='X' and boardValues[9]=='X') and '6' not in chosenAlready:
                      turns += 1
                      cpuMove(6)
                      if didCpuWin() == True:
                          lose += 1
                          cpuTurn = -1
                          break
                      else:
                          cpuTurn = 0
                          break
                      
                  elif (boardValues[1]=='X' and boardValues[2]=='X') and '3' not in chosenAlready:
                      turns += 1
                      cpuMove(3)
                      if didCpuWin() == True:
                          lose += 1
                          cpuTurn = -1
                          break
                      else:
                          cpuTurn = 0
                          break
                      
                  elif (boardValues[2]=='X' and boardValues[3]=='X') and '1' not in chosenAlready:
                      turns += 1
                      cpuMove(1)
                      if didCpuWin() == True:
                          lose += 1
                          cpuTurn = -1
                          break
                      else:
                          cpuTurn = 0
                          break
                      
                  elif (boardValues[1]=='X' and boardValues[3]=='X') and '2' not in chosenAlready:
                      turns += 1
                      cpuMove(2)
                      if didCpuWin() == True:
                          lose += 1
                          cpuTurn = -1
                          break
                      else:
                          cpuTurn = 0
                          break

                  elif (boardValues[4]=='X' and boardValues[5]=='X') and '6' not in chosenAlready:
                      turns += 1
                      cpuMove(6)
                      if didCpuWin() == True:
                          lose += 1
                          cpuTurn = -1
                          break
                      else:
                          cpuTurn = 0
                          break

                  elif (boardValues[5]=='X' and boardValues[6]=='X') and '4' not in chosenAlready:
                      turns += 1
                      cpuMove(4)
                      if didCpuWin() == True:
                          lose += 1
                          cpuTurn = -1
                          break
                      else:
                          cpuTurn = 0
                          break

                  elif (boardValues[4]=='X' and boardValues[6]=='X') and '5' not in chosenAlready:
                      turns += 1
                      cpuMove(5)
                      if didCpuWin() == True:
                          lose += 1
                          cpuTurn = -1
                          break
                      else:
                          cpuTurn = 0
                          break

                  elif (boardValues[7]=='X' and boardValues[8]=='X') and '9' not in chosenAlready:
                      turns += 1
                      cpuMove(9)
                      if didCpuWin() == True:
                          lose += 1
                          cpuTurn = -1
                          break
                      else:
                          cpuTurn = 0
                          break

                  elif (boardValues[8]=='X' and boardValues[9]=='X') and '7' not in chosenAlready:
                      turns += 1
                      cpuMove(7)
                      if didCpuWin() == True:
                          lose += 1
                          cpuTurn = -1
                          break
                      else:
                          cpuTurn = 0
                          break

                  elif (boardValues[7]=='X' and boardValues[9]=='X') and '8' not in chosenAlready:
                      turns += 1
                      cpuMove(8)
                      if didCpuWin() == True:
                          lose += 1
                          cpuTurn = -1
                          break
                      else:
                          cpuTurn = 0
                          break

                  elif (boardValues[1]=='X' and boardValues[5]=='X') and '9' not in chosenAlready:
                      turns += 1
                      cpuMove(9)
                      if didCpuWin() == True:
                          lose += 1
                          cpuTurn = -1
                          break
                      else:
                          cpuTurn = 0
                          break

                  elif (boardValues[5]=='X' and boardValues[9]=='X') and '1' not in chosenAlready:
                      turns += 1
                      cpuMove(1)
                      if didCpuWin() == True:
                          lose += 1
                          cpuTurn = -1
                          break
                      else:
                          cpuTurn = 0
                          break

                  elif (boardValues[1]=='X' and boardValues[9]=='X') and '5' not in chosenAlready:
                      turns += 1
                      cpuMove(5)
                      if didCpuWin() == True:
                          lose += 1
                          cpuTurn = -1
                          break
                      else:
                          cpuTurn = 0
                          break

                  elif (boardValues[3]=='X' and boardValues[5]=='X') and '7' not in chosenAlready:
                      turns += 1
                      cpuMove(7)
                      if didCpuWin() == True:
                          lose += 1
                          cpuTurn = -1
                          break
                      else:
                          cpuTurn = 0
                          break

                  elif (boardValues[5]=='X' and boardValues[7]=='X') and '3' not in chosenAlready:
                      turns += 1
                      cpuMove(3)
                      if didCpuWin() == True:
                          lose += 1
                          cpuTurn = -1
                          break
                      else:
                          cpuTurn = 0
                          break

                  elif (boardValues[3]=='X' and boardValues[7]=='X') and '5' not in chosenAlready:
                      turns += 1
                      cpuMove(5)
                      if didCpuWin() == True:
                          lose += 1
                          cpuTurn = -1
                          break
                      else:
                          cpuTurn = 0
                          break
                        
                #computer's defense starts here**********************************************************************************************************************************************************************
                        
                  elif (boardValues[2]=='O' and boardValues[5]=='O') and '8' not in chosenAlready:
                      turns += 1
                      cpuMove(8)
                      if didCpuWin() == True:
                          lose += 1
                          cpuTurn = -1
                          break
                      else:
                          cpuTurn = 0
                          break
                        
                  elif (boardValues[1]=='O' and boardValues[4]=='O') and '7' not in chosenAlready:
                      turns += 1
                      cpuMove(7)
                      if didCpuWin() == True:
                          lose += 1
                          cpuTurn = -1
                          break
                      else:
                          cpuTurn = 0
                          break
                      
                  elif (boardValues[3]=='O' and boardValues[2]=='O') and '1' not in chosenAlready:
                      turns += 1
                      cpuMove(1)
                      if didCpuWin() == True:
                          lose += 1
                          cpuTurn = -1
                          break
                      else:
                          cpuTurn = 0
                          break
                      
                  elif (boardValues[4]=='O' and boardValues[7]=='O') and '1' not in chosenAlready:
                      turns += 1
                      cpuMove(1)
                      if didCpuWin() == True:
                          lose += 1
                          cpuTurn = -1
                          break
                      else:
                          cpuTurn = 0
                          break
                      
                  elif (boardValues[2]=='O' and boardValues[8]=='O') and '5' not in chosenAlready:
                      turns += 1
                      cpuMove(5)
                      if didCpuWin() == True:
                          lose += 1
                          cpuTurn = -1
                          break
                      else:
                          cpuTurn = 0
                          break
                      
                  elif (boardValues[1]=='O' and boardValues[7]=='O') and '4' not in chosenAlready:
                      turns += 1
                      cpuMove(4)
                      if didCpuWin() == True:
                          lose += 1
                          cpuTurn = -1
                          break
                      else:
                          cpuTurn = 0
                          break
                      
                  elif (boardValues[2]=='O' and boardValues[5]=='O') and '8' not in chosenAlready:
                      turns += 1
                      cpuMove(8)
                      if didCpuWin() == True:
                          lose += 1
                          cpuTurn = -1
                          break
                      else:
                          cpuTurn = 0
                          break
                      
                  elif (boardValues[5]=='O' and boardValues[8]=='O') and '2' not in chosenAlready:
                      turns += 1
                      cpuMove(2)
                      if didCpuWin() == True:
                          lose += 1
                          cpuTurn = -1
                          break
                      else:
                          cpuTurn = 0
                          break
                      
                  elif (boardValues[2]=='O' and boardValues[8]=='O') and '5' not in chosenAlready:
                      turns += 1
                      cpuMove(5)
                      if didCpuWin() == True:
                          lose += 1
                          cpuTurn = -1
                          break
                      else:
                          cpuTurn = 0
                          break
                      
                  elif (boardValues[3]=='O' and boardValues[6]=='O') and '9' not in chosenAlready:
                      turns += 1
                      cpuMove(9)
                      if didCpuWin() == True:
                          lose += 1
                          cpuTurn = -1
                          break
                      else:
                          cpuTurn = 0
                          break
                      
                  elif (boardValues[6]=='O' and boardValues[9]=='O') and '3' not in chosenAlready:
                      turns += 1
                      cpuMove(3)
                      if didCpuWin() == True:
                          lose += 1
                          cpuTurn = -1
                          break
                      else:
                          cpuTurn = 0
                          break
                      
                  elif (boardValues[3]=='O' and boardValues[9]=='O') and '6' not in chosenAlready:
                      turns += 1
                      cpuMove(6)
                      if didCpuWin() == True:
                          lose += 1
                          cpuTurn = -1
                          break
                      else:
                          cpuTurn = 0
                          break
                      
                  elif (boardValues[1]=='O' and boardValues[2]=='O') and '3' not in chosenAlready:
                      turns += 1
                      cpuMove(3)
                      if didCpuWin() == True:
                          lose += 1
                          cpuTurn = -1
                          break
                      else:
                          cpuTurn = 0
                          break
                      
                  elif (boardValues[2]=='O' and boardValues[3]=='O') and '1' not in chosenAlready:
                      turns += 1
                      cpuMove(1)
                      if didCpuWin() == True:
                          lose += 1
                          cpuTurn = -1
                          break
                      else:
                          cpuTurn = 0
                          break
                      
                  elif (boardValues[1]=='O' and boardValues[3]=='O') and '2' not in chosenAlready:
                      turns += 1
                      cpuMove(2)
                      if didCpuWin() == True:
                          lose += 1
                          cpuTurn = -1
                          break
                      else:
                          cpuTurn = 0
                          break

                  elif (boardValues[4]=='O' and boardValues[5]=='O') and '6' not in chosenAlready:
                      turns += 1
                      cpuMove(6)
                      if didCpuWin() == True:
                          lose += 1
                          cpuTurn = -1
                          break
                      else:
                          cpuTurn = 0
                          break

                  elif (boardValues[5]=='O' and boardValues[6]=='O') and '4' not in chosenAlready:
                      turns += 1
                      cpuMove(4)
                      if didCpuWin() == True:
                          lose += 1
                          cpuTurn = -1
                          break
                      else:
                          cpuTurn = 0
                          break

                  elif (boardValues[4]=='O' and boardValues[6]=='O') and '5' not in chosenAlready:
                      turns += 1
                      cpuMove(5)
                      if didCpuWin() == True:
                          lose += 1
                          cpuTurn = -1
                          break
                      else:
                          cpuTurn = 0
                          break

                  elif (boardValues[7]=='O' and boardValues[8]=='O') and '9' not in chosenAlready:
                      turns += 1
                      cpuMove(9)
                      if didCpuWin() == True:
                          lose += 1
                          cpuTurn = -1
                          break
                      else:
                          cpuTurn = 0
                          break

                  elif (boardValues[8]=='O' and boardValues[9]=='O') and '7' not in chosenAlready:
                      turns += 1
                      cpuMove(7)
                      if didCpuWin() == True:
                          lose += 1
                          cpuTurn = -1
                          break
                      else:
                          cpuTurn = 0
                          break

                  elif (boardValues[7]=='O' and boardValues[9]=='O') and '8' not in chosenAlready:
                      turns += 1
                      cpuMove(8)
                      if didCpuWin() == True:
                          lose += 1
                          cpuTurn = -1
                          break
                      else:
                          cpuTurn = 0
                          break

                  elif (boardValues[1]=='O' and boardValues[5]=='O') and '9' not in chosenAlready:
                      turns += 1
                      cpuMove(9)
                      if didCpuWin() == True:
                          lose += 1
                          cpuTurn = -1
                          break
                      else:
                          cpuTurn = 0
                          break

                  elif (boardValues[5]=='O' and boardValues[9]=='O') and '1' not in chosenAlready:
                      turns += 1
                      cpuMove(1)
                      if didCpuWin() == True:
                          lose += 1
                          cpuTurn = -1
                          break
                      else:
                          cpuTurn = 0
                          break

                  elif (boardValues[1]=='O' and boardValues[9]=='O') and '5' not in chosenAlready:
                      turns += 1
                      cpuMove(5)
                      if didCpuWin() == True:
                          lose += 1
                          cpuTurn = -1
                          break
                      else:
                          cpuTurn = 0
                          break

                  elif (boardValues[3]=='O' and boardValues[5]=='O') and '7' not in chosenAlready:
                      turns += 1
                      cpuMove(7)
                      if didCpuWin() == True:
                          lose += 1
                          cpuTurn = -1
                          break
                      else:
                          cpuTurn = 0
                          break

                  elif (boardValues[5]=='O' and boardValues[7]=='O') and '3' not in chosenAlready:
                      turns += 1
                      cpuMove(3)
                      if didCpuWin() == True:
                          lose += 1
                          cpuTurn = -1
                          break
                      else:
                          cpuTurn = 0
                          break

                  elif (boardValues[3]=='O' and boardValues[7]=='O') and '5' not in chosenAlready:
                      turns += 1
                      cpuMove(5)
                      if didCpuWin() == True:
                          lose += 1
                          cpuTurn = -1
                          break
                      else:
                          cpuTurn = 0
                          break
                  
                  elif cpuInputStr not in chosenAlready:
                      turns += 1
                      cpuMove(cpuInput)
                      if didCpuWin() == True:
                          lose += 1
                          cpuTurn = -1
                          break
                      else:
                          cpuTurn = 0
                          break

                  else:
                      continue
          break
  if turns == 10:
      tie +=1
      print('\n' + 'Round ended in tie.' + '\n')
  print('Player Score: ' + str(win))
  print('Computer Score: ' + str(lose))
  print('Tie: ' + str(tie))
  print("Want to play another round? Enter yes or no.")
  while True:
    try:
      permissionUnknownCase = input()
      permission = permissionUnknownCase.lower()
      if permission == 'no':
         if win > lose:
             print('\n' + 'Player won the game!')
         elif lose > win:
             print('\n' + 'Computer won the game.')
         else:
             print('\n' + 'Game ended in a tie.')
         print('Thanks for playing!')
         break
      elif permission == 'yes':
         cpuTurn = 0
         turns = 0
         chosenAlready = []
         break
      else:
         print("Please enter yes or no.")
    except ValueError:
      print("Invalid input. Please enter yes or no.")
        
         

                

