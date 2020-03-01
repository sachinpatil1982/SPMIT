import sys
import os.path
import common
import business
import logging
import infrastructure
import data_service.server_logs_sql_transactions

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir)))
common.log_managment.logging.basicConfig(stream=sys.stdout, level=common.log_managment.logging.DEBUG)
log_erro_level = 'DEBUG'
log = common.log_managment.logging.getLogger('solution_management.Py')
log.setLevel(log_erro_level)

class Class_Solution_Management:
    def __init__(self, server_id, user_id):
        log.debug('{0}||{1}||Class_Solution_Management Initiatied' .format(server_id, user_id))
        self.server_id = server_id
        self.user_id = user_id   
        self.server_log_file_path = 'C:\\Temp\\ServerLogs\\results.txt'
        self.server_logs = []

#/***************************************************************************
# Read text file at given file path 
#/***************************************************************************
    def fetch_server_logs_in_db(self):        
        try:
            log.debug('{0}||{1}||Class_Solution_Management - fetch_server_logs_in_db - Started' .format(self.server_id, self.user_id))
            self.fetch_server_logs()
            self.save_server_logs_db()
            self.get_server_logs_db()
            #print (self.server_logs)
            log.debug('{0}||{1}||Class_Solution_Management - fetch_server_logs_in_db - Completed' .format(self.server_id, self.user_id))
        except Exception as e:
            error_msg = 'Critical exception raised while fetching server logs - {0}' .format(str(e)) 
            log.error('{0}||{1}||Class_Solution_Management - fetch_server_logs_in_db - Exception || {2}' .format(self.server_id, self.user_id, error_msg))
        
#/***************************************************************************
# Read text file at given file path 
#/***************************************************************************
    def fetch_server_logs(self):
        try:
            log.debug('{0}||{1}||Class_Solution_Management - fetch_server_logs - Started' .format(self.server_id, self.user_id))
            Class_File_Management_Obj = infrastructure.file_management.Class_File_Management(self.server_id, self.user_id)
            self.server_logs = Class_File_Management_Obj.read_txt_file(self.server_log_file_path)
            log.debug('{0}||{1}||Class_Solution_Management - fetch_server_logs - Completed' .format(self.server_id, self.user_id))
        except Exception as e:
            error_msg = 'Critical exception raised while fetching server logs - {0}' .format(str(e)) 
            log.error('{0}||{1}||Class_Solution_Management - fetch_server_logs - Exception || {2}' .format(self.server_id, self.user_id, error_msg))
        
#/***************************************************************************
# Save text in Database 
#/***************************************************************************
    def save_server_logs_db(self):
        try:
            log.debug('{0}||{1}||Class_Solution_Management - fetchsave_server_logs_db_server_logs - Started' .format(self.server_id, self.user_id))
            class_server_logs_sql_tranasctions_obj = data_service.server_logs_sql_transactions.Class_Common_Logs_Sql_Transactions(self.server_id, self.user_id)
            class_server_logs_sql_tranasctions_obj.save_server_logs_in_db()            
            log.debug('{0}||{1}||Class_Solution_Management - save_server_logs_db - Completed' .format(self.server_id, self.user_id))
        except Exception as e:
            error_msg = 'Critical exception raised while saving server logs - {0}' .format(str(e)) 
            log.error('{0}||{1}||Class_Solution_Management - save_server_logs_db - Exception || {2}' .format(self.server_id, self.user_id, error_msg))

#/***************************************************************************
# Read ServeLogs From Database 
#/***************************************************************************
    def get_server_logs_db(self):
        try:
            log.debug('{0}||{1}||Class_Solution_Management - get_server_logs_db - Started' .format(self.server_id, self.user_id))
            class_server_logs_sql_tranasctions_obj = data_service.server_logs_sql_transactions.Class_Common_Logs_Sql_Transactions(self.server_id, self.user_id)
            class_server_logs_sql_tranasctions_obj.get_server_logs_from_db()            
            log.debug('{0}||{1}||Class_Solution_Management - get_server_logs_db - Completed' .format(self.server_id, self.user_id))
        except Exception as e:
            error_msg = 'Critical exception raised while fetching server logs - {0}' .format(str(e)) 
            log.error('{0}||{1}||Class_Solution_Management - get_server_logs_db - Exception || {2}' .format(self.server_id, self.user_id, error_msg))
