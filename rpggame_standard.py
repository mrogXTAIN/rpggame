import random

inventory = []
currentRoom = "Hall"
rooms = {
            'Hall':{
                'south' : 'Kitchen',
                'east'  : 'Dining Room',
                'north' : 'Office',
                'west'  : 'Labor',
                'item'  : 'key'
                },        
            'Kitchen':{
                'north' : 'Hall'   
                },
            'Dining Room': {
                'west'  : 'Hall',
                'south' : 'Garden',
                'item'  : 'potion'
                },
            'Garden':{
                'north' : 'Dining Room' 
                },
            'Office':{
                'south' : 'Hall',
                'west'  : 'Library'
                },
            'Library':{
                'east'  : 'Office',
                'item'  : 'bookoflife'
                },
            'Labor':{
                'east'  : 'Hall',
                'item'  : 'BeamOMat'
                }
         }

def randomSpawnMonster():
    room_list = ['Hall', 'Kitchen', 'Dining Room', 'Garden', 'Office', 'Library', 'Labor']
    x = random.choice(room_list)
    rooms[x]['item'] = 'Monster'


def showInstructionWindow():
    print('''
            Welcome to your own RPG Game
            ============================
            Get to the Garden with a key and a potion.
            Avoid the monsters!

            Commands:
            go [direction]
            get [item]
''')

def showStatus():
    print("---------------------------")
    print(f"You are in the {currentRoom}")
    print("Inventory: "+ str(inventory))
    if "item" in rooms[currentRoom]:
        print(f"There is a {rooms[currentRoom]['item']}")
    print("---------------------------")


showInstructionWindow()
randomSpawnMonster()
while True:
    showStatus()
    move = ""
    while move == "":
        move = input('>')
    move = move.lower().split()
    if move[0] == "exit":
        break
    if move[0] == "go":
        if move[1] in rooms[currentRoom]:
            currentRoom = rooms[currentRoom][move[1]]
        else:
            print("You cant go that way!")
    
    if move[0] == "get":
        if 'item' in rooms[currentRoom] and move[1] in rooms[currentRoom]['item']:
            inventory += [move[1]]
            print(move[1] + " got!")
            del rooms[currentRoom]['item']
        else:
            print(f"Cant get {move[1]}!")
    if 'item' in rooms[currentRoom] and rooms[currentRoom]['item'] == 'Monster':
        print("You died... A monster killed you, all items in your Inventory are lost")
        break
    if currentRoom == "Garden" and "key" in inventory and "potion" in inventory:
        print("Congratulations! YOU WON!!!! ")
        break
    if currentRoom == 'Labor' and "BookOfLife" in inventory and "Beam-O-Mat" in inventory:
        print("Congratulations! YOU WON!!!")
        break
    if move[0] == "exit":
        break
