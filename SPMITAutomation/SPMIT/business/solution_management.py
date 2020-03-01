import sys
import os.path
import common
import business
import logging
import infrastructure
import data_service.server_logs_sql_transactions
import pandas as pd 
import numpy as np

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
        self.server_filtered_log_file_path = 'C:\\Temp\\ServerLogs\\results_filtered.txt'
        self.server_logs = []
        self.server_logs_db = []

#/***************************************************************************
# Read text file at given file path
#/***************************************************************************
    def fetch_server_logs_in_db(self):
        try:
            log.debug('{0}||{1}||Class_Solution_Management - fetch_server_logs_in_db - Started' .format(self.server_id, self.user_id))
            self.fetch_server_logs()
            self.save_server_logs_db(server_log_file_path_db=self.server_log_file_path, filtered=0)
            self.get_server_logs_db()
            #print (self.server_logs)
            log.debug('{0}||{1}||Class_Solution_Management - fetch_server_logs_in_db - Completed' .format(self.server_id, self.user_id))
            return self.server_logs_db
        except Exception as e:
            error_msg = 'Critical exception raised while fetching server logs - {0}' .format(str(e))
            log.error('{0}||{1}||Class_Solution_Management - fetch_server_logs_in_db - Exception || {2}' .format(self.server_id, self.user_id, error_msg))
            return None

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
    def save_server_logs_db(self, server_log_file_path_db, filtered):
        try:
            log.debug('{0}||{1}||Class_Solution_Management - fetchsave_server_logs_db_server_logs - Started' .format(self.server_id, self.user_id))
            class_server_logs_sql_tranasctions_obj = data_service.server_logs_sql_transactions.Class_Common_Logs_Sql_Transactions(self.server_id, self.user_id)
            class_server_logs_sql_tranasctions_obj.save_server_logs_in_db(server_log_file_path_db,filtered)
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
            self.server_logs_db = class_server_logs_sql_tranasctions_obj.get_server_logs_from_db()
            #print(len(self.server_logs_db.index))
            log.debug('{0}||{1}||Class_Solution_Management - get_server_logs_db - Completed' .format(self.server_id, self.user_id))
        except Exception as e:
            error_msg = 'Critical exception raised while fetching server logs - {0}' .format(str(e))
            log.error('{0}||{1}||Class_Solution_Management - get_server_logs_db - Exception || {2}' .format(self.server_id, self.user_id, error_msg))
            self.server_logs_db = None

#/***************************************************************************
# Read ServeLogs From Database
#/***************************************************************************
    def cleansing_server_logs(self, server_logs):
        try:
            log.debug('{0}||{1}||Class_Solution_Management - cleansing_server_logs - Started' .format(self.server_id, self.user_id))
            if (server_logs.empty):
                Exception ('Critical exception raised while cleansing server logs - server_logs input paramater is Null or Empty')
            cleansing_server_logs_nan = self.cleansing_server_logs_avoid_null(server_logs)   

            if (cleansing_server_logs_nan.empty):
                Exception ('Critical exception raised while cleansing server logs with null columns - cleansing_server_logs_nan input paramater is Null or Empty')
            cleansing_server_logs_split = self.cleansing_server_logs_filter_columns(cleansing_server_logs_nan)
            
            if (cleansing_server_logs_split.empty):
                Exception ('Critical exception raised while cleansing server logs to get set of data for analaysis - cleansing_server_logs_split data is Null or Empty')

            cleansing_server_logs_split.to_csv(self.server_filtered_log_file_path, encoding='utf-8', index=False, header=False, sep='|' )

            self.save_server_logs_db(server_log_file_path_db=self.server_filtered_log_file_path, filtered=1)

            # print (cleansing_server_logs_split)
            log.debug('{0}||{1}||Class_Solution_Management - cleansing_server_logs - Completed' .format(self.server_id, self.user_id))
        except Exception as e:
            error_msg = 'Critical exception raised while cleansing server logs - {0}' .format(str(e))
            log.error('{0}||{1}||Class_Solution_Management - cleansing_server_logs - Exception || {2}' .format(self.server_id, self.user_id, error_msg))

