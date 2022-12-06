partite = open("input2.txt").read().strip().split("\n")

# A = Rock, B = Paper, C = Scissor first player, X = Rock, Y = Paper, Z = Scissor second player
# score X = 1, Y = 2, Z = 3  + X = 0 loose, Y = 3 draw e Z = 6 if won
# 0 "" nothing = 0
# 1 BX = 1 for rock 0 lost                                                                        
# 2 CY = 2 for paper 0 lost
# 3 AZ = 3 for scissor 0 lost
# 4 AX = 1 for rock + 3 for draw
# 5 BY = 2 for paper + 3 for draw
# 6 CZ = 3 for scissor + 3 for draw
# 7 CX = 1 for rock + 6 for win
# 8 AY = 2 for paper + 6 for win
# 9 BZ = 3 for scissor + 6 for win
print("Final ",sum(map(["", "B X","C Y","A Z", "A X", "B Y", "C Z", "C X", "A Y", "B Z"].index,partite)))
