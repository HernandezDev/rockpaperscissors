"""
Juego de piedra, papel o tijera.

"""

import random
from init_input import initInput
from exit import exit
from game_logic import playing_logic

game_options = ("piedra", "papel", "tijera")
user_available_options = ("piedra", "papel", "tijera", "ranking", "exit")
selected_option=""
exit_game = False
players = {
    'user': {
        'points':0,
        'sel_option':""
    },
    'npc': {
        'points':0,
        'sel_option':""
    }
}


print("Juego de piedra papel o tijera")
print("-------------------------------")

"""
    whos_winning = max(players, key=players.get)
    print(f"Va ganando {whos_winning} con {players[whos_winning]}")
"""


while exit_game == False: 
    players["user"]["sel_option"] = ""

    players["npc"]["sel_option"] = random.choice(game_options)
    while players["user"]["sel_option"] not in game_options:
        players["user"]["sel_option"], exit_game = initInput(game_options, user_available_options, players)
        if exit_game == True:
            players["user"]["sel_option"] = ""
            break
    if exit_game == True:
        players["user"]["sel_option"] = ""
        break


    print("-------------------------------")
    print("Elecciones elegidas por los participantes:")
    print(f"npc -> {players["npc"]["sel_option"]}")
    print(f"Usuario -> {players["user"]["sel_option"]}")
    print("-------------------------------")
    
    players, exit_game = playing_logic(players)
