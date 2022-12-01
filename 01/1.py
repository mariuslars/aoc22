

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



