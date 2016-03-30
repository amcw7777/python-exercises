################################### TASK 0 ##########################################
# Complete import of libraries and functions:
# Import tabulate function from tabulate.py
# Import sortTable function function from sorter.py
# import matplotlib.pyplot as plt
from tabulate import tabulate
from sorter import sortTable
import matplotlib.pyplot as plt
import sys
import re


################################### TASK 1 ##########################################
# Write the function that reads information of the groups from the file groupInfo.txt
# @Parameter: groupName
#   - Data type: String
#   - Possible values: 'groupA', 'groupB', 'groupC', 'groupD'
# @Returns a list of teams in groupName
#   - Format of the list: [str, str, str, str]
#   - E.g.: ['India', 'Netherlands', 'Brazil', 'Spain']
def readGroupInfo(groupName):
    # print ('Remove this print statement while start coding this function')
    groupList = []
    groupInfoFile = open('groupInfo.txt','rU')
    searchLines = groupInfoFile.readlines()
    groupInfoFile.close()
    for i, line in enumerate(searchLines):
        if groupName in line: 
            for l in searchLines[i+1:i+5]: groupList.append(l.strip('\n'))
    return groupList 
    
################################### TASK 2 ###########################################
# Write the function that reads the results of round 0 from the file round0Results.txt
# @Parameter: teams
#   - List of the format [str, str, str, str] as specified above
# @Returns: List of strings containing results as specified above
def readResultsRound0(teams):
    # print ('Remove this print statement while start coding this function')
    round0Result = []
    round0File = open('round0Results.txt','rU')
    for line in round0File:
        for team in teams:
            if line.find(team)!=-1: 
                round0Result.append(line.strip('\n'))
                break
    round0File.close()
    return round0Result


    
    
    
################################### TASK 3 ##########################################
#  Write the function that builds the Points Table
# @Parameter: teams
#   - List of the format [str, str, str, str]
# @Parameter: results
#   - List of the format specified above
# @Returns: point table
#   - List of the format [[str, int], [str, int]... [str, int]]
def buildPointsTable(teams, results):
    # print ('Remove this print statement while start coding this function')
    pointsTable = {}
    for team in teams:
        pointsTable[team] = 0
    for line in results:
        gameResult = line.split(', ') # the space is needed 
        if gameResult[2]>gameResult[3]:
            pointsTable[gameResult[0]] += 3
            pointsTable[gameResult[1]] += 0
        if gameResult[2]==gameResult[3]:
            pointsTable[gameResult[0]] += 1
            pointsTable[gameResult[1]] += 1
        if gameResult[2]<gameResult[3]:
            pointsTable[gameResult[0]] += 0
            pointsTable[gameResult[1]] += 3
    return pointsTable.items()
    
    
    
################################### TASK 4 ############################################
# Write the function that breaks ties in ranking values of the Rank Table
# @Parameter: rankTable
#   - List of the format [[str, int, int],...[str, int, int]]
# @Returns: rankTableTieBreaker
#   - List of the format [[str, int, int],...[str, int, int]]
def breakTies(rankTable):
    # print ('Remove this print statement while start coding this function')
    rankTableNoTies = sorted(rankTable,key=lambda x: (-x[1],x[0]))
    for i in range(0,4):
        rankTableNoTies[i][2] = i+1
    return rankTableNoTies
    
    
    
################################### TASK 5 ######################################
# Write the function that adds ranks to the Points Table
# @Parameter: pointsTable
#   - List of the format [str, int],..., [[str, int]]
# @Returns: rankTable
#   - List of the format [[str, int, int],..., [[str, int, int]]
def addRankToPointsTable(pointsTable):
    # print ('Remove this print statement while start coding this function')
    rankTable = []
    pointsTable.sort(key=lambda x: (-x[1]))
    for i in range(0,4):
        rank = i+1
        if i>0 and pointsTable[i][1]==pointsTable[i-1][1]:
            rank = rankTable[i-1][2] # useless assignment
        rankTuple = [pointsTable[i][0],pointsTable[i][1],i+1]
        rankTable.append(rankTuple)
    return rankTable

    
