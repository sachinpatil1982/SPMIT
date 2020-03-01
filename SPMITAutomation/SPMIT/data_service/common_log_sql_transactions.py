import sys
import os.path
import data_service.ms_sql_helper
import time
from datetime import date
import logging

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir)))
logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)

BASE_DIR = os.path.dirname(os.path.dirname((os.path.abspath(__file__))))
log_file_path = os.path.join(BASE_DIR, 'logs', ('{0}.log' .format(str(date.today()))))
log_error_level = logging.DEBUG
log_to_db = True
db_tbale_pog = 'Log'
log = logging.getLogger('Common_Log_Sql_Transactions.Py')
log.setLevel(log_error_level)

class Class_Common_Logs_Sql_Transactions:
    def __init__(self, server_id, user_id):
        #log.debug('{0}||{1}||Class_Solution_Management Initiatied' .format(server_id, user_id))        
        self.db_tbl_log = "SystemLogs"
        self.server_id = server_id
        self.user_id = user_id

    def insert_common_logs_in_database(self, name, levelno, levelname, log_msg, log_created):      
        try:
            #log.debug('{0}||{1}||insert_common_logs_in_database Started' .format(self.server_id, self.user_id))
            Class_Ms_Sql_Helper_Obj = data_service.ms_sql_helper.Class_Ms_Sql_Helper()
            log_conn = Class_Ms_Sql_Helper_Obj.getConn()
            log_cursor = log_conn.cursor()   
            sql = 'INSERT INTO ' + self.db_tbl_log + ' (ServerId, UserId, ModuleName, LogLevel, LogLevelName, ' + \
                'LogMessage, CreatedDate, CreatedBy) ' + \
                'VALUES (' + \
                '' + self.server_id + ', ' + \
                '\'' + str(self.user_id) + '\', ' + \
                '\'' + str(name) + '\', ' + \
                '\'' + str(levelno) + '\', ' + \
                '\'' + str(levelname) + '\', ' + \
                '\'' + str(log_msg) + '\', ' + \
                '(convert(datetime, \'' + log_created + '\')), ' + \
                '\'' + str(self.user_id) + '\')'

            log_cursor.execute(sql)
            log_conn.commit()
            log_conn.close()
            #log.debug('{0}||{1}||insert_common_logs_in_database Completed' .format(self.server_id, self.user_id))
        except Exception as e:
            error_msg = 'Critical exception raised while saving  common logs - {0}' .format(str(e)) 
            print(error_msg)
            Exception(error_msg)
            #log.error('{0}||{1}||Class_Common_Logs_Sql_Transactions - insert_common_logs_in_database - Exception || {2}' .format(self.server_id, self.user_id, error_msg))
       

