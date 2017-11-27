#Claire Yegian
#11/20/17
#toDoList.py - keeps track of things to do

commandList = []

while True:
    command  = input('Enter your command and the item you are changing: ')
    
    if command[0:3] == 'add':
        commandList.append(command[4:])
    if command[0:6] == 'delete':
        commandList.remove(command[7:])
    if command[0:5] == 'print':
        for item in commandList:
            print(item)
    if command[0:4] == 'quit':
        break
