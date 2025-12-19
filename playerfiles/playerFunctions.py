# A file that defines the functions to manage the player json file
import json

# Adds a player to the Player.json file. The player can not already be in the file
def addPlayerRecord(name, player_class, country, alignment, deity = None): # {
  
    # Checks if player is in the file
    if checkPlayerRecord(name):
        raise LookupError
    
    players_json = readPlayerFile()

    data = {
      "class" : player_class, 
      "country" :country, 
      "alignment" : alignment, 
      "deity" : deity
      }

    players_json[name] = data
    
    writePlayerFile(players_json)
    
    return
# }

# Deletes a users from Players.json file. The player must be in the file
def deletePlayerRecord(name): # {
    
    # Checks if player is in the file
    if (not checkPlayerRecord(name)):
        raise LookupError
    
    players_json = readPlayerFile() 

    players_json.pop(name)
    
    writePlayerFile(players_json)

    return
# }

# Reads the Player.json file and returns dictionary
def readPlayerFile(): # {
    
    try: 
        with open("Players.json", "r") as file: 
            players_json = json.load(file)
    except:
        players_json = {}

    return players_json
# }

# Writes to the Player.json file. Takes a dictionary
def writePlayerFile(dictionary): # {

    with open("Players.json", "w") as file: 
        file_contents = json.dumps(dictionary, indent=4)
        file.write(file_contents)
    
    return
# }

# Checks if a player is in the Player.json file
def checkPlayerRecord(name): # {
    
    players_json = readPlayerFile()
 
    if name in players_json:
        return True
    else:
        return False
# }

# Testing
if __name__ == "__main__":
    pass
