import logging
logger = logging.getLogger('test_logger')




def handle_output(output):
    print('in output: __name__:', __name__)
    #print("User input:", output)
    if output == 'quit' or output == 'exit' or output == '0':
        print('Exiting')
        logger.debug("User entered exit command, exiting.")
        return False
    else:
        logger.debug(f"User entered {output}")
        return True