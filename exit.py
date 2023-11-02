def exit(exit_text):
    print("")
    user_wants_out = input(exit_text)
    if user_wants_out == "y":
        return True
    else: 
        return False