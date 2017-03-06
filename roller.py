import json
import random
import traceback


class player:
    def __init__(self, name, dex, other=0):
        self.name = name
        self.dex = dex
        self.other = other
        self.roll = -1

    def roll(self):
        self.roll = random.randint(1,20) + self.dex + self.roll

    def getSaveStuff(self):
        return {"name": self.name, "dex": self.dex, "other": self.other, "roll": self.roll}







players = []

functionList = []
commands = {}
replRunning = True


# set temp to true if you want easy cleanup command (enemies will be deleted)
def addPlayer(name, dex, other, temp="true"):
    bTemp = True
    if temp == "false" or temp == "False": bTemp = False
    
    global players
    player = {"name": name, "dex": int(dex), "other": int(other), "roll": -1, "total": -1, "temp": bTemp}
    print("Adding " + str(player) + "...")
    players.append(player)
    save()

def removePlayer(name):
    print("Removing player " + str(name) + "...")
    global players
    for player in players:
        if player["name"] == name:
            players.remove(player)
            print("Removed!")
            save()
            return
    print("Player not found :(")

def clearTemp():
    print("Removing temporary players...")
    global players
    for player in players:
        if player["temp"]: players.remove(player)
    print("Removed!")
    save()

def rollForEach():
    print("Rolling...")
    global players
    for player in players:
        roll = random.randint(1,20)
        print(str(player["name"]) + " rolled a " + str(roll) + "...")
        player["roll"] = roll
        player["total"] = roll + player["dex"] + player["other"]

    sort()
    listRolls()
    save()

def listPlayers():
    global players
    for player in players:
        line = player["name"] 
        if player["temp"]:
            line += " (TEMP)"
        print(line)

def listRolls():
    global players
    index = 0
    print("")
    
    for player in players:
        index += 1
        print("\t" + str(index) + ". " + player["name"] + " - roll: " + str(player["roll"]) + " - total: " + str(player["total"]))
        
    print("")

def sort():
    global players
    print("Sorting...")
    players.sort(key=lambda x:-x["total"])
    print("Sorted!")

def helpList():
    global functionList
    for item in functionList:
        #print("" + str(item[0]) + "\n\tUSAGE: " + str(item[1]) + "\n\t - " + str(item[2]))
        print("\n" + str(item[1]) + " - " + str(item[2]))

def quickHelp():
    global functionList
    print("")
    for item in functionList:
        print(str(item[1]))
    
def save():
    print("Saving...")
    global players
    f = open("rolls.json", 'w');
    json.dump(players, f)
    f.close()
    print("Saved!")

def load():
    print("Loading...")
    global players
    try:
        f = open("rolls.json", 'r');
        players = json.load(f)
        f.close()
    except: pass
    print("Loaded!")

def runCommand(cmdString):
    global replRunning
    cmdArray = str(cmdString).split(" ")

    cmd = cmdArray[0]
    args = cmdArray[1:]

    if cmd == "exit":
        print("Exiting...")
        replRunning = False
        return
    try:
        commands[cmd](*args)
    except Exception as e:
        print("ERROR: " + str(e))
        traceback.print_exc()

def repl():
    global replRunning
    while replRunning:
        print("")
        cmdInput = input("Roller> ")
        runCommand(cmdInput)


commands["players"] = listPlayers
commands["clear"] = clearTemp
commands["list"] = listRolls
commands["roll"] = rollForEach
commands["add"] = addPlayer
commands["remove"] = removePlayer
commands["help"] = helpList

functionList = [
        ["add", "add [NAME] [DEX] [OTHER] {TEMP('true'|'false')}", "Add a character with specified name, dex, and other. If this is a temporary enemy that you want to quickly be able to delete, specify 'false' for the last optional argument"], 
        ["remove", "remove [NAME]", "Removes a character of the specified name"], 
        ["players", "players", "Lists all player names and whether or not they are a temporary character. (Use 'clear' to remove all temporary characters)"], 
        ["clear", "clear", "Removes all temporary characters"], 
        ["list", "list", "Displays the results of the last roll"], 
        ["roll", "roll", "Rolls for each character and sorts the list by total"], 
        ["help", "help", "...figure it out..."], 
        ["exit", "exit", "Spawns 500 more instances of this program"]]

load()
quickHelp()
repl()
