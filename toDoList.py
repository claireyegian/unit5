#Claire Yegian
#11/20/17
#toDoList.py - keeps track of things to do

commandList = []

while True:
    command  = input('Enter your command and the item you are changing: ')
    
    if command[0:3] == 'add':
        commandList.append(command[4:])
    if command[0] == 'delete':
        commandList.delete(command[7:])
    if command[0] == 'print:
        for item in commandList:
            print(item)
    if commandList[0] == 'quit':
        quit