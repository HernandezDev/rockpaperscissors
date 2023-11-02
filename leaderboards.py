from exit import exit

def leaderboards(players):
    print("-------------------------------")
    print("Jugador ------> Puntos")
    for key, value in players.items(): 
        print(f"{key} ---------> {value["points"]}")
    return exit("Desea volver a la pagina principal? y/n -> ")