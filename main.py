#!/usr/bin/python

from sleeper_wrapper import User
from sleeper_wrapper import League
import json

USER_NAME = "UNKNOWN"
YEAR = 2020
PLAYER_DATABASE = {}

def player_data_base_load():
    with open('playa_list', 'r') as playa_file:
        data = json.load(playa_file)
        return data

def player_db_lookup(id):
    return PLAYER_DATABASE[id]

class Player:
    def __init__(self, id):
        self.id = id
        self.pos = 'none'
        self.name = 'none'
        self.proj_points = 0.0
        self.lookup()

    def __str__(self):
        return self.name + "\t" + self.pos

    def lookup(self):
        res = player_db_lookup(self.id)
        self.name = res["first_name"] + " " + res["last_name"]
        self.pos = res["position"]

class Roster:
    def __init__(self, name, list_of_ids):
        self.players = []
        self.league_name = name
        [self.players.append(Player(id)) for id in list_of_ids]

    def __str__(self):
        string = self.league_name + ":\n"
        for p in self.players:
            string += "\t" + str(p) + "\n"
        return string

if __name__ == "__main__":
    PLAYER_DATABASE = player_data_base_load()

    user = User(USER_NAME)
    user_id = user.get_user_id()

    leagues = [league for league in user.get_all_leagues("nfl", YEAR)]
    league_ids = [league['league_id'] for league in leagues]

    league_objs = []
    [league_objs.append(League(id)) for id in league_ids]

    my_rosters = []
    [[my_rosters.append(Roster(obj.get_league()["name"], roster["players"])) for roster in obj.get_rosters() if roster["owner_id"] == user_id] for obj in league_objs]

    [print(roster) for roster in my_rosters]
