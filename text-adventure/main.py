#!/usr/bin/env python3
import sys, os, json
# Check to make sure we are running the correct version of Python
assert sys.version_info >= (3,7), "This script requires at least Python 3.7"

# The game and item description files (in the same folder as this script)
game_file = 'zork.json'
item_file = 'items.json'


# Load the contents of the files into the game and items dictionaries. You can largely ignore this
# Sorry it's messy, I'm trying to account for any potential craziness with the file location
def load_files():
    try:
        __location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
        with open(os.path.join(__location__, game_file)) as json_file: game = json.load(json_file)
        with open(os.path.join(__location__, item_file)) as json_file: items = json.load(json_file)
        return (game,items)
    except:
        print("There was a problem reading either the game or item file.")
        os._exit(1)


{
    "LIBRARY": {
        "name": "Library",
        "desc": "You are currently located by the front desk of the library.",
        "exits": [{
            "exit": "NORTH",
            "target": "NELEVATOR"
        }, {
            "exit": "SOUTH",
            "target": "SELEVATOR"
        }, {
            "exit": "WEST",
            "target": "Bookshelves"
        }, {
            "exit": "EAST",
            "target": "WINDOW"
        }],
        "items": [
            {
                "item": "BOOK",
                "desc": "An old book is lying on the ground, near the front desk.",
                "take": "You pick up the old book and stuff it in your bag."
            }
        ]
    },
    "NELEVATOR": {
        "name": "North Elevators",
        "desc": "You are facing the northern elevators in the library. They don't appear to be working",
        "exits": [{
            "exit": "WEST",
            "target": "Bookshelves"
        }, {
            "exit": "SOUTH",
            "target": "LIBRARY"
        }], 
        "items": []
    },
    "SELEVATOR": {
        "name": "South Elevator"
        "desc": "You are facing the southern elevators. They don't appear to be operational.",
        "exits": [{
            "exit": "WEST",
            "target": "Bookshelves"
        }, {
            "exit": "NORTH",
            "target": "LIBRARY"
        }], 
        "items": []
    },
    "WINDOWS": {
        "name": "You look out the windows facing east.",
        "desc": "The darkness blinds your vision as you hear the rain pelt the window panes.",
        "exits": [{
            "exit": "WEST",
            "target": "LIBRARY"
        }, {
            "exit": "ENTER",
            "target": "LIBRARY"
        }],
        "items": []
    },
    "Bookshelves": {
        "name": "Bookshelves",
        "desc": "There seems to be something strange about the bookcase to the left.",
        "exits": [{
            "exit": "EAST",
            "target": "LIBRARY"
        }, {
            "exit": "WEST",
            "target": "Tunnel"
        }],
        "items": []
    },
"Tunnel": {
		"name": "Tunnel",
		"desc": "There is what appears to be a very dark, quiet, and strange tunnel that continues WEST, maybe you should check it out.",
		"exits": [{
			"exit": "WEST",
			"target": "DARK"
		}, {
            "exit": "EAST",
            "target": "Bookshelves"
		}],
		"items": []
	},
"DARK": {
		"name": "Tunnel cont.",
		"desc": "There is something lurking in the shadows. It is too dark to make out what it really is, do you continue WEST to get closer?",
		"exits": [{
			"exit": "WEST",
            "target": "LEFTG"
        }, {
            "exit": "EAST",
            "target": "Tunnel"
        }], 
        "items": []
    },
"LEFTG": {
		"name": "Monster",
		"desc": "There is a horrifying monster staring you in the eyes! Quick you need to run before it is too late!",
		"exits": [{
			"exit": "EAST",
			"target": "DARK"
		}, {
		}],
		"items": []
    },
