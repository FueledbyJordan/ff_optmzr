# Fantasy Football Optimizer

This project is used to recommend Boris Chen's optimal picks for a user's available players in all leagues available to that user in the Sleeper fantasy football app.

The python script is looking for a list of players in a file called "playa_list".
* To get this list, you can call the following
```
curl https://api.sleeper.app/v1/players/nfl > playa_list
```
