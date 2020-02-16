import common
import sys
import os.path
import data_service
import infrastructure
import json
import datetime as dt
import time

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir)))
common.log_managment.logging.basicConfig(stream=sys.stdout, level=common.log_managment.logging.DEBUG)
log_erro_level = 'DEBUG'
log = common.log_managment.logging.getLogger('Infrastructure_File_Managment.Py')
log.setLevel(log_erro_level)
user_id = 'SachinPatil'
server_id = 1

def stringLenghtTest_file(inStr):
    log.debug('{0}||{1}||Method invoked with input parameter - {2}' .format(server_id, user_id, inStr))
    inStr = "Input String Modified - {0}" .format (inStr)
    log.debug('{0}||{1}||Method modified input parameter - {2}' .format(server_id, user_id, inStr))
    return len(inStr)