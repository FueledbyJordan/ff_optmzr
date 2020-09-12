#!/usr/bin/python

from sleeper_wrapper import User
from sleeper_wrapper import League

USER_NAME = "USERNAME_HERE"
YEAR = 2020

if __name__ == "__main__":
    user = User(USER_NAME)
    user_id = user.get_user_id()
    leagues = [league for league in user.get_all_leagues("nfl", YEAR)]
    league_ids = [league['league_id'] for league in leagues]
    league_objs = []
    [league_objs.append(League(id)) for id in league_ids]

    my_rosters = []
    for obj in league_objs:
        [my_rosters.append({"league" : obj.get_league()["name"], "players" : roster["players"]}) for roster in obj.get_roster() if roster["owner_id"] == user_id]

    my_playas = []

    #for roster in my_rosters:
        #playa for playa in roster["players"] if playa[
