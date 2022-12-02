
def strategyPoints(filename):

    stratFile = open(filename)

    TAP = 0
    UAVGJORT = 3
    SEIER = 6
    gamerulesDict = {"A": {"Z": TAP+3, "X": UAVGJORT+1, "Y": SEIER+2},
                  "B": {"X": TAP+1, "Y": UAVGJORT+2, "Z": SEIER+3},
                  "C": {"Y": TAP+2, "Z": UAVGJORT+3, "X": SEIER+1}}

    gamerulesDict2 = {"A": {"Z": SEIER+2, "X": TAP+3, "Y": UAVGJORT+1},
                "B": {"X": TAP+1, "Y": UAVGJORT+2, "Z": SEIER+3},
                "C": {"Y": UAVGJORT+3, "Z": SEIER+1, "X": TAP+2}}
    totPoints1 = 0
    totPoints2 = 0

    for line in stratFile:

        playerABC, playerXYZ = line.split()
        
        totPoints1 = totPoints1 + gamerulesDict[playerABC][playerXYZ]
        totPoints2 = totPoints2 + gamerulesDict2[playerABC][playerXYZ]
  
            
    return(totPoints1, totPoints2)


print(strategyPoints("data.txt"))
