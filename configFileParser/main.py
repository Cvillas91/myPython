from configparser import ConfigParser

config = ConfigParser()

config["DEFAULT"] = {
    "numberdigits" : 6,
    "numbertries" : 8,
    "playername": "Player"
}

config["CarlosVillas"] = {
    "numberdigits" : 10,
    "numbertries" : 6,
    "playername": "Carlos"
}

config["SUDO"] = {
    "numberdigits" : 6,
    "numbertries" : 8,
    "playername": "Cheater",
    "cheats" : "on"
}

with open("number_guessing.ini", "w") as f:
    config.write(f)
