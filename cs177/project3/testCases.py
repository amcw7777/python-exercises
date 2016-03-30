##########################################################
#                     Required Imports                   #
##########################################################
from project3 import buildRankTable
from project3 import readGroupInfo
from project3 import readResultsRound0
from project3 import buildPointsTable
from project3 import addRankToPointsTable
from project3 import breakTies
from project3 import buildCrossedTable
from project3 import determineWinner
from project3 import plotGoalsBarChar
from sorter import sortTable


##########################################################
#           Test cases for Task 1 - Task 9               #
##########################################################

# This is a unit test for readGroupInfo function.
def testTask1():
    teams = readGroupInfo('groupA')
    for t in teams:
        print (t)

# This is a unit test for readResultsRound0 function.
def testTask2():
    teams = ['Colombia', 'Japan', 'Mexico', 'France']
    results = readResultsRound0(teams)
    for r in results:
        print (r)

# This is a unit test for buildPointsTable function.
def testTask3():
    teams = ['Colombia', 'Japan', 'Mexico', 'France']
    results = ['Mexico, France, 4, 6',   \
               'Japan, Mexico, 8, 2',    \
               'Colombia, Mexico, 3, 9', \
               'Colombia, Japan, 9, 7',  \
               'Colombia, France, 2, 8', \
               'Japan, France, 4, 4']
    pointsTable = buildPointsTable(teams, results)
    for p in pointsTable:
        print (p)

# This is a unit test for breakTies function.
def testTask4():
    # rankTable = [['France', 7, 1],   \
    #              ['Japan', 4, 2],    \
    #              ['Colombia', 3, 3], \
    #              ['Mexico', 3, 4]]
    rankTable = [['Bangladesh', 6, 1], \
            ['Brazil', 6, 1], \
            ['Panama', 6, 1], \
            ['Argentina', 0, 4]]

    rankTable = breakTies(rankTable)
    for r in rankTable:
        print (r)

# This is a unit test for addRankToPointsTable function. Note that this function
# calls breakTies function if there is a tie in the ranks of more than one teams.
# Hence, you should complete and test task 6 (break the Ties) before testing
# testTask4().
def testTask5():
    pointsTable = [['Colombia', 3], \
                   ['Japan', 4],    \
                   ['Mexico', 3],   \
                   ['France', 7]]
    rankTable = addRankToPointsTable(pointsTable)
    for r in rankTable:
        print (r)

# This is a unit test for buildRankTable function. Note that you are required
# to complete tasks 1, 2, 3, 4, and 5 first in order to complete the task 6.
# Hence, after completing the tasks 1, 2, 3, 4, and 5 you should run testTask6().
def testTask6():
    group = 'groupA'
    rankTable = buildRankTable(group)
    for r in rankTable:
        print(r)

# This is a unit test for buildCrossTable function.
def testTask7():
    rankTableA = [['Japan', 6, 1], ['Colombia', 4, 2],\
                  ['Mexico', 4, 3], ['France', 3, 4]]


    rankTableB = [['USA', 9, 1], ['Saudi Arabia', 4, 2], \
                  ['India', 3, 3], ['Argentina', 1, 4]]

    crossedTableAB = buildCrossedTable(rankTableA, rankTableB)

    print(crossedTableAB)

# This is a unit test for determine function.
def testTask8():
    teams = ['Panama', 'India']
    winner = determineWinner(teams)
    print(winner)

# This is a unit test for plotGlobalsBarChar function.
def testTask9():
    finalResults = ['Brazil', 'Germany', 'Italy']
    plotGoalsBarChar(finalResults)


##########################################################
#        Test cases for Sort Table (Optional)            #
##########################################################

def test1SortTable():
    rankTable = [['Brazil', 6, 1], \
                   ['Bangladesh', 6, 1], \
                   ['Panama', 6, 1], \
                   ['Argentina', 0, 4]]
    rankTable = sortTable(rankTable, 0, 0, 2, 'ascending')
    for r in rankTable:
        print (r)

def test2SortTable():
    pointsTable = [['Bangladesh', 1], \
                   ['Brazil', 4], \
                   ['Panama', 6], \
                   ['Argentina', 4]]
    pointsTable = sortTable(pointsTable, 1, 0, len(pointsTable)-1, 'descending')
    for p in pointsTable:
        print (p)


##########################################################
#  The main function contains the call to all the tests  #
#  Uncomment the desired test one at a time              #
##########################################################
def main():

    # Test for tasks
    # testTask1()
    # testTask2()
    # testTask3()
    # testTask4()
    # testTask5()
    # testTask6()
    # testTask7()
    testTask8()
    #testTask9()

    # Test for sort table
    #test1SortTable()
    #test2SortTable()

if __name__ == '__main__':
    main()
