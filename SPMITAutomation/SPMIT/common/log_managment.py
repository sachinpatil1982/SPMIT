import logging
import sys
import os.path
import time
from datetime import date
import data_service

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir)))
BASE_DIR = os.path.dirname(os.path.dirname((os.path.abspath(__file__))))

log_file_path = os.path.join(BASE_DIR, 'logs', ('{0}.log' .format(str(date.today()))))
log_error_level = 'DEBUG'
log_to_db = True
db_tbl_log = 'SystemLogs'

#############################################################################################
# Log Handler for Log Management
#############################################################################################
class logDBHandler(logging.Handler):
    '''
    Customized logging handler that puts logs to the database
    '''    
    def __init__(self):
        logging.Handler.__init__(self)

    def emit(self, record):        
        print ("record.name=", format(record.name))
        print ("record.levelno=", format(record.levelno))
        print ("record.levelname=", format(record.levelname))

        self.server_id = record.msg.split('||')[0]
        self.user_id = record.msg.split('||')[1]
        self.log_msg = record.msg.split('||')[2]
        self.log_msg = self.log_msg.strip()
        self.log_msg = self.log_msg.replace('\'', '\'\'')
        self.log_created = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(record.created))

        class_common_log_sql_transactions_obj = data_service.common_log_sql_transactions.Class_Common_Logs_Sql_Transactions(self.server_id, self.user_id)
        class_common_log_sql_transactions_obj.insert_common_logs_in_database(record.name,record.levelno,record.levelname,self.log_msg,self.log_created)
       

# main seetings for the database loggin use
if (log_to_db):
    # Make the connection to databse for the logger 
    logdb = logDBHandler()

logging.basicConfig(
    filename=log_file_path,
    format='%(asctime)s %(levelname)-8s %(name)s %(message)s',
    level=logging.INFO,
    datefmt='%Y-%m-%d %H:%M:%S')

if (log_to_db):
    logging.getLogger('').addHandler(logdb)
    
