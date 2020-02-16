SELECT * FROM SystemLogs
INSERT INTO SystemLogs (ServerId, UserId, ModuleName, LogLevel, LogLevelName, LogMessage, CreatedDate, CreatedBy) 
VALUES (1, 'SachinPatil', 'Infrastructure_File_Managment.Py', '10', 'DEBUG', 
'Method modified input parameter - Input String Modified - Test Data', 
(convert(datetime, '20-02-16 18:05:32')), 'SachinPatil')

SELECT * FROM ServerDetails
INSERT INTO ServerDetails 
SELECT 'Test Server','Test Server', 1, GETDATE(), 'SachinPatil'

