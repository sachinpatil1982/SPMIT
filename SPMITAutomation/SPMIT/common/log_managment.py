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
    def __init__(self, sql_conn, sql_cursor, db_tbl_log):
        logging.Handler.__init__(self)
        self.sql_cursor = sql_cursor
        self.sql_conn = sql_conn
        self.db_tbl_log = "SystemLogs"

    def emit(self, record):
        tm = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(record.created))
        print ("record.name=", format(record.name))
        print ("record.levelno=", format(record.levelno))
        print ("record.levelname=", format(record.levelname))

        self.server_id = record.msg.split('||')[0]
        self.user_id = record.msg.split('||')[1]
        self.log_msg = record.msg.split('||')[2]
        self.log_msg = self.log_msg.strip()
        self.log_msg = self.log_msg.replace('\'', '\'\'')
        sql = 'INSERT INTO ' + self.db_tbl_log + ' (ServerId, UserId, ModuleName, LogLevel, LogLevelName, ' + \
            'LogMessage, CreatedDate, CreatedBy) ' + \
            'VALUES (' + \
            '' + self.server_id + ', ' + \
            '\'' + str(self.user_id) + '\', ' + \
            '\'' + str(record.name) + '\', ' + \
            '\'' + str(record.levelno) + '\', ' + \
            '\'' + str(record.levelname) + '\', ' + \
            '\'' + str(self.log_msg) + '\', ' + \
            '(convert(datetime, \'' + tm + '\')), ' + \
            '\'' + str(self.user_id) + '\')'
        try:
            self.sql_cursor.execute(sql)
            self.sql_conn.commit()
        except Exception as inst:
            print (sql)
            print (inst)
            print ('CRITVAL DB ERROR! Logging to Database not possible!')

# main seetings for the database loggin use
if (log_to_db):
    # Make the connection to databse for the logger
    dalSQL = data_service.ms_sql_helper.DBServer()
    log_conn = dalSQL.getConn()
    log_cursor = log_conn.cursor()    
    logdb = logDBHandler(log_conn, log_cursor, db_tbl_log)

logging.basicConfig(
    filename=log_file_path,
    format='%(asctime)s %(levelname)-8s %(name)s %(message)s',
    level=logging.INFO,
    datefmt='%Y-%m-%d %H:%M:%S')

if (log_to_db):
    logging.getLogger('').addHandler(logdb)
    