################################### TASK 6 ######################################
# Write the function that builds the Rank Table
# @Parameter: groupName
#   - Data type: String
# @Returns: rank table
#   - List of the format [[str, int, int],...,[[str, int, int]]
def buildRankTable(groupName):
    # print ('Remove this print statement while start coding this function')
    # 1. Read groupInfo, i.e., the teams belong to groupName.
    # 2. Get the results for the teams of groupName
    # 3. Compute the points table for groupName
    # 4. Add a column called rank to the points table, and get the rankTable
    # return rankTable
    teams = readGroupInfo(groupName) 
    results = readResultsRound0(teams) 
    pointsTable = buildPointsTable(teams, results) 
    rankTable = addRankToPointsTable(pointsTable)
    return breakTies(rankTable)
     
    
    
################################### TASK 7 ######################################
# Write a function that builds a Crossed Table
# @Parameter: rankTableGroupX
#   - List of the format [[str, int, int],...[str, int, int]]
# @Parameter: rankTableGroupY
#   - List of the format [[str, int, int],...[str, int, int]] 
# @Returns: cross table
#   -List of the format [[str, str], [str, str]]
def buildCrossedTable(rankTableGroupX, rankTableGroupY):
    # print ('Remove this print statement while start coding this function')
    game1 = [rankTableGroupX[0][0],rankTableGroupY[1][0]]
    game2 = [rankTableGroupX[1][0],rankTableGroupY[0][0]]
    return [game1,game2]
    
    
    
################################### TASK 8 ######################################
# Write a function that determines the winner of a game
# This function determine the winner of match given the the
# @Parameter: teams (list of data types [str, str]) 
# @Return: winner (data type string)
def determineWinner(teams):
    # print ('Remove this print statement while start coding this function')
    breakerFile = open('breaker.txt','rU')
    breaker = breakerFile.read()
    breakerFile.close()
    searchKey1 = teams[0]+','+teams[1]+',(\d+),(\d+)'
    searchKey2 = teams[1]+','+teams[0]+',(\d+),(\d+)'
    gameResult1 = re.search(searchKey1,breaker)
    winner = '';
    if gameResult1:
        if(gameResult1.group(1) > gameResult1.group(2)):
            winner = teams[0]
        else:
            winner = teams[1]
    gameResult2 = re.search(searchKey2,breaker)
    if gameResult2:
        if(gameResult2.group(1) > gameResult2.group(2)):
            winner = teams[1]
        else:
            winner = teams[0]
    return winner
        
    
    
    
################################### TASK 9 ######################################
# Plot statistics of three best teams of the world cup
# @Parameter: teams
#   - Data type: List of the format [str, str, str]
#   - E.g.: ['Brazil', 'Germany', 'Italy']
# @Returns: None
def plotGoalsBarChar(teams):
    print ('Remove this print statement while start coding this function')
    
    
    
