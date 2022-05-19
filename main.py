import random

#an inventory, which is initially empty
inventory = []

#start the player in the Hall
currentRoom = 'Hall'

#a dictionary linking a room to other rooms
rooms = {
            'Hall' : { 
                'south' : 'Kitchen',
                'east'  : 'Dining Room',
                'north' : 'Laboratory',
                'item'  : 'key'
                },        
            'Kitchen' : { 
                'north' : 'Hall',
                'item'  : ''
                },
            'Dining Room' : { 
                'west'  : 'Hall',
                'south' : 'Garden',
                'north' : 'Library',
                'item'  : 'potion'
                },
            'Garden' : { 
                'north' : 'Dining Room',
                'item'  : ''                
                },
            'Library': {
                'south' : 'Dining Room',
                'item': 'Book of Life'
            },
            'Office': {
                'east' : 'Laboratory',
                'item'  : ''
            
            },
            'Laboratory': {
                'south' : 'Hall',
                'west' : 'Office',
                'item': 'Beam-O-Mat'
            }
         }
def showInstructions():
  #print a main menu and the commands
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
  #print the player's current status
  print('---------------------------')
  print('You are in the ' + currentRoom)
  #print the current inventory
  print('Inventory : ' + str(inventory))
  #print an item if there is one
  if "item" in rooms[currentRoom]:
    if len(rooms[currentRoom]['item']) > 0:
        print('You see a ' + rooms[currentRoom]['item'])
  print("---------------------------")
  
def spawnMonster():
    rooms[random.choice(list(rooms.keys()))]['item'] = 'monster'
    
#main-program
showInstructions()
showStatus()
spawnMonster()
move = ''
while move == '':
    move = input('>')
    move = move.lower().split()
    if move[0] == "exit":
        print(move)
        break
    if move[0] == "go":
        if move[1] in rooms[currentRoom]:
            currentRoom = rooms[currentRoom][move[1]]
            showStatus()
        else:
            print('You can\'t go that way!')
    if move[0] == 'get' :
        if 'item' in rooms[currentRoom] and move[1] in rooms[currentRoom]['item'].lower():
            inventory += [move[1]]
            print(move[1] + ' got!')
            del rooms[currentRoom]['item']
        else:
            print('Can\'t get ' + move[1] + '!')
    if 'item' in rooms[currentRoom] and 'monster' in rooms[currentRoom]['item']:
        print('A monster has got you... GAME OVER!')
        break    
    if currentRoom == 'Garden' and 'key' in inventory and 'potion' in inventory:
        print('You escaped the house... YOU WIN!')
        break
    if currentRoom == 'Laboratory' and 'book of life' in inventory and 'beam-o-mat' in inventory:
        print('You escaped the house... YOU WIN!')
        break
    move = ''
