# dnd-util

Collection of useful DnD scripts!

## roller.py

This is an automatic initiative roller.

### Add
To add a player:
~~~~
add [NAME] [DEX] [OTHER] {TEMP('true'|'false')}
~~~~
OTHER is for some other non-dex bonus someone might get to initiative.
TEMP (which is true by default, this argument is optional) is a flag for each player. If you're quickly adding a set of enemies you want to easily be able to remove without messing with your base set of players, leave this set to true. (For a base player you aren't likely to delete, pass "false" to this)

Example:
~~~~
Roller> add Dude 2 0 false
Adding {'other': 0, 'total': -1, 'temp': False, 'dex': 2, 'roll': -1, 'name': 'Dude'}...
Saving...
Saved!
~~~~

This added a player named "Dude" (Who is a base player, aka doesn't need to be deleted soon, so temp is set to false) with a dex of 2 and no special bonus.



### Usage Example


~~~~
Roller> add dude 2 0 false
Adding {'name': 'dude', 'temp': False, 'other': 0, 'dex': 2, 'roll': -1, 'total': -1}...
Saving...
Saved!

Roller> add dudet 1 0 false
Adding {'name': 'dudet', 'temp': False, 'other': 0, 'dex': 1, 'roll': -1, 'total': -1}...
Saving...
Saved!

Roller> add enemy1 0 0
Adding {'name': 'enemy1', 'temp': True, 'other': 0, 'dex': 0, 'roll': -1, 'total': -1}...
Saving...
Saved!

Roller> add enemy2 0 0
Adding {'name': 'enemy2', 'temp': True, 'other': 0, 'dex': 0, 'roll': -1, 'total': -1}...
Saving...
Saved!

Roller> players
dude
dudet
enemy1 (TEMP)
enemy2 (TEMP)

Roller> roll
Rolling...
dude rolled a 15...
dudet rolled a 20...
enemy1 rolled a 5...
enemy2 rolled a 4...
Sorting...
Sorted!

        1. dudet - roll: 20 - total: 121
        2. dude - roll: 15 - total: 17
        3. enemy1 - roll: 5 - total: 5
        4. enemy2 - roll: 4 - total: 4

Saving...
Saved!

Roller> clear
Removing temporary players...
Removed!
Saving...
Saved!

Roller> players
dudet
dude

Roller> remove dude
Removing player dude...
Removed!
Saving...
Saved!

Roller> players
dudet
~~~~
NOTE: crits add 100 to total for sorting purposes