#/***************************************************************************
# Filter null value columns to avoid errors
#/***************************************************************************
    def cleansing_server_logs_avoid_null(self, server_logs):
        try:
            log.debug('{0}||{1}||Class_Solution_Management - cleansing_server_logs_avoid_null - Started' .format(self.server_id, self.user_id))
            #print(server_logs)            
            # print (server_logs)
            # cleansing_server_logs = server_logs.dropna(inplace = True)
            # cleansing_server_logs = server_logs.dropna(thresh=2)
            # cleansing_server_logs = server_logs.ServerLogs.notnull()
            # cleansing_server_logs_nan = server_logs.dropna(axis = 0, how ='any')

            # drop rows with missing value
            # print(len(server_logs.index))
            cleansing_server_logs_nan = server_logs.dropna()
            # print(len(cleansing_server_logs_nan.index))
                        
            log.debug('{0}||{1}||Class_Solution_Management - cleansing_server_logs_avoid_null - Completed' .format(self.server_id, self.user_id))
            return cleansing_server_logs_nan
        except Exception as e:
            error_msg = 'Critical exception raised while cleansing server logs with null - {0}' .format(str(e))
            log.error('{0}||{1}||Class_Solution_Management - cleansing_server_logs_avoid_null - Exception || {2}' .format(self.server_id, self.user_id, error_msg))
            return None

#/***************************************************************************
# Filter unwanted columns and data to get final set of data
#/***************************************************************************
    def cleansing_server_logs_filter_columns(self, cleansing_server_logs_nan):
        try:
            log.debug('{0}||{1}||Class_Solution_Management - cleansing_server_logs_filter_columns - Started' .format(self.server_id, self.user_id))
            
            cleansing_server_logs_split_1 = cleansing_server_logs_nan.ServerLogs.str.split("\"",expand=True)
            cleansing_server_logs_split_2 = cleansing_server_logs_split_1[0].str.split("-",expand=True)
            cleansing_server_logs_split_3 = cleansing_server_logs_split_2[0].str.split(" ",expand=True)
            cleansing_server_logs_split_4 = cleansing_server_logs_split_1[2].str.split(" ",expand=True)
            # cleansing_server_logs_split_2 = cleansing_server_logs_split_2.merge(cleansing_server_logs_split_1, left_on='Id', right_on='Id')
            # cleansing_server_logs_split_3 = pd.concat([cleansing_server_logs_split_2, cleansing_server_logs_split_1], axis=1)
            
            cleansing_server_logs_split_3[1] = cleansing_server_logs_split_2[2].str.strip()
            cleansing_server_logs_split_3[2] = cleansing_server_logs_split_1[1].str.strip()
            cleansing_server_logs_split_3[3] = cleansing_server_logs_split_4[1].str.strip()
            cleansing_server_logs_split_3[4] = cleansing_server_logs_split_4[2].str.strip()
            cleansing_server_logs_split_3[5] = cleansing_server_logs_split_1[3].str.strip()
            cleansing_server_logs_split_3[6] = cleansing_server_logs_split_1[5].str.strip()  
            # cleansing_server_logs_split_2[8] = str(cleansing_server_logs_split_1[6][7])            

            pd.set_option('display.max_rows', cleansing_server_logs_split_3.shape[0]+1)
            for row in cleansing_server_logs_split_3.iterrows():
                # A = str(row[1][7])
                # print('The value of ServerLogs: {}'.format(A))
                print(row)
            print(len(cleansing_server_logs_split_3.index))
            print(len(cleansing_server_logs_split_3.columns))
            # print (cleansing_server_logs_split)
            log.debug('{0}||{1}||Class_Solution_Management - cleansing_server_logs_filter_columns - Completed' .format(self.server_id, self.user_id))
            return cleansing_server_logs_split_3
        except Exception as e:
            error_msg = 'Critical exception raised while cleansing server logs by filter redundant columns - {0}' .format(str(e))
            log.error('{0}||{1}||Class_Solution_Management - cleansing_server_logs_filter_columns - Exception || {2}' .format(self.server_id, self.user_id, error_msg))
            return None
