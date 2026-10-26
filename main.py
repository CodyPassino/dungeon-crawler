from handlers.input_handler import InputHandler

import file_manager
import constants
import time

def main():
    username = None
    while username == None:
        username = input("Please insert username:\n")

    input_handler = InputHandler(username)

    input_handler.enter_dungeon()
    

    while True:
        #input_handler.q_attack(input("Do you wish to attack? y/n"))
        input_handler.chest_open()

if __name__ == '__main__':
    main()

