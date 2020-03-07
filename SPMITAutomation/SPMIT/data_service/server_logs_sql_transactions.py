import sys
import os.path
import logging
import data_service.ms_sql_helper
import json
from datetime import date
import time
import pandas as pd 

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir)))
logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)

BASE_DIR = os.path.dirname(os.path.dirname((os.path.abspath(__file__))))
log_file_path = os.path.join(BASE_DIR, 'logs', ('{0}.log' .format(str(date.today()))))
log_error_level = logging.DEBUG
log_to_db = True
db_tbale_pog = 'Log'
log = logging.getLogger('Common_Logs_Sql_Transactions.Py')
log.setLevel(log_error_level)

class Class_Common_Logs_Sql_Transactions:
    def __init__(self, server_id, user_id):
            #log.debug('{0}||{1}||Common_Logs_Sql_Transactions Initiatied' .format(server_id, user_id))
            self.server_id = server_id
            self.user_id = user_id               
            self.server_logs = []

#/***************************************************************************
# Save text in Database 
#/***************************************************************************
    def save_server_logs_in_db(self, server_log_file_path, isfiltered):
        try:
            # self.server_log_file_path = server_log_file_path
            print(server_log_file_path)
            #log.debug('{0}||{1}||Class_Solution_Management - fetchsave_server_logs_db_server_logs - Started' .format(self.server_id, self.user_id))
            Class_Ms_Sql_Helper_Obj = data_service.ms_sql_helper.Class_Ms_Sql_Helper()
            sqlDBConn = Class_Ms_Sql_Helper_Obj.getConn()
            sqlCursor = sqlDBConn.cursor()
            sp_name = ""
            if (isfiltered == 1):
                sp_name = "sp_insert_filtered_server_logs"
            else:
                sp_name = "sp_insert_server_logs"        
            sql = """\
            DECLARE @IsTransactionSuccessfull_value INT;
            DECLARE @TransactionMessage_value nvarchar(400);
            EXEC """ + sp_name + """ @ServerId = %d, @UserId = %s, @ServerLogFilePath = %s, @IsTransactionSuccessfull = @IsTransactionSuccessfull_value OUTPUT, @TransactionMessage = @TransactionMessage_value OUTPUT;
            SELECT @IsTransactionSuccessfull_value AS IsTransactionSuccessfull_value, @TransactionMessage_value AS TransactionMessage_value ;
            """            
            params = (self.server_id, self.user_id, server_log_file_path,)
            print(sql)
            sqlCursor.execute(sql, params)            

            rows = sqlCursor.fetchall()
            while rows:
                print(rows)
                if sqlCursor.nextset():
                    rows = sqlCursor.fetchall()
                else:
                    rows = None
            
            sqlDBConn.commit()
            sqlDBConn.close()
            #log.debug('{0}||{1}||Class_Solution_Management - save_server_logs_db - Completed' .format(self.server_id, self.user_id))
        except Exception as e:
            error_msg = 'Critical exception raised while fetching server logs - {0}' .format(str(e)) 
            print(error_msg)
            Exception(error_msg)
            #log.error('{0}||{1}||Class_Solution_Management - save_server_logs_db - Exception || {2}' .format(self.server_id, self.user_id, error_msg))

#/***************************************************************************
# Read ServeLogs From Database 
#/***************************************************************************
    def get_server_logs_from_db(self):
        try:
            #log.debug('{0}||{1}||Class_Solution_Management - fetchsave_server_logs_db_server_logs - Started' .format(self.server_id, self.user_id))
            Class_Ms_Sql_Helper_Obj = data_service.ms_sql_helper.Class_Ms_Sql_Helper()
            sqlDBConn = Class_Ms_Sql_Helper_Obj.getConn()
            sqlCursor = sqlDBConn.cursor()

            sql = "EXEC sp_get_server_logs @ServerId = {0}" .format(self.server_id)
            # sql = "EXEC sp_get_server_logs @ServerId = %d"
            # params = (self.server_id,)
            print(sql)
            # sqlCursor.execute(sql, params)
            # result = sqlCursor.fetchall()
            # print (result)
            # columns = [column[0] for column in sqlCursor.description]
            # df = pd.DataFrame.from_records(result, columns=columns)
            df = pd.read_sql(sql, con=sqlDBConn)#.head(10)
            # print(df)
            # print(len(df.index))  
            df.set_index('Id', inplace=True)

            sqlDBConn.commit()
            sqlDBConn.close()

            return df
            #log.debug('{0}||{1}||Class_Solution_Management - save_server_logs_db - Completed' .format(self.server_id, self.user_id))
        except Exception as e:
            error_msg = 'Critical exception raised while fetching server logs - {0}' .format(str(e)) 
            print(error_msg)
            Exception(error_msg)
            return None
            #log.error('{0}||{1}||Class_Solution_Management - save_server_logs_db - Exception || {2}' .format(self.server_id, self.user_id, error_msg))
       