import common
import sys
import os.path
import data_service
import json
import datetime as dt
import time
import csv

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir)))
common.log_managment.logging.basicConfig(stream=sys.stdout, level=common.log_managment.logging.DEBUG)
log_erro_level = 'DEBUG'
log = common.log_managment.logging.getLogger('file_management.py')
log.setLevel(log_erro_level)

class Class_File_Management:
    def __init__(self, server_id, user_id):
        log.debug('{0}||{1}||Class_File_Management Initiatied' .format(server_id, user_id))
        self.server_id = server_id
        self.user_id = user_id


#/***************************************************************************
# Read text file at given file path
#/***************************************************************************
    def read_txt_file(self, file_path):
        try:
            log.debug('{0}||{1}||Class_File_Management - read_txt_file - Started' .format(self.server_id, self.user_id))
            if os.path.exists(file_path):
                # with open(file_path, newline='') as csvfile:
                #     server_logs = csv.reader(csvfile, delimiter=',')
                
                # f = open(file_path, 'r') # Open file on read mode
                # server_logs = f.read().split("\n") # Create a list containing all lines
                # f.close() # Close file
                server_logs = open(file_path).read().splitlines()
                # count=0
                # for x in server_logs:
                #     print(x)
                #     count += 1
                #     if count == 50:
                #         break
                
                #print(server_logs)

            else:
                raise Exception('Server Log Not Exist At Requested Path - {0}', file_path)
            log.debug('{0}||{1}||Class_File_Management - read_txt_file - Completed' .format(self.server_id, self.user_id))
            return server_logs
        except Exception as e:
            error_msg = 'Critical exception raised while reading text file - {0}' .format(str(e))
            log.error('{0}||{1}||Class_File_Management - read_txt_file - Exception - {2}' .format(self.server_id, self.user_id, error_msg))













