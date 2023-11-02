from exit import exit

def playing_logic(players):
    if players["npc"]["sel_option"] == players["user"]["sel_option"]:
        print("Empate, ninguno gana puntos...")
    elif players["npc"]["sel_option"] == "piedra" and players["user"]["sel_option"] == "tijera":
       print("npc gana!")
       players["npc"]["points"] += 1
    elif players["user"]["sel_option"] == "piedra" and players["npc"]["sel_option"] == "tijera":
       print("ganaste!")
       players["user"]["points"] += 1
    elif players["npc"]["sel_option"] == "tijera" and players["user"]["sel_option"] == "papel":
       print("npc gana!")
       players["npc"]["points"] += 1
    elif players["user"]["sel_option"] == "tijera" and players["npc"]["sel_option"] == "papel":
       print("ganaste!")
       players["user"]["points"] += 1
    elif players["npc"]["sel_option"] == "papel" and players["user"]["sel_option"] == "piedra":
       print("npc gana!")
       players["npc"]["points"] += 1
    elif players["user"]["sel_option"] == "papel" and players["npc"]["sel_option"] == "piedra":
       print("ganaste!")
       players["user"]["points"] += 1

    print("")
    print("")
    whos_winning = ""
    if players["user"]["points"] == players["npc"]["points"]:
        print(f"Van empatados con {players["user"]["points"]}")
    elif players["user"]["points"] > players["npc"]["points"]:
        print(f"Va ganando Usuario con {players["user"]["points"]}")
    else:
        print(f"Va ganando npc con {players["npc"]["points"]}")
    print("")



   
    return players, exit("desea salir? y/n -> ")   
 