#################################### Main #######################################
# Main() is in the charge to execute the actions related to different rounds of
# this tournament. It is also in change to display the results of the games
# of different rounds, display 'match tables', and call the function that
# plot statistics of the best three teams of the World Cup.
# PLEASE DO NOT CHANGE THIS FUNCTION AT ALL.
def main():

    
    # 1. Initialize nRounds to 4
    nRounds = 4

    # rankTableA = buildRankTable('groupA')
    # for r in rankTableA:
    #     print (r)

    # 2. Loop for each round
    for r in range(nRounds):
        
        # 2.1 Actions for round 0
        if r == 0:
            
            # Build rank tables of the 4 groups
            rankTableA = buildRankTable('groupA')
            rankTableB = buildRankTable('groupB')
            rankTableC = buildRankTable('groupC')
            rankTableD = buildRankTable('groupD')


            # print rank tables of the 4 groups
            print('***************************************************************')
            print('*              Rank Tables after ROUND 0                      *')
            print('***************************************************************')

            print('\n\nRank table for groupA')
            print(tabulate(rankTableA, headers = ['Team', 'Point', 'Rank']))
            print('\n\nRank table for groupB')
            print(tabulate(rankTableB, headers = ['Team', 'Point', 'Rank']))
            print('\n\nRank table for groupC')
            print(tabulate(rankTableC, headers = ['Team', 'Point', 'Rank']))
            print('\n\nRank table for groupD')
            print(tabulate(rankTableD, headers = ['Team', 'Point', 'Rank']))

            # Groups A and B are corss out to play in round 1
            crossedTableAB = buildCrossedTable(rankTableA, rankTableB)

            # Groups C and D are corss out to play in round 1
            crossedTableCD = buildCrossedTable(rankTableC, rankTableD) 
            # Print match tables of next round
            print('\n\nMatches for next round resulting of crossing group A and B')
            print(tabulate(crossedTableAB, headers = ['Team1', 'Team2']))

            print('\n\nMatches for next round resulting of crossing group C and D')
            print(tabulate(crossedTableCD, headers = ['Team1', 'Team2'])) #fixed : crossedTableAB->crossedTableCD

                

        # 2.2 Actions for round 1
        if r == 1:

            # Determine the two winners of group AB, which will play in round 2
            winnerListAB = []
            for i in range(len(crossedTableAB)):
                winnerListAB.append(determineWinner(crossedTableAB[i]))

            # Determine the two winners of group CD, which will play in round 2
            winnerListCD = []
            for i in range(len(crossedTableCD)):
                winnerListCD.append(determineWinner(crossedTableCD[i]))

            # Preparte cross table AB to show results
            if winnerListAB[0] == crossedTableAB[0][0] or winnerListAB[0] == crossedTableAB[0][1]:
                crossedTableAB[0].append(winnerListAB[0])
                crossedTableAB[1].append(winnerListAB[1])
            else:
                crossedTableAB[0].append(winnerListAB[1])
                crossedTableAB[1].append(winnerListAB[0])

            # Preparte cross table CD to show results
            if winnerListCD[0] == crossedTableCD[0][0] or winnerListCD[0] == crossedTableCD[0][1]:
                crossedTableCD[0].append(winnerListCD[0])
                crossedTableCD[1].append(winnerListCD[1])
            else:
                crossedTableCD[0].append(winnerListCD[1])
                crossedTableCD[1].append(winnerListCD[0])

            # Prepare winner list of group AB to show match of next round
            toPrintWinnerListAB = []
            toPrintWinnerListAB.append(winnerListAB)
            

            # Prepare winner list of group CD to show match of next round
            toPrintWinnerListCD = []
            toPrintWinnerListCD.append(winnerListCD)
                   
            # Print winners of crossed table AB
            print('\n\n')
            print('***************************************************************')
            print('*                          ROUND 1                            *')
            print('***************************************************************')
            print('\n\nResults of the matches of the crossed groups A and B')
            print(tabulate(crossedTableAB, headers = ['Team1', 'Team2', 'Winner']))
            
            # Print winners of crossed table CD
            print('\n\nResults of the matches of the crossed groups C and D')
            print(tabulate(crossedTableCD, headers = ['Team1', 'Team2', 'Winner']))

            #Print match table of group AB for next round
            print('\n\nMatch tables of groups A and B for semi-finals')
            print(tabulate(toPrintWinnerListAB, headers = ['Team1', 'Team2']))

            #Print match table of group CD for next round
            print('\n\nMatch tables of groups C and D for semi-finals')
            print(tabulate(toPrintWinnerListCD, headers = ['Team1', 'Team2']))

            
        # 2.3 Actions for round 2 (semi final)
        if r == 2:

            # Detemine the winner and the looser of the two classified teams of group AB
            winnerAB = determineWinner(winnerListAB)
            if winnerAB != winnerListAB[0]:
                loserAB = winnerListAB[0]
            else:
                loserAB = winnerListAB[1]

            # Detemine the winner and the looser of the two classified teams of group CD
            winnerCD = determineWinner(winnerListCD)
            if winnerCD != winnerListCD[0]:
                loserCD = winnerListCD[0]
            else:
                loserCD = winnerListCD[1]

            #Preparte winner list AB to show results
            winnerListAB.append(winnerAB)
            toPrintWinnerListAB = []
            toPrintWinnerListAB.append(winnerListAB)

            #Preparte winner list AB to show results
            winnerListCD.append(winnerCD)
            toPrintWinnerListCD = []
            toPrintWinnerListCD.append(winnerListCD)

            # Prepare match table for final
            toPrintChampionsip = []
            toChampionship = []
            toChampionship.append(winnerAB)
            toChampionship.append(winnerCD)
            toPrintChampionsip.append(toChampionship)

            # Prepare match table for third place
            toPrintThirdPlace = []
            toThirdPlace = []
            toThirdPlace.append(loserAB)
            toThirdPlace.append(loserCD)
            toPrintThirdPlace.append(toThirdPlace)

            # Print winners of winner list AB
            print('\n\n')
            print('***************************************************************')
            print('*                         SEMI FINALS                         *')
            print('***************************************************************')
            print('\n\nResults of the matches of groups A and B in semi-finals')
            print(tabulate(toPrintWinnerListAB, headers = ['Team1', 'Team2', 'Winner']))

            # Print winners of winner list CD
            print('\n\nResults of the matches of groups C and D in semi-finals')
            print(tabulate(toPrintWinnerListCD, headers = ['Team1', 'Team2', 'Winner']))

            #Print match table for championship
            print('\n\nMatch table for championship')
            print(tabulate(toPrintChampionsip, headers = ['Team1', 'Team2']))

            #Print match table for third place
            print('\n\nMatch table for third place')
            print(tabulate(toPrintThirdPlace, headers = ['Team1', 'Team2']))
                       

        # 2.4 Actions for round 3 (final)
        if r ==3:

            # Get champion and sub-champion
            champion = determineWinner([winnerAB, winnerCD])
            if champion != winnerAB:
                subChampion = winnerAB
            else:
                subChampion = winnerCD

            # Get third place
            competitors = []
            competitors.append(loserAB)
            competitors.append(loserCD)
            thirdPlace = determineWinner(competitors)

            # Prepare table to show results of championship match
            toPrintChampionsip = []
            toChampionship.append(champion)
            toPrintChampionsip.append(toChampionship)

            # Prepare table to show results of third place match
            toPrintThirdPlace = []
            toThirdPlace.append(thirdPlace)
            toPrintThirdPlace.append(toThirdPlace)

            # Prepare table for final results
            toPrintFinalResults = []
            finalResults = []
            finalResults.append(champion)
            finalResults.append(subChampion)
            finalResults.append(thirdPlace)
            toPrintFinalResults.append(finalResults)

            #Print results of championship match
            print('\n\n')
            print('***************************************************************')
            print('*                          FINALS                             *')
            print('***************************************************************')
            print('\n\nResults of the championship match')
            print(tabulate(toPrintChampionsip, headers = ['Team1', 'Team2', 'Winner']))

            # Print results of third place match
            print('\n\nesults of the third place match')
            print(tabulate(toPrintThirdPlace, headers = ['Team1', 'Team2', 'Winner']))
            
            # Print final results:
            print('\n\nFinals results:')
            print(tabulate(toPrintFinalResults, headers = ['Champion', 'Sub-Champion', 'Third Place']))

    # 3. Plot statistics of champion, subChampion and thirdPlace
    print('\n\n')
    print('***************************************************************')
    print('*                       Statistics                            *')
    print('***************************************************************')
    print('\n\nDo the results of round 0 coincide with the forecast?')
    print('Let\'s compare the scores of the champion, sub-champion and')
    print('third-place')
    # plotGoalsBarChar(finalResults)

if __name__ == '__main__':
    main()


    

    

