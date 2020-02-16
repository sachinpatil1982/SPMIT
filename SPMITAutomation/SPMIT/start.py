import sys
import os.path
import infrastructure
import common
import data_service
import business
import logging

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir)))
common.log_managment.logging.basicConfig(stream=sys.stdout, level=common.log_managment.logging.DEBUG)
log_erro_level = 'DEBUG'
log = common.log_managment.logging.getLogger('Main_Start.Py')
log.setLevel(log_erro_level)

some_string = "Test Data"
server_id = 1
user_id = 'SachinPatil'
log.debug('{0}||{1}||Application Process Cycle' .format(server_id, user_id))
infrastructure.file_management.stringLenghtTest_file(some_string)

dalSQL = data_service.ms_sql_helper.DBServer()
sqlDBConn = dalSQL.getConn()
cursor = sqlDBConn.cursor()