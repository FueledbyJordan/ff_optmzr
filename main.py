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
        self.tier = 0
        self.lookup()

    def __str__(self):
        string = self.league_name + ":\n"
        for p in self.players:
            string += "\t" + str(p) + "\n"
        return string

    def __str__(self):
        return self.name + "\t" + self.pos

    def __eq__(self, other):
        return (self.tier == other.tier)

    def __ne__(self, other):
        return (self.tier != other.tier)

    def __lt__(self, other):
        return (self.tier < other.tier)

    def __le__(self, other):
        return (self.tier <= other.tier)

    def __gt__(self, other):
        return (self.tier > other.tier)

    def __ge__(self, other):
        return (self.tier >= other.tier)

    def lookup(self):
        res = player_db_lookup(self.id)
        self.name = res["first_name"] + " " + res["last_name"]
        self.pos = res["position"]

class Roster:
    def __init__(self, name, list_of_ids):
        self.players = []
        self.league_name = name
        [self.players.append(Player(id)) for id in list_of_ids]

    def __num_of_players_in_pos__(self, number, pos):
        res = []
        if (number != 0):
            res = list([p for p in self.players if p.pos == pos])
            res.sort()

        return res[0:number]

    def quarterbacks(self, number):
        return self.__num_of_players_in_pos__(number, 'QB')

    def running_backs(self, number):
        return self.__num_of_players_in_pos__(number, 'RB')

    def wide_receivers(self, number):
        return self.__num_of_players_in_pos__(number, 'WR')

    def tight_ends(self, number):
        return self.__num_of_players_in_pos__(number, 'TE')

    def defenses(self, number):
        return self.__num_of_players_in_pos__(number, 'DEF')

    def kickers(self, number):
        return self.__num_of_players_in_pos__(number, 'K')

if __name__ == "__main__":
    PLAYER_DATABASE = player_data_base_load()
    user = User(USER_NAME)
    user_id = user.get_user_id()

    league_objs = []
    [league_objs.append(League(league['league_id'])) for league in user.get_all_leagues("nfl", YEAR)]

    my_rosters = []
    [[my_rosters.append(Roster(obj.get_league()["name"], roster["players"])) for roster in obj.get_rosters() if roster["owner_id"] == user_id] for obj in league_objs]

    [[print(backs) for backs in roster.defenses(5)] for roster in my_rosters]
