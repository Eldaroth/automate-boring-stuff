def printTable(listOfItems):
    # generate list with values for each of the inner list
    colWidths = [0] * len(listOfItems)

    # find out the maximal width for each column
    for i in range(len(listOfItems)):
        for j in range(len(listOfItems[i])):
            if colWidths[i] < len(listOfItems[i][j]):
                colWidths[i] = len(listOfItems[i][j])

    # iterate over each of the items in the list
    for k in range(len(listOfItems[0])):
        for l in range(len(listOfItems)):
            print(listOfItems[l][k].rjust(colWidths[l]) + " |", end=" ")
        print()


tableData = [
    ["apples", "oranges", "cherries", "banana"],
    ["Alice", "Bob", "Carol", "David"],
    ["dogs", "cats", "moose", "goose"],
]

printTable(tableData)
