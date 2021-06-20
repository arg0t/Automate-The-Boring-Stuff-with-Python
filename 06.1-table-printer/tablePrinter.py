def tablePrinter(tableData):
    colWidths = [0] * len(tableData)

    # Find the longest string in each of the inner lists
    for i in range(len(tableData)):
        maxWidth = 0
        for y in tableData[i]:
            if len(y) > maxWidth:
                maxWidth = len(y)

        colWidths[i] = maxWidth

    # Print the table
    for i in range(len(tableData[0])):
        for j in range(len(tableData)):
            print(tableData[j][i].rjust(colWidths[j]), end=' ')
        print()


tableData = [['apples', 'oranges', 'cherries', 'banana'],
            ['Alice', 'Bob', 'Carol', 'David'],
            ['dogs', 'cats', 'moose', 'goose']]

tablePrinter(tableData)
