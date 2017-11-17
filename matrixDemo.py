#Claire Yegian
#11/17/17
#matrixDemo.py - how to create/use a matrix

board = [['a','b','c'],['d','e','f'],['g','h','i']]
printBoard()

def printBoard():
    for row in range(0,3):
        for col in range(0,3):
            print(board[row][col],' ',end = '')
        print()