from operator import index, indexOf


medalResults = [
    {
        "sport": "cycling",
        "podium": ["1.China", "2.Germany", "3.ROC"]
    },
    {
        "sport": "fencing",
        "podium": ["1.ROC", "2.France", "3.Italy"]
    },
    {
        "sport": "high jump",
        "podium": ["1.Italy", "1.Qatar", "3.Belarus"]
    },
    {
        "sport": "swimming",
        "podium": ["1.USA", "2.France", "3.Brazil"]
    }
]
    
def createMedalTable(medalResults):
    # Use the results object above to create a medal table
    # The winner gets 3 points, second place 2 points and third place 1 point
    exp = {}
    # loop through result
    for i in medalResults:
        #get the list by using podium key
        for j in (i['podium']):
            #split it into two part, number and name
            k = j[0]
            j = j[2:]
            #if number is 1
            if k == "1":
                #and key in already in dictionary the add 3 to range
                if j in exp.keys():
                    exp[j] += 3
                #otherwise assign 3, making name as key
                else:
                    exp[j] = 3
            # same as above but just assign 2 in range is 2
            if k == "2":
                if j in exp.keys():
                    exp[j] += 2
                else:
                    exp[j] = 2
            # same as above but just assign 1 in range is 3
            if k == "3":
                if j in exp.keys():
                    exp[j] += 1
                else:
                    exp[j] = 1
    #sort distionary by range
    dic = {}
    for w in sorted(exp, key=exp.get, reverse=True):
        dic[w] = exp[w]
    # return dic
    return exp


def test_function():
    #This it the test function, please don't change me
    medalTable = createMedalTable(medalResults)
    expectedTable = {
        "Italy": 4,
        "France": 4,
        "ROC": 4,
        "USA": 3,
        "Qatar": 3,
        "China": 3,
        "Germany": 2,
        "Brazil": 1,
        "Belarus": 1,
    }
    print('Actual Values',medalTable)
    print('Expected Values', expectedTable)
    assert medalTable == expectedTable

test_function()
