# Gives input handler functions to use

def y_n(question):
    response = None
    while response == None or response != "y" or response != "n":
        response = input(question + " y/n\n").strip().lower()

        if response == "y":
            return True
        elif response == "n":
            return False
        else:
            print("Response not accepted please try again using y/n\n")