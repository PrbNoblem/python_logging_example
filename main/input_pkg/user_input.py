import logging
#from main.output_pkg.output_stuff import handle_output
import output_pkg.output_stuff
logger = logging.getLogger('test_logger')


def handle_input():
    running = True
    print("Enter input")
    #print('in input, __name__:', __name__)
    while running:
        logger.info('getting user input')
        usr_input = input()
        running = output_pkg.output_stuff.handle_output(usr_input)




