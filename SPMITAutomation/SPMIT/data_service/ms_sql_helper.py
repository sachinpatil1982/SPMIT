import logging
import sys
import os.path
import infrastructure
import json
from datetime import date
import time
import pymssql

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir)))
logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)

BASE_DIR = os.path.dirname(os.path.dirname((os.path.abspath(__file__))))
log_file_path = os.path.join(BASE_DIR, 'logs', ('{0}.log' .format(str(date.today()))))
log_error_level = logging.DEBUG
log_to_db = True
db_tbale_pog = 'Log'
log = logging.getLogger('DataService_SQL_Helper.Py')
log.setLevel(log_error_level)

class DBServer:
    def __init__(self):
        self.DB_CONFIG = {
            'name': 'SPMIT',
            'host': 'EC2AMAZ-848AN2Q',
            'user': 'spmit_admin',
            'pass': 'SPMITadmin1234',
        }

    def getConn(self):
        conn = pymssql.connect(
            server=self.DB_CONFIG["host"],
            user=self.DB_CONFIG["user"],
            password=self.DB_CONFIG["pass"],
            database=self.DB_CONFIG["name"],
        )
        try:
            c = conn.cursor()
        except pymssql.MssqlDatabaseException:
            connected = False            
            print("Error in SQL Server Connection")
        else:
            connected = True
            print("SQL Server Connected")
        return conn

    def setup_cursor(self, dbc):
        dbc.excute('SET NAMES utf8;')
        dbc.excute('SET CHARACTER SET utf8;')
        dbc.excute('SET character_set_connection=utf8;')
        return dbc