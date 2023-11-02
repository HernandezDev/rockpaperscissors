
from leaderboards import leaderboards
from exit import exit

def initInput(game_options, user_available_options, players):
    user_wants_out = False
    while True:
        print("Opciones disponibles:")
        print("")
        for option in user_available_options:
            print(f"- {option.capitalize()}")
        print("-------------------------------")

        selected_option = input("Ingrese su opcion -> ")

        selected_option = selected_option.lower()
        if selected_option in game_options:
            return selected_option, False
            break
        elif selected_option == "ranking":
            while user_wants_out == False:
                user_wants_out = leaderboards(players)
            return selected_option, False
            break
        elif selected_option == "exit":
            return selected_option, exit("Desea finalizar el juego? y/n -> ")
        else:
            print("-------------------------------")
            print("No ha seleccionado una de las opciones disponibles.")
            print("-------------------------------")