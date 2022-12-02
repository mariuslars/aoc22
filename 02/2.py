
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


""" 
def findMaxCaloriesList(filename):
    calFile = open(filename)
    totCals = 0
    maxCals = []
    for line in calFile:

        if line == "\n":
            maxCals.append(totCals)
            totCals = 0
            
            continue
        #print(line.strip())
        
        cals = int(line)
        totCals = totCals + cals
        
        
        #if totCals > maxCals:

        
    maxCals.append(totCals)
    maxCals.sort(reverse=True)
    
    return f"maxCal: {maxCals[0]}, top 3 cals: {sum(maxCals[0:3])}"
print(findMaxCaloriesList("data.txt"))



 """