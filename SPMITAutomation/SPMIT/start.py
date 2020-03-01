import sys
import os.path
import common
import business
import logging

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir)))
common.log_managment.logging.basicConfig(stream=sys.stdout, level=common.log_managment.logging.DEBUG)
log_erro_level = 'DEBUG'
log = common.log_managment.logging.getLogger('Main_Start.Py')
log.setLevel(log_erro_level)

#/***************************************************************************
# Project Intiation 
#/***************************************************************************
some_string = "Test Data"
server_id = 1
user_id = 'SachinPatil'
log.debug('{0}||{1}||Application Process Cycle' .format(server_id, user_id))

#/***************************************************************************
# Test SQL Connection 
#/***************************************************************************
# infrastructure.file_management.stringLenghtTest_file(some_string)
# Class_Ms_Sql_Helper_Obj = data_service.ms_sql_helper.Class_Ms_Sql_Helper()
# sqlDBConn = Class_Ms_Sql_Helper_Obj.getConn()
# cursor = sqlDBConn.cursor()

#/***************************************************************************
# Fetch Server Logs in Database 
#/***************************************************************************
try:
    log.debug('{0}||{1}||Fetch Server Logs in Database - Started' .format(server_id, user_id))
    Class_File_Management_Obj = business.solution_management.Class_Solution_Management(server_id, user_id)
    Class_File_Management_Obj.fetch_server_logs_in_db()
    log.debug('{0}||{1}||Fetch Server Logs in Database - Completed' .format(server_id, user_id))
except Exception as e:
    error_msg='Critical exception raised while fetching server logs in database'
    print(error_msg)
    log.error('{0}||{1}||Fetch Server Logs in Database - Exception || {2}' .format(server_id, user_id, error_msg))
        





































































































































































































































































