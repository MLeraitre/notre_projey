import argparse
import logging
import traceback

import database_handler

logger = logging.getLogger('application')
logger.setLevel(logging.DEBUG)

file_handler = logging.FileHandler('application.log')
file_handler.setLevel(logging.DEBUG)

console_handler = logging.StreamHandler()
console_handler.setLevel(logging.INFO)

formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
file_handler.setFormatter(formatter)
console_handler.setFormatter(formatter)

logger.addHandler(file_handler)
logger.addHandler(console_handler)

parser = argparse.ArgumentParser()
parser.add_argument("--init-db", "-i", help="Possible values : {sample, empty}. Creates a new database and leaves it empty or inserts sample data.")

def main():
    logger.info("Application started.")
    args = parser.parse_args()
    if args.init_db:
        init_arg = args.init_db
        if init_arg == "sample":
            try:
                database_handler.initialize_database(True)
            except:
                logger.error("Failed to initialize database.")
                traceback.print_exc()
        else:
            try:
                database_handler.initialize_database(False)
            except:
                logger.error("Failed to initialize database.")
                traceback.print_exc()
            if init_arg != "empty":
                logger.warning(f"{init_arg} is not a known value for --init-database. Database left empty by default. Possible values : sample, empty.")
        logging.info("Application ended.")

if __name__=="__main__":
    main()
