import logging

def handle_input():
    running = True
    print("Enter input")
    while running:
        usr_input = input()
        print("User input:", usr_input)
        if usr_input == 'quit' or usr_input == 'exit' or usr_input == '0':
            print('Exiting')
            logger.debug("User entered exit command, exiting.")
            running = False
        else:
            logger.debug(f"User entered {usr_input}")



