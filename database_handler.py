# %%
import logging
import os
import sqlite3
import traceback
from pathlib import Path

import yaml
from sqlalchemy.engine.base import Connection
from yaml.loader import SafeLoader

module_logger = logging.getLogger('application.{}'.format(__name__))

with open("resources.yml") as file:
    resources = yaml.load(file, Loader=SafeLoader)
    database_url = Path(resources["database"]["url"])
    schema_url = Path(resources["database"]["schema"])
    sample_data = Path(resources["database"]["sample_data"])

def initialize_database(with_sampe_data): 
    module_logger.info("Initializing database.")
    if database_url.exists():
        os.remove(database_url)
        module_logger.warning("Existing database has been deleted.")
    
    execute_sql_file(schema_url)
    module_logger.debug("Empty database created.")
    if with_sampe_data:
        execute_sql_file(sample_data)
        module_logger.debug("Sample data inserted.")

def execute_script(script):
    module_logger.debug("Executing sql script.")
    connection = sqlite3.connect(database_url)
    cursor = connection.cursor()
    try:
        cursor.executescript(script).fetchall()
    except:
        module_logger.error("Failed to execute SQL script. Script :\n\n{}\n".format(script))
        traceback.print_exc()
    connection.commit()
    cursor.close()
    connection.close()

def execute_sql_file(url):
    module_logger.debug("Reading SQL file.")
    file = open(url, 'r')
    script = file.read()
    file.close()
    execute_script(script)

def execute_statement(statement):
    module_logger.info("Executing SQL statement.")
    connection = sqlite3.connect(database_url)
    cursor = connection.cursor()
    try:
        result = cursor.execute(statement).fetchall()
    except:
        module_logger.error("Failed to execute SQL statement. Statement :\n\n{}\n".format(statement))
        traceback.print_exc()
    connection.commit()
    cursor.close()
    connection.close()
    return result
