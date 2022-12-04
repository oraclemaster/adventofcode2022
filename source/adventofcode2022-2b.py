import os

#os.chdir('X:\\Sorgenti\\Python\\adventofcode\\2022')
print ('Directory: ' + os.getcwd())

partite = open("input2.txt").read().strip().split("\n") # prod

# A = Rock, B = Paper, C = Scissor first player, X = I must loose, Y = I must draw, Z = I must win 
# score X = 1 rock, Y = 2 paper, Z = 3 scissor + 0 if lost, 3 draw e 6 if won
# 0 "" nothing = 0
# 1 BX I must loose so I choose X rock 1 + 0 I lost =  1     
# 2 CX I must loose so I choose so I choose Y paper 2 + 0 I lost = 2
# 3 AX I must loose so I choose Z scissor 2 + 0 I lost = 3       
# 4 AY I must draw so I choose X rock 1 + 3 I draw = 4     
# 5 BY I must draw so I choose Y paper 2 + 3 I draw = 5                                                  
# 6 CY I must draw so I choose Z scissor 3 + 3 I draw = 6
# 7 CZ I must win so I choose X rock 1 + 6 I win = 7
# 8 AZ I must win so I choose Y paper 2 + 6 I win = 8
# 9 BZ I must win so I choose 3 scissor 3 + 6 I win = 9
print("Final ", sum(map(["", "B X","C X","A X", "A Y", "B Y", "C Y", "C Z", "A Z", "B Z"].index,partite)))
